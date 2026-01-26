import os
import json
import zipfile
from alive_progress import alive_bar

def az_save_config_pack(path=".\\temp\\", az_region="all", initial_data=None, detail_price_data=None, regions_prices_data=None, calculator_price_data=None, enable_silent=False, enable_logging=True):
    logs = []
    config_pack = {}

    path_relativ = ("\\".join(path.split("\\")[:-2])).strip() + "\\"
    conf_filename = f"{path}az_config_pack.json"

    pack_struct = {
        "region": az_region,
        "initial_data": initial_data,
        "detail_price_data": detail_price_data,
        "regions_prices_data": regions_prices_data,
        "calculator_price_data": calculator_price_data
    }

    try:
        with open(conf_filename, 'w', encoding='utf-8') as json_file:
            json.dump(pack_struct, json_file, indent=4)
            if not enable_silent:
                print(f"Configuration package created and saved to JSON file: {conf_filename}")
            result = f"Configuration package created and saved to JSON file: {conf_filename}"
            config_pack = {"config_pack": conf_filename}
    except Exception as e:
        result = f"ERR-FILE: Error create and saved to JSON file {conf_filename}: {e}"
    if enable_logging:
        logs.append(result)
    
    pack_filename = "\\".join(path.split("\\")[0:-2]) + "\\" + path.split("\\")[-2].strip() + ".azpx"
    try:
        with zipfile.ZipFile(pack_filename, 'w', zipfile.ZIP_DEFLATED) as zip_pack:
            if not enable_silent:
                print(f"Create Azure prices pack file {pack_filename}")
            if enable_logging:
                logs.append(f"Create Azure prices pack file {pack_filename}")
            for root, dirs, files in os.walk(path):
                max_progress = len(files)
                with alive_bar(max_progress, title="Packing", disable=enable_silent) as bar:
                    for file in files:
                        if enable_logging:
                            logs.append(f"OK: Add file {file} to Azure prices pack file {pack_filename}")
                        bar_item = f"{file}"
                        if not enable_silent:
                            bar.text = bar_item
                        zip_pack.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(path, '..')))
                        if not enable_silent:
                            bar()
            if not enable_silent:
                print(f"Created Azure prices pack file {pack_filename} with {max_progress} files packed.")
            if enable_logging:
                logs.append(f"Created Azure prices pack file {pack_filename} with {max_progress} files packed.")
    except Exception as e:
        if enable_logging:
            logs.append(f"ERR-PACK: Error create Azure prices pack file {pack_filename}: {e}")

    return logs, config_pack

def az_load_config_pack(path=".\\temp\\", pack_filename=".\\az_price_data.azpx", enable_silent=False, enable_logging=False):
    logs = []
    
    conf_file = "az_config_pack.json"
    conf_filename = ""
    path_data = ""

    az_region = ""
    initial_data = {}
    detail_price_data = {}
    regions_prices_data = {}
    calculator_price_data = {}

    try:
        with zipfile.ZipFile(pack_filename, 'r') as zip_unpack:
            list_pack_files = zip_unpack.namelist()
            max_progress = len(list_pack_files)
            with alive_bar(max_progress, title="Unpacking", disable=enable_silent) as bar:
                for unpack_file in list_pack_files:
                    unpack_filename = unpack_file.replace("/", '\\')
                    if enable_logging:
                        logs.append(f"OK: Unpack file {unpack_filename} from Azure prices pack file {pack_filename}")
                    unpack_filename = unpack_filename.split("\\")[-1].strip()
                    if unpack_filename == conf_file:
                        conf_filename = path + unpack_file.replace("/", "\\")
                    bar_item = f"{unpack_filename}"
                    if not enable_silent:
                        bar.text = bar_item
                    zip_unpack.extract(unpack_file, path)
                    if not enable_silent:
                        bar()
            if not enable_silent:
                print(f"Unpack Azure prices from pack file {pack_filename} with {max_progress} files packed.")
            if enable_logging:
                logs.append(f"Unpack Azure from prices pack file {pack_filename} with {max_progress} files packed.")
    except Exception as e:
        if enable_logging:
            logs.append(f"ERR-PACK: Error unpack Azure prices from pack file {pack_filename}: {e}")

    try:
        with open(conf_filename, 'r', encoding='utf-8') as file:
            data_conf_file = json.load(file)
            path_data = os.path.dirname(conf_filename) + "\\"
            az_region = data_conf_file['region']
            initial_data = data_conf_file['initial_data']
            detail_price_data = data_conf_file['detail_price_data']
            regions_prices_data = data_conf_file['regions_prices_data']
            calculator_price_data = data_conf_file['calculator_price_data']
            config_pack = {"config_pack": conf_filename}
            if not enable_silent:
                print(f"Load data from configuration package JSON file {conf_filename}")
            if enable_logging:
                logs.append(f"Load data from configuration package JSON file {conf_filename}")
    except Exception as e:
        if not enable_silent:
            print(f"Unable to read configuration package from JSON file {conf_filename}: {e}")
        if enable_logging:
            logs.append(f"ERR-FILE: Unable to read configuration package from JSON file {conf_filename}: {e}")

    return logs, path_data, az_region, initial_data, detail_price_data, regions_prices_data, calculator_price_data, config_pack
