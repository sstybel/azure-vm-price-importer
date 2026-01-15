from alive_progress import alive_bar

def az_export_prices_list_to_csv(csv_prices_output_filename, csv_currencies_output_filename, prices_list={}, is_silent_enabled=False, is_logging_enabled=True):
    logs = []

    char_delimiter = ";"
    char_currency = ","

    csv_head_prices = ""
    csv_head_prices =  csv_head_prices + "\"name\";\"series\";\"instance_name\";\"offer_name\";\"tier\";\"os\";\"category\";\"cores\";\"ram_gb\";\"disk_size_gb\";\"has_paygo\";\"has_spot\";"
    csv_head_prices =  csv_head_prices + "\"is_in_preview\";\"is_vcpu\";\"is_constrained_core\";\"is_base_vm\";\"region\";\"region_name\";\"country\";\"country_name\";\"geographic\";"
    csv_head_prices =  csv_head_prices + "\"geographic_name\";\"price_available\";\"price_hybridbenefit\";\"price_per_hour\";\"price_per_month\";\"price_per_hour_one_year_reserved\";"
    csv_head_prices =  csv_head_prices + "\"price_per_month_one_year_reserved\";\"price_per_hour_three_year_reserved\";\"price_per_month_three_year_reserved\";"
    csv_head_prices =  csv_head_prices + "\"price_per_hour_one_year_savings\";\"price_per_month_one_year_savings\";\"price_per_hour_three_year_savings\";"
    csv_head_prices =  csv_head_prices + "\"price_per_month_three_year_savings\";\"price_per_hour_spot\";\"price_per_month_spot\";"
    csv_head_prices =  csv_head_prices + "\"price_per_hour_hybridbenefit\";\"price_per_month_hybridbenefit\";\"price_per_hour_one_year_reserved_hybridbenefit\";"
    csv_head_prices =  csv_head_prices + "\"price_per_month_one_year_reserved_hybridbenefit\";\"price_per_hour_three_year_reserved_hybridbenefit\";\"price_per_month_three_year_reserved_hybridbenefit\";"
    csv_head_prices =  csv_head_prices + "\"price_per_hour_one_year_savings_hybridbenefit\";\"price_per_month_one_year_savings_hybridbenefit\";\"price_per_hour_three_year_savings_hybridbenefit\";"
    csv_head_prices =  csv_head_prices + "\"price_per_month_three_year_savings_hybridbenefit\";\"price_per_hour_spot_hybridbenefit\";\"price_per_month_spot_hybridbenefit\""

    csv_head_prices_currencies = ""
    csv_head_prices_currencies = csv_head_prices_currencies + "\"currency\";\"currency_name\";\"currency_info\";\"currency_symbol\";\"currency_conversion\";\"currency_conversion_onprem\";"
    csv_head_prices_currencies = csv_head_prices_currencies + "\"currency_conversion_modern\""
    
    csv_head_prices = csv_head_prices.replace(";", char_delimiter)
    csv_head_prices_currencies = csv_head_prices_currencies.replace(";", char_delimiter)

    i = 0

    try:
        if not is_silent_enabled:
            print(f"Export Azure VM prices to CSV file: {csv_prices_output_filename}")
        if is_logging_enabled:
            logs.append(f"OK: Export Azure VM prices to CSV file {csv_prices_output_filename}")
        with open(csv_prices_output_filename, 'w', encoding='utf-8') as csv_prices_file:
            csv_prices_file.write(f"{csv_head_prices}\n")
            prices_list_records = prices_list['prices_list']
            max_bar = len(prices_list_records)
            with alive_bar(max_bar, title="Export prices record to CSV", disable=is_silent_enabled) as bar:
                for price_item in prices_list_records:
                    price_item_record = prices_list_records[price_item]
                    str_name = price_item_record['name']
                    str_series = price_item_record['series']
                    str_instance_name = price_item_record['instance_name']
                    str_offer_name = price_item
                    str_tier = price_item_record['tier']
                    str_os = price_item_record['os']
                    str_category = price_item_record['category']
                    str_cores = str(price_item_record['cores'])
                    str_ram_gb = str(price_item_record['ram_gb'])
                    str_disk_size_gb = str(price_item_record['disk_size_gb'])
                    str_has_paygo = str(price_item_record['has_paygo'])
                    str_has_spot = str(price_item_record['has_spot'])
                    str_is_in_preview = str(price_item_record['is_in_preview'])
                    str_is_vcpu = str(price_item_record['is_vcpu'])
                    str_is_constrained_core = str(price_item_record['is_constrained_core'])
                    str_is_base_vm = str(price_item_record['is_base_vm'])
                    str_region = price_item_record['region']
                    str_region_name = price_item_record['region_name']
                    str_country = price_item_record['country']
                    str_country_name = price_item_record['country_name']
                    str_geographic = price_item_record['geographic']
                    str_geographic_name = price_item_record['geographic_name']
                    str_price_available = str(price_item_record['price_available'])
                    str_price_hybridbenefit = str(price_item_record['price_hybridbenefit'])
                    str_price_per_hour = str(price_item_record['price_per_hour'])
                    str_price_per_month = str(price_item_record['price_per_month'])
                    str_price_per_hour_one_year_reserved = str(price_item_record['price_per_hour_one_year_reserved'])
                    str_price_per_month_one_year_reserved = str(price_item_record['price_per_month_one_year_reserved'])
                    str_price_per_hour_three_year_reserved = str(price_item_record['price_per_hour_three_year_reserved'])
                    str_price_per_month_three_year_reserved = str(price_item_record['price_per_month_three_year_reserved'])
                    str_price_per_hour_one_year_savings = str(price_item_record['price_per_hour_one_year_savings'])
                    str_price_per_month_one_year_savings = str(price_item_record['price_per_month_one_year_savings'])
                    str_price_per_hour_three_year_savings = str(price_item_record['price_per_hour_three_year_savings'])
                    str_price_per_month_three_year_savings = str(price_item_record['price_per_month_three_year_savings'])
                    str_price_per_hour_spot = str(price_item_record['price_per_hour_spot'])
                    str_price_per_month_spot = str(price_item_record['price_per_month_spot'])
                    str_price_per_hour_hybridbenefit = str(price_item_record['price_per_hour_hybridbenefit'])
                    str_price_per_month_hybridbenefit = str(price_item_record['price_per_month_hybridbenefit'])
                    str_price_per_hour_one_year_reserved_hybridbenefit = str(price_item_record['price_per_hour_one_year_reserved_hybridbenefit'])
                    str_price_per_month_one_year_reserved_hybridbenefit = str(price_item_record['price_per_month_one_year_reserved_hybridbenefit'])
                    str_price_per_hour_three_year_reserved_hybridbenefit = str(price_item_record['price_per_hour_three_year_reserved_hybridbenefit'])
                    str_price_per_month_three_year_reserved_hybridbenefit = str(price_item_record['price_per_month_three_year_reserved_hybridbenefit'])
                    str_price_per_hour_one_year_savings_hybridbenefit = str(price_item_record['price_per_hour_one_year_savings_hybridbenefit'])
                    str_price_per_month_one_year_savings_hybridbenefit = str(price_item_record['price_per_month_one_year_savings_hybridbenefit'])
                    str_price_per_hour_three_year_savings_hybridbenefit = str(price_item_record['price_per_hour_three_year_savings_hybridbenefit'])
                    str_price_per_month_three_year_savings_hybridbenefit = str(price_item_record['price_per_month_three_year_savings_hybridbenefit'])
                    str_price_per_hour_spot_hybridbenefit = str(price_item_record['price_per_hour_spot_hybridbenefit'])
                    str_price_per_month_spot_hybridbenefit = str(price_item_record['price_per_month_spot_hybridbenefit'])

                    csv_prices_record = ""
                    csv_prices_record = csv_prices_record + f"\"{str_name}\";\"{str_series}\";\"{str_instance_name}\";\"{str_offer_name}\";\"{str_tier}\";\"{str_os}\";\"{str_category}\";\"{str_cores}\";"
                    csv_prices_record = csv_prices_record + f"\"{str_ram_gb}\";\"{str_disk_size_gb}\";\"{str_has_paygo}\";\"{str_has_spot}\";\"{str_is_in_preview}\";\"{str_is_vcpu}\";\"{str_is_constrained_core}\";"
                    csv_prices_record = csv_prices_record + f"\"{str_is_base_vm}\";\"{str_region}\";\"{str_region_name}\";\"{str_country}\";\"{str_country_name}\";\"{str_geographic}\";\"{str_geographic_name}\";"
                    csv_prices_record = csv_prices_record + f"\"{str_price_available}\";\"{str_price_hybridbenefit}\";\"{str_price_per_hour}\";\"{str_price_per_month}\";\"{str_price_per_hour_one_year_reserved}\";"
                    csv_prices_record = csv_prices_record + f"\"{str_price_per_month_one_year_reserved}\";\"{str_price_per_hour_three_year_reserved}\";\"{str_price_per_month_three_year_reserved}\";"
                    csv_prices_record = csv_prices_record + f"\"{str_price_per_hour_one_year_savings}\";\"{str_price_per_month_one_year_savings}\";\"{str_price_per_hour_three_year_savings}\";"
                    csv_prices_record = csv_prices_record + f"\"{str_price_per_month_three_year_savings}\";\"{str_price_per_hour_spot}\";\"{str_price_per_month_spot}\"\n"
                    csv_prices_record = csv_prices_record + f"\"{str_price_per_hour_hybridbenefit}\";\"{str_price_per_month_hybridbenefit}\";\"{str_price_per_hour_one_year_reserved_hybridbenefit}\";"
                    csv_prices_record = csv_prices_record + f"\"{str_price_per_month_one_year_reserved_hybridbenefit}\";\"{str_price_per_hour_three_year_reserved_hybridbenefit}\";\"{str_price_per_month_three_year_reserved_hybridbenefit}\";"
                    csv_prices_record = csv_prices_record + f"\"{str_price_per_hour_one_year_savings_hybridbenefit}\";\"{str_price_per_month_one_year_savings_hybridbenefit}\";\"{str_price_per_hour_three_year_savings_hybridbenefit}\";"
                    csv_prices_record = csv_prices_record + f"\"{str_price_per_month_three_year_savings_hybridbenefit}\";\"{str_price_per_hour_spot_hybridbenefit}\";\"{str_price_per_month_spot_hybridbenefit}\"\n"

                    csv_prices_record = csv_prices_record.replace(";", char_delimiter).replace(".", char_currency)

                    csv_prices_file.write(csv_prices_record)

                    i += 1

                    if not is_silent_enabled:
                        bar.text = str_offer_name
                        bar()

        if not is_silent_enabled:
            print(f"Exported Azure VM prices count {i} to CSV file: {csv_prices_output_filename}")
        if is_logging_enabled:
            logs.append(f"OK: Exported Azure VM prices count {i} to CSV file {csv_prices_output_filename}")
    except Exception as e:
        if not is_silent_enabled:
            print(f"Unable to export Azure VM prices to CSV file {csv_prices_output_filename}: {e}")
        if is_logging_enabled:
            logs.append(f"ERR-FILE: Unable to export Azure VM prices to CSV file {csv_prices_output_filename}: {e}")

    i = 0

    try:
        with open(csv_currencies_output_filename, 'w', encoding='utf-8') as csv_prices_currencies_file:
            csv_prices_currencies_file.write(f"{csv_head_prices_currencies}\n")
            currencies_prices_list_records = prices_list['currencies_list']
            max_bar = len(currencies_prices_list_records)
            with alive_bar(max_bar, title="Export prices record to CSV", disable=is_silent_enabled) as bar:
                for currencies_price_item in currencies_prices_list_records:
                    currencies_price_item_record = currencies_prices_list_records[currencies_price_item]
                    str_currency = currencies_price_item
                    str_currency_name = currencies_price_item_record['name']
                    str_currency_info = currencies_price_item_record['info']
                    str_currency_symbol = currencies_price_item_record['symbol']
                    str_currency_conversion = str(currencies_price_item_record['conversion'])
                    str_currency_conversion_onprem = str(currencies_price_item_record['conversion_onprem'])
                    str_currency_conversion_modern = str(currencies_price_item_record['conversion_modern'])

                    csv_prices_currencies_record = f"\"{str_currency}\";\"{str_currency_name}\";\"{str_currency_info}\";\"{str_currency_symbol}\";\"{str_currency_conversion}\";\"{str_currency_conversion_onprem}\";\"{str_currency_conversion_modern}\"\n"
                    csv_prices_currencies_record = csv_prices_currencies_record.replace(";", char_delimiter).replace(".", char_currency)

                    csv_prices_currencies_file.write(csv_prices_currencies_record)

                    i += 1

                    if not is_silent_enabled:
                        bar.text = str_currency
                        bar()

        if not is_silent_enabled:
            print(f"Exported Azure VM prices currencies count {i} to CSV file: {csv_currencies_output_filename}")
        result_export_currencies = f"OK: Exported Azure VM prices currencies count {i} to CSV file {csv_currencies_output_filename}"
    except Exception as e:
        if not is_silent_enabled:
            print(f"Unable to export Azure VM prices currencies to CSV file {csv_currencies_output_filename}: {e}")
        result_export_currencies = f"ERR-FILE: Unable to export Azure VM prices currencies to CSV file {csv_currencies_output_filename}: {e}"
    if is_logging_enabled:
        logs.append(result_export_currencies)

    return logs