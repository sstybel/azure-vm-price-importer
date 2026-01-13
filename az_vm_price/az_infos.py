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

def print_end_process(time_process, is_silent_enabled=False):
    if not is_silent_enabled:
        if time_process.total_seconds() > 0:
            print(f"Total processing time: {time_process}")
        print("Processing completed.")
        print_line()

def print_cleanup_files(path, count_files, delete_directory=False, is_silent_enabled=False):
    if not is_silent_enabled:
        if delete_directory:
            print(f"Remove files {count_files} and directory {path}")
        else:
            print(f"Remove files {count_files} in directory {path}")
