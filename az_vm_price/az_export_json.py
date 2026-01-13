import json

from az_vm_price import az_misc

def az_export_prices_list_to_json(json_output_filename, prices_list={}, is_silent_enabled=False, is_logging_enabled=True):
    logs = []
    
    try:
        with open(json_output_filename, 'w', encoding='utf-8') as json_file:
            json.dump(prices_list, json_file, ensure_ascii=False, indent=4)
        result_export = f"OK: Exported Azure VM prices to JSON file {json_output_filename}"
        if not is_silent_enabled:
            print(f"Exported Azure VM prices to JSON file: {json_output_filename}")
    except Exception as e:
        if not is_silent_enabled:
            print(f"Unable to export Azure VM prices to JSON file {json_output_filename}: {e}")
        result_export = f"ERR-FILE: Unable to export Azure VM prices to JSON file {json_output_filename}: {e}"
    if is_logging_enabled:
        logs.append(result_export)

    return logs

def az_import_prices_list_from_json(json_input_filename, is_silent_enabled=False, is_logging_enabled=True):
    logs = []
    prices_list = {}
    
    try:
        with open(json_input_filename, 'r', encoding='utf-8') as json_file:
            prices_list = json.load(json_file)
            count_prices = len(prices_list['prices_list'])
            count_currencies = len(prices_list['currencies_list'])
            region_prices = prices_list['region']
        result_import = f"OK: Imported Azure VM prices list count {count_prices} and currencies count {count_currencies} from JSON file {json_input_filename} for region {region_prices}"
        if not is_silent_enabled:
            print(f"Imported Azure VM prices list count {count_prices} and currencies count {count_currencies} from JSON file: {json_input_filename}")
    except Exception as e:
        if not is_silent_enabled:
            print(f"Unable to import Azure VM prices from JSON file {json_input_filename}: {e}")
        result_import = f"ERR-FILE: Unable to import Azure VM prices from JSON file {json_input_filename}: {e}"
    if is_logging_enabled:
        logs.append(result_import)

    return logs, prices_list
