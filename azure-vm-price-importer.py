import argparse

from az_vm_price import az_oss
from az_vm_price import az_regions
from az_vm_price import az_download
from az_vm_price import az_pack
from az_vm_price import az_infos
from az_vm_price import az_logs
from az_vm_price import az_misc

str_version = "1.00"
str_app_name ="Azure VM Prices Importer - ver. " + str_version
str_author = "Copyright (c) 2025 - 2026 by Sebastian Stybel, www.BONO.Edu.PL"

pathname = "az_price_data"
path = ".\\"

file_currencies = "azure_currencies"
file_regions = "azure_regions" 
file_resources = "azure_resources"
file_oss = "azure_oss"
file_sku_details = "azure_sku_details" # file_sku_details + "_{os}"
file_sku_calculator = "azure_sku_calculator" # file_sku_calculator + "_{region}"
file_sku_region = "azure_sku_region" # file_sku_region + "_{os}_{region}"

azure_oss = {}
azure_regions = {}
azure_vm_series = {}
azure_initial_data = {}
azure_detail_price_data = {}
azure_regions_prices_data = {}
azure_calculator_price_data = {}

is_delete_files_enabled = True
is_delete_directory_enabled = True
is_logging_enabled = True
is_silent_enabled = False
is_load_pack = True
is_save_pack = True

azure_prices_of_region = "poland-central"
#azure_prices_of_region = "all"

log_filename = ".\\azure_vm_price_importer.log"

azpx_input_filename = ".\\az_price_data_20260107111512.azpx"
azpx_input_filename = ".\\az_price_data_20260107122903.azpx"

csv_output_filename = ".\\azure_vm_prices.csv"
xlsx_output_filename = ".\\azure_vm_prices.xlsx"
json_output_filename = ".\\azure_vm_prices.json"

if __name__ == "__main__":
    path = az_misc.az_create_pathname(pathname, path=path)

    az_logs.log_create(log_filename, is_logging_enabled)
    az_infos.print_app_title(str_app_name, str_author, is_silent_enabled)
    az_logs.log_app_title(log_filename, str_app_name, str_author, is_logging_enabled)
    az_infos.print_start_logs(log_filename, is_silent_enabled)
    az_logs.log_start_logs(log_filename, is_logging_enabled)

    if not is_load_pack:
        logs, azure_initial_data = az_download.az_download_initial_data(path=path, file_currencies=file_currencies, file_regions=file_regions, file_resources=file_resources, file_oss=file_oss, enable_silent=is_silent_enabled, enable_logging=is_logging_enabled)
        az_logs.log_messages(log_filename, logs, is_logging_enabled)
    else:
        logs, path, azure_prices_of_region, azure_initial_data, azure_detail_price_data, azure_regions_prices_data, azure_calculator_price_data, azure_config_pack = az_pack.az_load_config_pack(path=".\\", pack_filename=azpx_input_filename, enable_silent=is_silent_enabled, enable_logging=is_logging_enabled)
        az_logs.log_messages(log_filename, logs, is_logging_enabled)        

    logs, azure_oss = az_oss.az_list_oss(azure_initial_data['oss'], is_silent_enabled, is_logging_enabled)
    az_logs.log_messages(log_filename, logs, is_logging_enabled)
    
    logs, azure_vm_series = az_oss.az_list_vm_series(azure_initial_data['oss'], is_silent_enabled, is_logging_enabled)
    az_logs.log_messages(log_filename, logs, is_logging_enabled)

    logs, azure_regions = az_regions.az_list_regions(azure_initial_data['regions'], is_silent_enabled, is_logging_enabled)
    az_logs.log_messages(log_filename, logs, is_logging_enabled)

    if not is_load_pack:
        logs, azure_detail_price_data, azure_regions_prices_data = az_download.az_download_regions_prices_data(path=path, file_sku_details=file_sku_details, file_sku_region=file_sku_region, az_region=azure_prices_of_region, az_oss=azure_oss, az_regions=azure_regions, enable_silent=is_silent_enabled, enable_logging=is_logging_enabled)
        az_logs.log_messages(log_filename, logs, is_logging_enabled)

    if not is_load_pack:
        logs, azure_calculator_price_data = az_download.az_download_calculator_prices_data(path=path, file_sku_calculator=file_sku_calculator, az_region=azure_prices_of_region, az_regions=azure_regions, enable_silent=is_silent_enabled, enable_logging=is_logging_enabled)
        az_logs.log_messages(log_filename, logs, is_logging_enabled)

    if not is_load_pack and is_save_pack:
        logs, azure_config_pack = az_pack.az_save_config_pack(path=path, az_region=azure_prices_of_region, initial_data=azure_initial_data, detail_price_data=azure_detail_price_data, regions_prices_data=azure_regions_prices_data, calculator_price_data=azure_calculator_price_data, enable_silent=is_silent_enabled, enable_logging=is_logging_enabled)
        az_logs.log_messages(log_filename, logs, is_logging_enabled)

    if is_delete_files_enabled:
        files_to_delete = azure_initial_data | azure_detail_price_data | azure_regions_prices_data | azure_calculator_price_data | azure_config_pack
        logs = az_misc.az_delete_directory(path, files_to_delete, is_delete_directory_enabled, is_logging_enabled)
        az_infos.print_cleanup_files(path=path, count_files=len(files_to_delete), delete_directory=is_delete_directory_enabled, is_silent_enabled=is_silent_enabled)
        az_logs.log_cleanup_files(log_filename, path=path, count_files=len(files_to_delete), delete_directory=is_delete_directory_enabled, is_logging_enabled=is_logging_enabled)
        az_logs.log_messages(log_filename, logs, is_logging_enabled)

    az_infos.print_stop_logs(log_filename, is_silent_enabled)
    az_logs.log_stop_logs(log_filename, is_logging_enabled) 

    az_infos.print_end_process(is_silent_enabled)
    az_logs.log_end_process(log_filename, is_logging_enabled)

'''''
    is_created = create_temp_directory()
    print(f"Creating temporary directory: {path_temp}\n")
    with open(log_filename, 'a', encoding='utf-8') as log_file:
        log_file.write(f"Creating temporary directory: {path_temp}\n\n")
        log_file.write(f"{is_created}\n")

    if is_created.startswith("OK"):
        results = download_azure_data()
        if is_logging_enabled:
            with open(log_filename, 'a', encoding='utf-8') as log_file:
                for result in results:
                    log_file.write(result + "\n")

        results, result_data = create_azure_prices_list()
        if is_logging_enabled:
            with open(log_filename, 'a', encoding='utf-8') as log_file:
                for result in results:
                    log_file.write(result + "\n")
        with open(json_output_filename, 'w', encoding='utf-8') as json_file:
            json.dump(result_data, json_file, indent=4)
            print(f"JSON file created: {json_output_filename}\n")
        if is_logging_enabled:
            with open(log_filename, 'a', encoding='utf-8') as log_file:
                log_file.write(f"JSON file created: {json_output_filename}\n\n")


'''
