import json

from az_vm_price import az_geographical

def az_list_regions(filename_regions="azure_regions", enable_silent=False, enable_logging=False):
    logs = []
    regions = {}

    try:
        with open(filename_regions, 'r', encoding='utf-8') as file:
            data_regions = json.load(file)
            for az_countries in data_regions:
                country = az_countries['slug']
                country_name = az_countries['displayName']
                geographic = az_geographical.az_geographical_key_by_country(country)
                geographic_name = az_geographical.az_geographical_name_by_country(country)
                az_regions = az_countries['regions']
                for az_region in az_regions:
                    region = az_region['slug']
                    region_name = az_region['displayName']
                    dict_region_data = {
                        'region': region,
                        'region_name': region_name,
                        'country': country,
                        'country_name': country_name,
                        'geographic': geographic,
                        'geographic_name': geographic_name
                    }
                    dict_region = {region: dict_region_data} 
                    regions.update(dict_region)
            if not enable_silent:
                print(f"Loaded {len(regions)} regions from file {filename_regions}.")
            if enable_logging:
                logs.append(f"OK: Loaded {len(regions)} regions from file {filename_regions}.")
    except Exception as e:
        if not enable_silent:
            print(f"Unable to read regions from file {filename_regions}: {e}")
        if enable_logging:
            logs.append(f"ERR-FILE: Unable to read regions from file {filename_regions}: {e}")
    
    return logs, regions
