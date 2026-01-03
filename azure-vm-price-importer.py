import os
import json
import argparse
import requests
from datetime import datetime

str_version = "1.00"
str_app_name ="Azure VM Prices Importer - ver. " + str_version
str_author = "Copyright (c) 2025 - 2026 by Sebastian Stybel, www.BONO.Edu.PL"

url_currencies = "https://azure.microsoft.com/api/v2/currencies/"
url_regions = "https://azure.microsoft.com/api/v2/pricing/calculator/regions/"
url_resources = "https://azure.microsoft.com/api/v3/pricing/virtual-machines/page/resources/"
url_oss = "https://azure.microsoft.com/api/v3/pricing/virtual-machines/page/dropdowns/"
url_sku_details = "https://azure.microsoft.com/api/v3/pricing/virtual-machines/page/details/" # url_sku_details + "{os}/"
url_sku_region = "https://azure.microsoft.com/api/v3/pricing/virtual-machines/page/" # url_sku_region + "{os}/" + "{region}/"

file_currencies = "azure_currencies"
file_regions = "azure_regions" 
file_resources = "azure_resources"
file_oss = "azure_oss"
file_sku_details = "azure_sku_details" # file_sku_details + "_{os}"
file_sku_region = "azure_sku_region" # file_sku_region + "_{os}_{region}"

filename_currencies = ""
filename_regions = "" 
filename_resources = ""
filename_oss = ""
filename_sku_details = []
filename_sku_region = []

def temp_file_name(filename, prefix_filename="temp", fileextension=".json"):
    str_timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    return f"{prefix_filename}_{filename}_{str_timestamp}{fileextension}"

def download_url_to_file(url, output_file):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(response.text)

        result = f"OK: Downloaded {len(response.content)} bytes from \"{url}\" to \"{output_file}\" file."
    except requests.exceptions.RequestException as e:
        result = f"ERR-URL: {e}"
    except IOError as e:
        result = f"ERR-FILE: {e}"

    return result

def download_azure_data():
    global filename_currencies, filename_regions, filename_resources, filename_oss, filename_sku_details, filename_sku_region

    results = []

    filename_currencies = temp_file_name(file_currencies)
    filename_regions = temp_file_name(file_regions)
    filename_resources = temp_file_name(file_resources)
    filename_oss = temp_file_name(file_oss)

    results.append(download_url_to_file(url_currencies, filename_currencies))
    results.append(download_url_to_file(url_regions, filename_regions))
    results.append(download_url_to_file(url_resources, filename_resources))
    results.append(download_url_to_file(url_oss, filename_oss))
    
    return results

def delete_azure_data():
    results = []

    files_to_delete = [
        filename_currencies,
        filename_regions,
        filename_resources,
        filename_oss
    ] + filename_sku_details + filename_sku_region

    for file in files_to_delete:
        try:
            if os.path.exists(file):
                os.remove(file)
                results.append(f"OK: Deleted file: {file}")
            else:
                results.append(f"ERR-FILE: File not found, cannot delete: {file}")
        except Exception as e:
            results.append(f"ERR-FILE: Error deleting file {file}: {e}")

    return results

if __name__ == "__main__":
    results = download_azure_data()
    for result in results:
        print(result)

    results = delete_azure_data()
    for result in results:
        print(result)
