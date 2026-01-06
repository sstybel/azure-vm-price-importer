import os
import shutil
import requests
from datetime import datetime

def print_line(is_silent_enabled=False):
    if not is_silent_enabled:
        print("--------------------------------------------------------------------\n")

def print_app_title(app_name, app_author, is_silent_enabled=False):
    if not is_silent_enabled:
        print(f"\n{app_name}")
        print(f"{app_author}")
        print_line()

def print_start_logs(log_filename, is_silent_enabled=False):
    if not is_silent_enabled:
        print(f"Logging is enabled in log file: {log_filename}")
        print(f"Log started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def print_stop_logs(log_filename, is_silent_enabled=False):
    if not is_silent_enabled:
        print(f"Log ended at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Logging is disabled in log file: {log_filename}")

def print_end_process(is_silent_enabled=False):
    if not is_silent_enabled:
        print("Processing completed.")
        print_line()

def print_cleanup_files(path, count_files, delete_directory=False, is_silent_enabled=False):
    if not is_silent_enabled:
        if delete_directory:
            print(f"Remove files {count_files} and directory {path}")
        else:
            print(f"Remove files {count_files} in directory {path}")

def log_create(log_filename, is_logging_enabled=False):
    if is_logging_enabled:
        with open(log_filename, 'w', encoding='utf-8') as log_file:
            log_file.write("")

def log_line(log_filename, is_logging_enabled=False):
    if is_logging_enabled:
        with open(log_filename, 'a', encoding='utf-8') as log_file:
            log_file.write("--------------------------------------------------------------------\n")

def log_app_title(log_filename, app_name, app_author, is_logging_enabled=False):
    if is_logging_enabled:
        with open(log_filename, 'a', encoding='utf-8') as log_file:
            log_file.write(f"{app_name}\n")
            log_file.write(f"{app_author}\n")
        log_line(log_filename, is_logging_enabled)

def log_messages(log_filename, messages, is_logging_enabled=False):
    if is_logging_enabled:
        with open(log_filename, 'a', encoding='utf-8') as log_file:
            for message in messages:
                log_file.write(f"{message}\n")

def log_start_logs(log_filename, is_logging_enabled=False):
    if is_logging_enabled:
        with open(log_filename, 'a', encoding='utf-8') as log_file:
            log_file.write(f"Logging is enabled in log file: {log_filename}\n")
            log_file.write(f"Log started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

def log_stop_logs(log_filename, is_logging_enabled=False):
    if is_logging_enabled:
        with open(log_filename, 'a', encoding='utf-8') as log_file:
            log_file.write(f"Log ended at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            log_file.write(f"Logging is disabled in log file: {log_filename}\n")

def log_cleanup_files(log_filename, path, count_files, delete_directory=False, is_logging_enabled=False):
    if is_logging_enabled:
        with open(log_filename, 'a', encoding='utf-8') as log_file:
            if delete_directory:
                log_file.write(f"Remove files {count_files} and directory {path}\n")
            else:
                log_file.write(f"Remove files {count_files} in directory {path}\n")

def log_end_process(log_filename, is_logging_enabled=False):
    if is_logging_enabled:
        with open(log_filename, 'a', encoding='utf-8') as log_file:
            log_file.write("Processing completed.\n")
    log_line(log_filename, is_logging_enabled)

def az_create_filename(filename, path=".\\temp\\", prefix_filename="temp", fileextension=".json"):
    str_timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    return f"{path}{prefix_filename}_{filename}_{str_timestamp}{fileextension}"

def az_download_url_to_filename(url, output_filename):
    result = ""

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(response.text)

        result = f"OK: Downloaded {len(response.content)} bytes from \"{url}\" to \"{output_filename}\" file."
    except requests.exceptions.RequestException as e:
        result = f"ERR-URL: Download from {url} to {output_filename} failed: {e}"
    except IOError as e:
        result = f"ERR-FILE: Create file {output_filename} failed: {e}"

    return result

def az_create_directory(path=".\\temp\\", if_exists_delete=False):
    result = ""
    
    try:
        if not os.path.exists(path):
            os.makedirs(path)
            result = f"OK: Created directory {path} and is ready."
        else:
            if if_exists_delete:
                shutil.rmtree(path)
                os.makedirs(path)
                result = f"OK: Removed and recreated directory {path} and is ready."
            else:
                result = f"OK: Directory {path} exist and is ready."
    except Exception as e:
        result = f"ERR-DIR: Unable to create directory {path}: {e}"
    return result

def az_delete_directory(path=".\\temp\\", files_to_delete=None, if_exists_delete_directory=False, enable_logging=False):
    logs = []

    for file in files_to_delete:
        file_name = files_to_delete[file]
        try:
            if os.path.exists(file_name):
                os.remove(file_name)
                result = f"OK: Deleted file: {file_name}"
            else:
                result = f"ERR-FILE: File not found, cannot delete: {file_name}"
        except Exception as e:
            result = f"ERR-FILE: Error deleting file {file_name}: {e}"
        if enable_logging:
            logs.append(result)

    try:
        if if_exists_delete_directory and os.path.exists(path):
            shutil.rmtree(path)
            result = f"OK: Removed directory {path}."
        else:
            result = f"OK: The {path} directory still exists."
    except Exception as e:
        result = f"ERR-DIR: Error deleting directory {path}: {e}"
    if enable_logging:
        logs.append(result) 

    return logs