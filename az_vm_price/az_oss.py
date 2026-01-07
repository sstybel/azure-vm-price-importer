import json

def az_list_oss(filename_oss="azure_oss", enable_silent=False, enable_logging=False):
    logs = []
    oss = {}

    os = ['linux', 'windows']

    try:
        with open(filename_oss, 'r', encoding='utf-8') as file:
            data_oss = json.load(file)
            for ossys in os:
                az_oss_list = data_oss[ossys]
                for az_os in az_oss_list:
                    dict_os = {az_os: az_oss_list[az_os]}
                    oss.update(dict_os)
            if not enable_silent:
                print(f"Loaded {len(oss)} OSs from file {filename_oss}.")
            if enable_logging:
                logs.append(f"OK: Loaded {len(oss)} OSs from file {filename_oss}.") 
    except Exception as e:
        if not enable_silent:
            print(f"Unable to read OSs from file {filename_oss}: {e}")
        if enable_logging:
            logs.append(f"ERR-FILE: Unable to read OSs from file {filename_oss}: {e}")
    
    return logs, oss

def az_list_vm_series(filename_oss="azure_oss", enable_silent=False, enable_logging=False):
    logs = []
    series = {}

    try:
        with open(filename_oss, 'r', encoding='utf-8') as file:
            data_oss = json.load(file)
            series_list = data_oss['series']
            for az_series in series_list:
                dict_series = {az_series: series_list[az_series]}
                series.update(dict_series)
            if not enable_silent:
                print(f"Loaded {len(series)} VMs series from file {filename_oss}.")
            if enable_logging:
                logs.append(f"OK: Loaded {len(series)} VMs series from file {filename_oss}.") 
    except Exception as e:
        if not enable_silent:
            print(f"Unable to read VMs series from file {filename_oss}: {e}")
        if enable_logging:
            logs.append(f"ERR-FILE: Unable to read VMs series from file {filename_oss}: {e}")
    
    return logs, series
