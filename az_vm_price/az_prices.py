import json
from datetime import datetime
from alive_progress import alive_bar

def az_currencies_list_for_region(filename_currencies_data="", is_silent_enabled=False, is_logging_enabled=True):
    logs = []
    result_currencies_list = {}

    try:
        with open(filename_currencies_data, 'r', encoding='utf-8') as file_currencies:
            currencies_data = json.load(file_currencies)
        result_currencies = f"OK: Processed currencies from file {filename_currencies_data}"
    except Exception as e:
        result_currencies = f"ERR-FILE: Unable to process currencies from file {filename_currencies_data}: {e}"
    if is_logging_enabled:
        logs.append(result_currencies)

    if not result_currencies.startswith("ERR"):
        if not is_silent_enabled:
            print(f"Processing {len(currencies_data)} currencies from file {filename_currencies_data}")
        if is_logging_enabled:
            logs.append(f"OK: Processing {len(currencies_data)} currencies from file {filename_currencies_data}")
        max_progress = len(currencies_data) 
        with alive_bar(max_progress, title=f"Processing currencies", disable=is_silent_enabled) as bar_currencies:
            for currency in currencies_data:
                str_currency = currency
                str_currency_name = currencies_data[currency]['name']
                str_currency_info = currencies_data[currency]['displayName']
                str_currency_symbol = currencies_data[currency]['glyph']
                num_conversion = 0.0
                if 'conversion' in currencies_data[currency]:
                    num_conversion = currencies_data[currency]['conversion']
                num_conversion_onprem = 0.0
                if 'onPremConversion' in currencies_data[currency]:
                    num_conversion_onprem = currencies_data[currency]['onPremConversion']
                num_conversion_modern = 0.0
                if 'modernConversion' in currencies_data[currency]:
                    num_conversion_modern = currencies_data[currency]['modernConversion']
                dict_currency_data = {
                    "name": str_currency_name,
                    "info": str_currency_info,
                    "symbol": str_currency_symbol,
                    "conversion": num_conversion,
                    "conversion_onprem": num_conversion_onprem,
                    "conversion_modern": num_conversion_modern
                }
                result_currencies_list.update({str_currency: dict_currency_data})
                if is_logging_enabled:
                    logs.append(f"OK: Processed currency {str_currency_name} ({str_currency_symbol}) - {str_currency_info}")
                bar_currencies.text = f"{str_currency_name} ({str_currency_symbol})"
                bar_currencies()

        if not is_silent_enabled:
            print(f"Processed currencies count: {len(result_currencies_list)}")
        if is_logging_enabled:
            logs.append(f"OK: Processed currencies count: {len(result_currencies_list)}")

    return logs, result_currencies_list

