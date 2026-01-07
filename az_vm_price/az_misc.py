import os
import shutil
import requests
from datetime import datetime

def az_create_filename(filename, path=".\\temp\\", prefix_filename="temp", fileextension=".json"):
    str_timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    return f"{path}{prefix_filename}_{filename}_{str_timestamp}{fileextension}"

def az_create_pathname(pathame, path=".\\"):
    str_timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    return f"{path}{pathame}_{str_timestamp}\\"

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