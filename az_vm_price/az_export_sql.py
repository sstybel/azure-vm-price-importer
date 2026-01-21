from alive_progress import alive_bar

def az_bool_notation(bool_value=False):
    result = bool_value

    return result

def az_export_prices_list_to_sql(sql_prices_output_filename, prices_list={}, is_add_currency_sql=True, is_silent_enabled=False, is_logging_enabled=True):
    logs = []

    sql_create_table_prices = ""
    sql_create_table_prices += "CREATE TABLE IF NOT EXISTS az_vm_prices ("
    sql_create_table_prices += "id INTEGER PRIMARY KEY AUTOINCREMENT,"
    sql_create_table_prices += "name TEXT,"
    sql_create_table_prices += "series TEXT,"
    sql_create_table_prices += "instance_name TEXT,"
    sql_create_table_prices += "offer_name TEXT,"
    sql_create_table_prices += "tier TEXT,"
    sql_create_table_prices += "os TEXT,"
    sql_create_table_prices += "category TEXT,"
    sql_create_table_prices += "cores REAL,"
    sql_create_table_prices += "ram_gb REAL,"
    sql_create_table_prices += "disk_size_gb REAL,"
    sql_create_table_prices += "has_paygo NUMERIC,"
    sql_create_table_prices += "has_spot NUMERIC,"
    sql_create_table_prices += "is_in_preview NUMERIC,"
    sql_create_table_prices += "is_vcpu NUMERIC,"
    sql_create_table_prices += "is_constrained_core NUMERIC,"
    sql_create_table_prices += "is_base_vm NUMERIC,"
    sql_create_table_prices += "region TEXT,"
    sql_create_table_prices += "region_name TEXT,"
    sql_create_table_prices += "country TEXT,"
    sql_create_table_prices += "country_name TEXT,"
    sql_create_table_prices += "geographic TEXT,"
    sql_create_table_prices += "geographic_name TEXT,"
    sql_create_table_prices += "price_available NUMERIC,"
    sql_create_table_prices += "price_hybridbenefit NUMERIC,"
    sql_create_table_prices += "price_per_hour REAL,"
    sql_create_table_prices += "price_per_month REAL,"
    sql_create_table_prices += "price_per_hour_one_year_reserved REAL,"
    sql_create_table_prices += "price_per_month_one_year_reserved REAL,"
    sql_create_table_prices += "price_per_hour_three_year_reserved REAL,"
    sql_create_table_prices += "price_per_month_three_year_reserved REAL,"
    sql_create_table_prices += "price_per_hour_one_year_savings REAL,"
    sql_create_table_prices += "price_per_month_one_year_savings REAL,"
    sql_create_table_prices += "price_per_hour_three_year_savings REAL,"
    sql_create_table_prices += "price_per_month_three_year_savings REAL,"
    sql_create_table_prices += "price_per_hour_spot REAL,"
    sql_create_table_prices += "price_per_month_spot REAL,"
    sql_create_table_prices += "price_per_hour_hybridbenefit REAL,"
    sql_create_table_prices += "price_per_month_hybridbenefit REAL,"
    sql_create_table_prices += "price_per_hour_one_year_reserved_hybridbenefit REAL,"
    sql_create_table_prices += "price_per_month_one_year_reserved_hybridbenefit REAL,"
    sql_create_table_prices += "price_per_hour_three_year_reserved_hybridbenefit REAL,"
    sql_create_table_prices += "price_per_month_three_year_reserved_hybridbenefit REAL,"
    sql_create_table_prices += "price_per_hour_one_year_savings_hybridbenefit REAL,"
    sql_create_table_prices += "price_per_month_one_year_savings_hybridbenefit REAL,"
    sql_create_table_prices += "price_per_hour_three_year_savings_hybridbenefit REAL,"
    sql_create_table_prices += "price_per_month_three_year_savings_hybridbenefit REAL,"
    sql_create_table_prices += "price_per_hour_spot_hybridbenefit REAL,"
    sql_create_table_prices += "price_per_month_spot_hybridbenefit REAL)"

    sql_create_table_prices_currency = ""
    sql_create_table_prices_currency += "CREATE TABLE IF NOT EXISTS az_prices_currency ("
    sql_create_table_prices_currency += "id INTEGER PRIMARY KEY AUTOINCREMENT,"
    sql_create_table_prices_currency += "currency TEXT,"
    sql_create_table_prices_currency += "currency_info TEXT,"
    sql_create_table_prices_currency += "currency_name TEXT,"
    sql_create_table_prices_currency += "currency_symbol TEXT,"
    sql_create_table_prices_currency += "currency_conversion REAL,"
    sql_create_table_prices_currency += "currency_conversion_onprem REAL,"
    sql_create_table_prices_currency += "currency_conversion_modern REAL)"

    try:
        if not is_silent_enabled:
            print(f"Export Azure VM prices to SQL notation in file: {sql_prices_output_filename}")
        if is_logging_enabled:
            logs.append(f"OK: Export Azure VM prices to SQL notation in file: {sql_prices_output_filename}")
        with open(sql_prices_output_filename, 'w', encoding='utf-8') as sql_file:
            prices_list_records = prices_list['prices_list']
            prices_list_records = dict(sorted(prices_list_records.items(), key=lambda item: (item[1]['cores'], item[1]['ram_gb'], item[1]['disk_size_gb'])))
            
            i = 0
            
            max_bar = len(prices_list_records)
            with alive_bar(max_bar, title="Export prices records to SQL notation", disable=is_silent_enabled) as bar:
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
                    str_has_paygo = str(az_bool_notation(price_item_record['has_paygo']))
                    str_has_spot = str(az_bool_notation(price_item_record['has_spot']))
                    str_is_in_preview = str(az_bool_notation(price_item_record['is_in_preview']))
                    str_is_vcpu = str(az_bool_notation(price_item_record['is_vcpu']))
                    str_is_constrained_core = str(az_bool_notation(price_item_record['is_constrained_core']))
                    str_is_base_vm = str(az_bool_notation(price_item_record['is_base_vm']))
                    str_region = price_item_record['region']
                    str_region_name = price_item_record['region_name']
                    str_country = price_item_record['country']
                    str_country_name = price_item_record['country_name']
                    str_geographic = price_item_record['geographic']
                    str_geographic_name = price_item_record['geographic_name']
                    str_price_available = str(az_bool_notation(price_item_record['price_available']))
                    str_price_hybridbenefit = str(az_bool_notation(price_item_record['price_hybridbenefit']))
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

                    sql_insert_price = ""
                    sql_insert_price += "INSERT INTO az_vm_prices("
                    sql_insert_price += "name, series, instance_name, offer_name, tier, os, category, cores, ram_gb, disk_size_gb, has_paygo, has_spot, is_in_preview, is_vcpu, "
                    sql_insert_price += "is_constrained_core, is_base_vm, region, region_name, country, country_name, geographic, geographic_name, price_available, price_hybridbenefit, "
                    sql_insert_price += "price_per_hour, price_per_month, price_per_hour_one_year_reserved, price_per_month_one_year_reserved, price_per_hour_three_year_reserved, "
                    sql_insert_price += "price_per_month_three_year_reserved, price_per_hour_one_year_savings, price_per_month_one_year_savings, price_per_hour_three_year_savings, "
                    sql_insert_price += "price_per_month_three_year_savings, price_per_hour_spot, price_per_month_spot, price_per_hour_hybridbenefit, price_per_month_hybridbenefit, "
                    sql_insert_price += "price_per_hour_one_year_reserved_hybridbenefit, price_per_month_one_year_reserved_hybridbenefit, price_per_hour_three_year_reserved_hybridbenefit, "
                    sql_insert_price += "price_per_month_three_year_reserved_hybridbenefit, price_per_hour_one_year_savings_hybridbenefit, price_per_month_one_year_savings_hybridbenefit, "
                    sql_insert_price += "price_per_hour_three_year_savings_hybridbenefit, price_per_month_three_year_savings_hybridbenefit, price_per_hour_spot_hybridbenefit, "
                    sql_insert_price += "price_per_month_spot_hybridbenefit) "
                    sql_insert_price += "VALUES ("
                    sql_insert_price += f"'{str_name}', '{str_series}', '{str_instance_name}', '{str_offer_name}', '{str_tier}', '{str_os}', '{str_category}', '{str_cores}', "
                    sql_insert_price += f"'{str_ram_gb}', '{str_disk_size_gb}', '{str_has_paygo}', '{str_has_spot}', '{str_is_in_preview}', '{str_is_vcpu}', '{str_is_constrained_core}', "
                    sql_insert_price += f"'{str_is_base_vm}', '{str_region}', '{str_region_name}', '{str_country}', '{str_country_name}', '{str_geographic}', '{str_geographic_name}', "
                    sql_insert_price += f"'{str_price_available}', '{str_price_hybridbenefit}', '{str_price_per_hour}', '{str_price_per_month}', '{str_price_per_hour_one_year_reserved}', "
                    sql_insert_price += f"'{str_price_per_month_one_year_reserved}', '{str_price_per_hour_three_year_reserved}', '{str_price_per_month_three_year_reserved}', "
                    sql_insert_price += f"'{str_price_per_hour_one_year_savings}', '{str_price_per_month_one_year_savings}', '{str_price_per_hour_three_year_savings}', "
                    sql_insert_price += f"'{str_price_per_month_three_year_savings}', '{str_price_per_hour_spot}', '{str_price_per_month_spot}', "
                    sql_insert_price += f"'{str_price_per_hour_hybridbenefit}', '{str_price_per_month_hybridbenefit}', '{str_price_per_hour_one_year_reserved_hybridbenefit}', "
                    sql_insert_price += f"'{str_price_per_month_one_year_reserved_hybridbenefit}', '{str_price_per_hour_three_year_reserved_hybridbenefit}', '{str_price_per_month_three_year_reserved_hybridbenefit}', "
                    sql_insert_price += f"'{str_price_per_hour_one_year_savings_hybridbenefit}', '{str_price_per_month_one_year_savings_hybridbenefit}', '{str_price_per_hour_three_year_savings_hybridbenefit}', "
                    sql_insert_price += f"'{str_price_per_month_three_year_savings_hybridbenefit}', '{str_price_per_hour_spot_hybridbenefit}', '{str_price_per_month_spot_hybridbenefit}'"
                    sql_insert_price += ");\n"

                    sql_file.write(sql_insert_price)

                    i += 1

                    if not is_silent_enabled:
                        bar.text = str_offer_name
                        bar()

            if not is_silent_enabled:
                print(f"Exported Azure VM prices count {i} to SQL notation file: {sql_prices_output_filename}")
            if is_logging_enabled:
                logs.append(f"OK: Exported Azure VM prices count {i} to SQL notation file {sql_prices_output_filename}")

            if is_add_currency_sql:
                currencies_prices_list_records = prices_list['currencies_list']
                currencies_prices_list_records = dict(sorted(currencies_prices_list_records.items()))     

                i = 0

                max_bar = len(currencies_prices_list_records)
                with alive_bar(max_bar, title="Export prices currencies record to SQL notation", disable=is_silent_enabled) as bar:
                    for currencies_price_item in currencies_prices_list_records:
                        currencies_price_item_record = currencies_prices_list_records[currencies_price_item]
                        str_currency = currencies_price_item
                        str_currency_name = currencies_price_item_record['name']
                        str_currency_info = currencies_price_item_record['info']
                        str_currency_symbol = currencies_price_item_record['symbol']
                        str_currency_conversion = str(currencies_price_item_record['conversion'])
                        str_currency_conversion_onprem = str(currencies_price_item_record['conversion_onprem'])
                        str_currency_conversion_modern = str(currencies_price_item_record['conversion_modern'])

                        sql_insert_price_currency = ""
                        sql_insert_price_currency += "INSERT INTO az_prices_currency("
                        sql_insert_price_currency += "currency, currency_info, currency_name, currency_symbol, currency_conversion, currency_conversion_onprem, currency_conversion_modern) "
                        sql_insert_price_currency += "VALUES ("
                        sql_insert_price_currency += f"'{str_currency}', '{str_currency_info}', '{str_currency_name}', '{str_currency_symbol}', '{str_currency_conversion}', '{str_currency_conversion_onprem}', '{str_currency_conversion_modern}'"
                        sql_insert_price_currency += ");\n"

                        sql_file.write(sql_insert_price_currency)

                        i += 1

                        if not is_silent_enabled:
                            bar.text = str_currency
                            bar()

                if not is_silent_enabled:
                    print(f"Exported Azure VM prices currencies count {i} to SQL notation file: {sql_prices_output_filename}")
                if is_logging_enabled:
                    logs.append(f"OK: Exported Azure VM prices currencies count {i} to SQL notation file {sql_prices_output_filename}")

            sql_file.close()

    except Exception as e:
        if not is_silent_enabled:
            print(f"Unable to export Azure VM prices to SQL notation file {sql_prices_output_filename}: {e}")
        if is_logging_enabled:
            logs.append(f"ERR-FILE: Unable to export Azure VM prices to SQL notation file {sql_prices_output_filename}: {e}")

    return logs