def az_prices_list_for_region(az_region="us-central", az_regions={}, initial_data={}, detail_price_data={}, regions_prices_data={}, calculator_price_data={}, is_silent_enabled=False, is_logging_enabled=True):
    logs = []
    result_prices_list_records = {}
    result_prices_list = {}

    start_price = datetime.now()

    i = 0
    j = 0
    i_detail_price_data = 0
    max_detail_price_data = len(detail_price_data)
    if is_logging_enabled:
        logs.append(f"OK: Processed SKU details count: {max_detail_price_data}")
    for sku_detail_file in detail_price_data:
        filename_sku_details = detail_price_data[sku_detail_file]
        i_detail_price_data += 1
        item_bar = sku_detail_file
        item_bar = item_bar.split("_")[-1]
        item_bar = f"OS: {item_bar}"
        try:
            with open(filename_sku_details, 'r', encoding='utf-8') as file_sku_detail:
                data_sku_detail = json.load(file_sku_detail)
            result_sku_detail = f"OK: Processed SKU details from {filename_sku_details}"
        except Exception as e:
            result_sku_detail = f"ERR-FILE: Unable to process SKU details from file {filename_sku_details}: {e}"
        if is_logging_enabled:
            logs.append(result_sku_detail)

        if result_sku_detail.startswith("ERR"):
            continue

        sku_detail = data_sku_detail['attributesByOffer']
        max_progress_sku_detail = len(sku_detail)
        max_progress = max_progress_sku_detail
        if is_logging_enabled:
            logs.append(f"OK: Processed SKU detail count {max_detail_price_data} from file {filename_sku_details}")
        with alive_bar(max_progress, title=f"Processed SKU detail {i_detail_price_data}/{max_detail_price_data}", disable=is_silent_enabled) as bar_sku_detail:
            for detail in sku_detail:
                j += 1

                bool_price_available = False
                str_detail = detail
                bool_isbasevm = sku_detail[detail]['isBaseVm']
                bool_haspaygo = sku_detail[detail]['hasPayGo']
                bool_hasspot = sku_detail[detail]['hasSpot']
                
                if (not bool_isbasevm) and (not bool_haspaygo) and (not bool_hasspot):
                    if not is_silent_enabled:
                        bar_sku_detail.text = item_bar
                        bar_sku_detail()
                    if is_logging_enabled:
                        logs.append(f"OK-SKIP: I skip processed SKU {str_detail} as it is not a base VM and has no PayGo or Spot pricing.")
                    continue

                str_name = sku_detail[detail]['nameLocKey']
                str_series = sku_detail[detail]['series']
                str_instance_name = sku_detail[detail]['instanceName']
                str_tier = sku_detail[detail]['tier']
                str_os = sku_detail[detail]['type']
                str_category = sku_detail[detail]['category']
                num_cores = sku_detail[detail]['cores']
                num_ram = sku_detail[detail]['ram']
                num_disksize = 0
                if 'diskSize' in sku_detail[detail]:
                    num_disksize = sku_detail[detail]['diskSize']
                bool_isinpreview = sku_detail[detail]['isInPreview']
                bool_isvcpu = sku_detail[detail]['isVcpu']
                bool_isconstrainedcore = sku_detail[detail]['isConstrainedCore']

                if is_logging_enabled:
                    logs.append(f"OK: Processed SKU {str_detail} regions prices count {len(regions_prices_data)}")
                for sku_region_file in regions_prices_data:
                    arr_region = sku_region_file.split("_")
                    str_region = arr_region[-1]

                    if str_region != az_region:
                        if is_logging_enabled:
                            logs.append(f"OK-SKIP: I skip processed SKU {str_detail} regions prices for region {str_region} as it does not match the target region {az_region}.")
                        continue

                    filename_sku_region = regions_prices_data[sku_region_file]

                    try:
                        with open(filename_sku_region, 'r', encoding='utf-8') as file_sku_region:
                            data_sku_region = json.load(file_sku_region)
                        result_sku_region = f"OK: Processed SKU {str_detail} region {str_region} prices from {filename_sku_region}"
                    except Exception as e:
                        result_sku_region = f"ERR-FILE: Unable to process SKU {str_detail} regions {str_region} prices from file {filename_sku_region}: {e}"
                    if is_logging_enabled:
                        logs.append(result_sku_region)

                    if result_sku_region.startswith("ERR"):
                        continue

                    if str_detail in data_sku_region:
                        str_region_name = az_regions[str_region]['region_name']
                        str_country = az_regions[str_region]['country']
                        str_country_name = az_regions[str_region]['country_name']
                        str_geographic = az_regions[str_region]['geographic']
                        str_geographic_name = az_regions[str_region]['geographic_name']
                        num_cost_per_hour = 0.0
                        num_cost_per_hour_one_year_reserved = 0.0
                        num_cost_per_hour_three_year_reserved = 0.0
                        num_cost_per_hour_one_year_savings = 0.0
                        num_cost_per_hour_three_year_savings = 0.0
                        num_cost_per_hour_spot = 0.0
                        if len(data_sku_region[str_detail])>0:
                            bool_price_available = True
                            if 'perhour' in data_sku_region[str_detail]:
                                num_cost_per_hour = data_sku_region[str_detail]['perhour']
                            if 'perhouroneyearreserved' in data_sku_region[str_detail]:
                                num_cost_per_hour_one_year_reserved = data_sku_region[str_detail]["perhouroneyearreserved"]
                            if 'perhourthreeyearreserved' in data_sku_region[str_detail]:
                                num_cost_per_hour_three_year_reserved = data_sku_region[str_detail]["perhourthreeyearreserved"]
                            if 'perunitoneyearsavings' in data_sku_region[str_detail]:
                                num_cost_per_hour_one_year_savings = data_sku_region[str_detail]["perunitoneyearsavings"]
                            if 'perunitthreeyearsavings' in data_sku_region[str_detail]:
                                num_cost_per_hour_three_year_savings = data_sku_region[str_detail]["perunitthreeyearsavings"]
                            if 'perhourspot' in data_sku_region[str_detail]:
                                num_cost_per_hour_spot = data_sku_region[str_detail]["perhourspot"]
                        num_cost_per_month = num_cost_per_hour * 730
                        num_cost_per_month_one_year_reserved = num_cost_per_hour_one_year_reserved * 730
                        num_cost_per_month_three_year_reserved = num_cost_per_hour_three_year_reserved * 730
                        num_cost_per_month_one_year_savings = num_cost_per_hour_one_year_savings * 730
                        num_cost_per_month_three_year_savings = num_cost_per_hour_three_year_savings * 730
                        num_cost_per_month_spot = num_cost_per_hour_spot * 730

                        if bool_price_available:
                            if i == 0:
                                dict_record_data = {"region": az_region} 
                                result_prices_list.update(dict_record_data)
                            dict_record_data = {
                                "name": str_name,
                                "series": str_series,
                                "instance_name": str_instance_name,
                                "tier": str_tier,
                                "os": str_os,
                                "category": str_category,
                                "cores": num_cores,
                                "ram_gb": num_ram,
                                "disk_size_gb": num_disksize,
                                "has_paygo": bool_haspaygo,
                                "has_spot": bool_hasspot,
                                "is_in_preview": bool_isinpreview,
                                "is_vcpu": bool_isvcpu,
                                "is_constrained_core": bool_isconstrainedcore,
                                "is_base_vm": bool_isbasevm,
                                "region": str_region,
                                "region_name": str_region_name,
                                "country": str_country,
                                "country_name": str_country_name,
                                "geographic": str_geographic,
                                "geographic_name": str_geographic_name,
                                "price_available": bool_price_available,
                                "price_per_hour": num_cost_per_hour,
                                "price_per_month": num_cost_per_month,
                                "price_per_hour_one_year_reserved": num_cost_per_hour_one_year_reserved,
                                "price_per_month_one_year_reserved": num_cost_per_month_one_year_reserved,
                                "price_per_hour_three_year_reserved": num_cost_per_hour_three_year_reserved,
                                "price_per_month_three_year_reserved": num_cost_per_month_three_year_reserved,
                                "price_per_hour_one_year_savings": num_cost_per_hour_one_year_savings,
                                "price_per_month_one_year_savings": num_cost_per_month_one_year_savings,
                                "price_per_hour_three_year_savings": num_cost_per_hour_three_year_savings,
                                "price_per_month_three_year_savings": num_cost_per_month_three_year_savings,
                                "price_per_hour_spot": num_cost_per_hour_spot,
                                "price_per_month_spot": num_cost_per_month_spot
                            }
                            dict_record_data = {str_detail: dict_record_data} 
                            result_prices_list_records.update(dict_record_data)
                            if not is_silent_enabled:
                                print(f"Added price for SKU {str_detail} in region {str_region}")
                            if is_logging_enabled:
                                logs.append(f"OK: Added price for SKU {str_detail} in region {str_region}")

                            i += 1
                if not is_silent_enabled:
                    bar_sku_detail.text = item_bar
                    bar_sku_detail()

    if len(result_prices_list_records) > 0:
        result_prices_list.update({"prices_list": result_prices_list_records})

    logs_currencies, result_currencies_list = az_currencies_list_for_region(initial_data['currencies'], is_silent_enabled=is_silent_enabled, is_logging_enabled=is_logging_enabled)
    if is_logging_enabled:
        logs.extend(logs_currencies)

    if len(result_currencies_list) > 0:
        result_prices_list.update({"currencies_list": result_currencies_list})   

    end_price = datetime.now()

    delta_price = end_price - start_price

    if not is_silent_enabled:
        print(f"Total added SKU prices: {i}")
        print(f"Total processed SKU: {j}")
        print(f"Total processing time: {delta_price}")
    if is_logging_enabled:
        logs.append(f"Total added SKU prices: {i}")
        logs.append(f"Total processed SKU: {j}")
        logs.append(f"Total processing time: {delta_price}")

    return logs, result_prices_list
