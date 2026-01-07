from datetime import datetime
from alive_progress import alive_bar

from az_vm_price import az_oss
from az_vm_price import az_regions
from az_vm_price import az_misc

url_currencies = "https://azure.microsoft.com/api/v2/currencies/"
url_regions = "https://azure.microsoft.com/api/v2/pricing/calculator/regions/"
url_resources = "https://azure.microsoft.com/api/v3/pricing/virtual-machines/page/resources/"
url_oss = "https://azure.microsoft.com/api/v3/pricing/virtual-machines/page/dropdowns/"
url_sku_details = "https://azure.microsoft.com/api/v3/pricing/virtual-machines/page/details/" # url_sku_details + "{os}/"
url_sku_calculator = "https://azure.microsoft.com/api/v4/pricing/virtual-machines/calculator/" # url_sku_calculator+ "{region}/"
url_sku_region = "https://azure.microsoft.com/api/v3/pricing/virtual-machines/page/" # url_sku_region + "{os}/" + "{region}/"

def az_download_initial_data(path=".\\temp\\", file_currencies="azure_currencies", file_regions="azure_regions", file_resources="azure_resources", file_oss="azure_oss", enable_silent=False, enable_logging=False):
    logs = []
    results = {}

    start_download = datetime.now()

    result = az_misc.az_create_directory(path=path)
    if enable_logging:
        logs.append(result)

    if result.startswith("OK"):
        i = 0

        if not enable_silent:
            dir_info = result.split(":")[1].strip()
            print(f"{dir_info}")
        
        with alive_bar(4, title="Downloading", disable=enable_silent) as bar:
            filename_currencies = az_misc.az_create_filename(file_currencies, path=path, prefix_filename="az", fileextension=".json")
            bar_item = f"{filename_currencies}"
            bar_item = bar_item[len(path):]
            if not enable_silent:
                bar.text = bar_item
            result_download = az_misc.az_download_url_to_filename(url_currencies, filename_currencies)
            if result_download.startswith("ERR"):
                if not enable_silent:
                    print(f"Error downloading: {filename_currencies}")
            else:
                if not enable_silent:
                    print(f"Downloaded: {filename_currencies}")
                results.update({"currencies": filename_currencies})
                i += 1
            if enable_logging:
                logs.append(result_download)
            if not enable_silent:
                bar()

            filename_resources = az_misc.az_create_filename(file_resources, path=path, prefix_filename="az", fileextension=".json")
            bar_item = f"{filename_resources}"
            bar_item = bar_item[len(path):]
            if not enable_silent:
                bar.text = bar_item
            result_download = az_misc.az_download_url_to_filename(url_resources, filename_resources)
            if result_download.startswith("ERR"):
                if not enable_silent:
                    print(f"Error downloading: {filename_resources}")
            else:
                if not enable_silent:
                    print(f"Downloaded: {filename_resources}")
                results.update({"resources": filename_resources})
                i += 1
            if enable_logging:
                logs.append(result_download)
            if not enable_silent:
                bar()

            filename_regions = az_misc.az_create_filename(file_regions, path=path, prefix_filename="az", fileextension=".json")
            bar_item = f"{filename_regions}"
            bar_item = bar_item[len(path):]
            if not enable_silent:
                bar.text = bar_item
            result_download = az_misc.az_download_url_to_filename(url_regions, filename_regions)
            if result_download.startswith("ERR"):
                if not enable_silent:
                    print(f"Error downloading: {filename_regions}")
            else:
                if not enable_silent:
                    print(f"Downloaded: {filename_regions}")
                results.update({"regions": filename_regions})
                i += 1
            if enable_logging:
                logs.append(result_download)
            if not enable_silent:
                bar()

            filename_oss = az_misc.az_create_filename(file_oss, path=path, prefix_filename="az", fileextension=".json")
            bar_item = f"{filename_oss}"
            bar_item = bar_item[len(path):]
            if not enable_silent:
                bar.text = bar_item
            result_download = az_misc.az_download_url_to_filename(url_oss, filename_oss)
            if result_download.startswith("ERR"):
                if not enable_silent:
                    print(f"Error downloading: {filename_oss}")
            else:
                if not enable_silent:
                    print(f"Downloaded: {filename_oss}")
                results.update({"oss": filename_oss})
                i += 1
            if enable_logging:
                logs.append(result_download)
            if not enable_silent:
                bar()
        
        end_download = datetime.now()
        
        delta_download = end_download - start_download  

        if not enable_silent:
            print(f"Download summary")
            print(f"Count files downloaded: {i}")
            print(f"Elapsed: {bar.elapsed}")
            print(f"Throughput: {bar.rate}")
        if enable_logging:
            logs.append("Download summary")
            logs.append(f"Count files downloaded: {i}")
            logs.append(f"Elapsed: {bar.elapsed}")
            logs.append(f"Throughput: {bar.rate}")

        if not enable_silent:
            print(f"Total download time: {delta_download}")
        if enable_logging:
            logs.append(f"Total download time: {delta_download}")

    return logs, results

