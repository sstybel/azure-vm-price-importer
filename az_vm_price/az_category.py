import json

def az_list_categories(filename_metadata="azure_metadata", enable_silent=False, enable_logging=False):
    logs = []
    categories = {}

    try:
        with open(filename_metadata, 'r', encoding='utf-8') as file:
            data_metadata = json.load(file)
            categories_list = data_metadata['dropdown']
            for az_category in categories_list:
                str_name = az_category['slug'].lower()
                str_fullname = "All"
                if 'displayName' in az_category:
                    str_fullname = az_category['displayName']
                for serie in az_category['series']:
                    str_serie_name = serie['slug'].lower()
                    str_serie_fullname = serie['displayName']
                    for instance in serie['instances']:
                        str_instance_name = instance['slug'].lower()
                        dict_category = {
                            "category": str_name,
                            "category_fullname": str_fullname,
                            "series": str_serie_name,
                            "series_fullname": str_serie_fullname,
                            "instance": str_instance_name,
                        }
                        categories.update({str_instance_name: dict_category})
            if not enable_silent:
                print(f"Loaded {len(categories)} categories from file {filename_metadata}.")
            if enable_logging:
                logs.append(f"OK: Loaded {len(categories)} categories from file {filename_metadata}.") 
    except Exception as e:
        if not enable_silent:
            print(f"Unable to read categories from file {filename_metadata}: {e}")
        if enable_logging:
            logs.append(f"ERR-FILE: Unable to read categories from file {filename_metadata}: {e}")
    
    return logs, categories