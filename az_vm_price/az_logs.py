from datetime import datetime

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

def log_end_process(time_process, log_filename, is_logging_enabled=False):
    if is_logging_enabled:
        with open(log_filename, 'a', encoding='utf-8') as log_file:
            if time_process.total_seconds() > 0:
                log_file.write(f"Total processing time: {time_process}\n")
            log_file.write("Processing completed.\n")
    log_line(log_filename, is_logging_enabled)