def az_download_regions_prices_data(path=".\\temp\\", file_sku_details="azure_sku_details", file_sku_region="azure_sku_region", az_region="all", az_oss=None, az_regions=None, enable_silent=False, enable_logging=False):
    logs = []
    results_sku_details = {}
    results_sku_region = {}

    start_download = datetime.now()

    result = az_misc.az_create_directory(path=path)
    if enable_logging:
        logs.append(result)

    if result.startswith("OK"):
        i = 0

        if not enable_silent:
            dir_info = result.split(":")[1].strip()
            print(f"{dir_info}")

        if az_region == "" or az_region == "all":
            max_bar = len(az_oss) + (len(az_oss) * len(az_regions))
        else:
            max_bar = len(az_oss) + (len(az_oss) * 1)

        i = 0
        j = 0

        with alive_bar(max_bar, title="Downloading", disable=enable_silent) as bar:
            for az_os in az_oss:
                sku_details_file = az_misc.az_create_filename(file_sku_details + f"_{az_os}", path=path, prefix_filename="az", fileextension=".json")
                sku_details_url = url_sku_details + f"{az_os}/"
                bar_item = f"{sku_details_file}"
                bar_item = bar_item[len(path):]
                if not enable_silent:
                    bar.text = bar_item
                result_download = az_misc.az_download_url_to_filename(sku_details_url, sku_details_file)
                if result_download.startswith("ERR"):
                    if not enable_silent:
                        print(f"Error downloading: {sku_details_file}")
                else:
                    if not enable_silent:
                        print(f"Downloaded: {sku_details_file}")
                    results_sku_details.update({f"sku_details_{az_os}": sku_details_file})
                    i += 1
                if enable_logging:
                    logs.append(result_download)
                if not enable_silent:
                    bar()

                for az_region_name in az_regions:
                    if az_region != "" and az_region != "all":
                        if az_region_name != az_region:
                            continue
                    sku_region_file = az_misc.az_create_filename(file_sku_region + f"_{az_os}_{az_region_name}", path=path, prefix_filename="az", fileextension=".json")
                    sku_region_url = url_sku_region + f"{az_os}/{az_region_name}/"
                    bar_item = f"{sku_region_file}"
                    bar_item = bar_item[len(path):]
                    if not enable_silent:
                        bar.text = bar_item
                    result_download = az_misc.az_download_url_to_filename(sku_region_url, sku_region_file)
                    if result_download.startswith("ERR"):
                        if not enable_silent:
                            print(f"Error downloading: {sku_region_file}")
                    else:
                        if not enable_silent:
                            print(f"Downloaded: {sku_region_file}")
                        results_sku_region.update({f"sku_region_{az_os}_{az_region_name}": sku_region_file})
                        j += 1
                    if enable_logging:
                        logs.append(result_download)
                    if not enable_silent:
                        bar()

        k = i + j

        end_download = datetime.now()
        
        delta_download = end_download - start_download  

        if not enable_silent:
            print(f"Download summary")
            print(f"Count files downloaded: {k}")
            print(f"Elapsed: {bar.elapsed}")
            print(f"Throughput: {bar.rate}")
        if enable_logging:
            logs.append("Download summary")
            logs.append(f"Count files downloaded: {k}")
            logs.append(f"Elapsed: {bar.elapsed}")
            logs.append(f"Throughput: {bar.rate}")

        if not enable_silent:
            print(f"Total download time: {delta_download}")
        if enable_logging:
            logs.append(f"Total download time: {delta_download}")

    return logs, results_sku_details, results_sku_region

def az_download_calculator_prices_data(path=".\\temp\\", file_sku_calculator="azure_sku_calculator", az_region="all", az_regions=None, enable_silent=False, enable_logging=False):
    logs = []
    results_sku_calculator = {}

    start_download = datetime.now()

    result = az_misc.az_create_directory(path=path)
    if enable_logging:
        logs.append(result)

    if result.startswith("OK"):
        i = 0

        if not enable_silent:
            dir_info = result.split(":")[1].strip()
            print(f"{dir_info}")

        if az_region == "" or az_region == "all":
            max_bar = len(az_regions)
        else:
            max_bar = 1

        i = 0

        with alive_bar(max_bar, title="Downloading", disable=enable_silent) as bar:
            for az_region_name in az_regions:
                if az_region != "" and az_region != "all":
                    if az_region_name != az_region:
                        continue
                sku_calculator_file = az_misc.az_create_filename(file_sku_calculator + f"_{az_region_name}", path=path, prefix_filename="az", fileextension=".json")
                sku_calculator_url = url_sku_calculator + f"{az_region_name}/"
                bar_item = f"{sku_calculator_file}"
                bar_item = bar_item[len(path):]
                if not enable_silent:
                    bar.text = bar_item
                result_download = az_misc.az_download_url_to_filename(sku_calculator_url, sku_calculator_file)
                if result_download.startswith("ERR"):
                    if not enable_silent:
                        print(f"Error downloading: {sku_calculator_file}")
                else:
                    if not enable_silent:
                        print(f"Downloaded: {sku_calculator_file}")
                    results_sku_calculator.update({f"sku_calculator_{az_region_name}": sku_calculator_file})
                    i += 1
                if enable_logging:
                    logs.append(result_download)
                if not enable_silent:
                    bar()

        end_download = datetime.now()
    
        delta_download = end_download - start_download  

        if not enable_silent:
            print(f"Download summary")
            print(f"Count files downloaded: {i}")
            print(f"Elapsed: {bar.elapsed}")
            print(f"Throughput: {bar.rate}")
        if enable_logging:
            logs.append("Download summary")
            logs.append(f"Count files downloaded: {i}")
            logs.append(f"Elapsed: {bar.elapsed}")
            logs.append(f"Throughput: {bar.rate}")

        if not enable_silent:
            print(f"Total download time: {delta_download}")
        if enable_logging:
            logs.append(f"Total download time: {delta_download}")

    return logs, results_sku_calculator
