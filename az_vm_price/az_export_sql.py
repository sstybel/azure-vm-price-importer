from alive_progress import alive_bar

def az_bool_notation(bool_value=False, sql_notation='sqlite'):
    result = bool_value

    if sql_notation == "sqlite":
            if  bool_value == True:
                result = 1
            else:
                result = 0
    else:
        result = bool_value
    
    return result

def az_export_prices_list_to_sql(sql_prices_output_filename, sql_notation="sqlite", prices_list={}, is_add_currency_sql=True, is_silent_enabled=False, is_logging_enabled=True):
    logs = []

    notation = sql_notation.lower()

    match notation:
        case "mysql":
            notation = "mysql"
            notation_name = "MySQL"
            sql_create_table_int = "INT NOT NULL"
            sql_create_table_str50 = "VARCHAR(50) NOT NULL"
            sql_create_table_str100 = "VARCHAR(100) NOT NULL"
            sql_create_table_real = "DOUBLE NOT NULL DEFAULT '0.0'"
            sql_create_table_bool = "ENUM('False','True') NOT NULL DEFAULT 'False'"
            sql_create_table_autoinc = sql_create_table_int + " AUTO_INCREMENT"
            sql_add_first = ""
            sql_add_last = ""
            sql_add_last += ", PRIMARY KEY (`id`)"
            sql_add_last += ") ENGINE=InnoDB DEFAULT CHARSET=utf8;"
        case "postgresql":
            notation = "postgresql"
            notation_name = "PostgreSQL"
            sql_create_table_int = "INT NOT NULL"
            sql_create_table_str50 = "VARCHAR(50) NOT NULL"
            sql_create_table_str100 = "VARCHAR(100) NOT NULL"
            sql_create_table_real = "DOUBLE PRECISION NOT NULL DEFAULT '0.0'"
            sql_create_table_bool = "ENUM_BOOL NOT NULL DEFAULT 'False'"
            sql_create_table_autoinc = " BIGSERIAL PRIMARY KEY"
            sql_add_first = ""
            sql_add_first += "CREATE TYPE enum_bool AS ENUM('False', 'True');\n"
            sql_add_last = ""
            sql_add_last += ");"
        case _:
            notation = "sqlite"
            notation_name = "SQLite"
            sql_create_table_int = "INT NOT NULL"
            sql_create_table_str50 = "TEXT NOT NULL"
            sql_create_table_str100 = "TEXT NOT NULL"
            sql_create_table_real = "REAL NOT NULL DEFAULT '0.0'"
            sql_create_table_bool = "NUMERIC NOT NULL DEFAULT '0'"
            sql_create_table_autoinc = "INTEGER PRIMARY KEY AUTOINCREMENT"
            sql_add_first = ""
            sql_add_last = ""
            sql_add_last += ");"

    sql_create_table_prices = ""
    sql_create_table_prices += "CREATE TABLE IF NOT EXISTS az_vm_prices ("
    sql_create_table_prices += "id " + sql_create_table_autoinc + ", "
    sql_create_table_prices += "name " + sql_create_table_str50 + ", "
    sql_create_table_prices += "series " + sql_create_table_str50 + ", "
    sql_create_table_prices += "instance_name " + sql_create_table_str50 + ", "
    sql_create_table_prices += "offer_name " + sql_create_table_str100 + ", "
    sql_create_table_prices += "tier " + sql_create_table_str50 + ", "
    sql_create_table_prices += "os " + sql_create_table_str50 + ", "
    sql_create_table_prices += "category " + sql_create_table_str50 + ", "
    sql_create_table_prices += "cores " + sql_create_table_real + ", "
    sql_create_table_prices += "ram_gb " + sql_create_table_real + ", "
    sql_create_table_prices += "disk_size_gb " + sql_create_table_real + ", "
    sql_create_table_prices += "has_paygo " + sql_create_table_bool + ", "
    sql_create_table_prices += "has_spot " + sql_create_table_bool + ", "
    sql_create_table_prices += "is_in_preview " + sql_create_table_bool + ", "
    sql_create_table_prices += "is_vcpu " + sql_create_table_bool + ", "
    sql_create_table_prices += "is_constrained_core " + sql_create_table_bool + ", "
    sql_create_table_prices += "is_base_vm " + sql_create_table_bool + ", "
    sql_create_table_prices += "region " + sql_create_table_str100 + ", "
    sql_create_table_prices += "region_name " + sql_create_table_str100 + ", "
    sql_create_table_prices += "country " + sql_create_table_str100 + ", "
    sql_create_table_prices += "country_name " + sql_create_table_str100 + ", "
    sql_create_table_prices += "geographic " + sql_create_table_str100 + ", "
    sql_create_table_prices += "geographic_name " + sql_create_table_str100 + ", "
    sql_create_table_prices += "price_available " + sql_create_table_bool + ", "
    sql_create_table_prices += "price_hybridbenefit " + sql_create_table_bool + ", "
    sql_create_table_prices += "price_per_hour " + sql_create_table_real + ", "
    sql_create_table_prices += "price_per_month " + sql_create_table_real + ", "
    sql_create_table_prices += "price_per_hour_one_year_reserved " + sql_create_table_real + ", "
    sql_create_table_prices += "price_per_month_one_year_reserved " + sql_create_table_real + ", "
    sql_create_table_prices += "price_per_hour_three_year_reserved " + sql_create_table_real + ", "
    sql_create_table_prices += "price_per_month_three_year_reserved " + sql_create_table_real + ", "
    sql_create_table_prices += "price_per_hour_one_year_savings " + sql_create_table_real + ", "
    sql_create_table_prices += "price_per_month_one_year_savings " + sql_create_table_real + ", "
    sql_create_table_prices += "price_per_hour_three_year_savings " + sql_create_table_real + ", "
    sql_create_table_prices += "price_per_month_three_year_savings " + sql_create_table_real + ", "
    sql_create_table_prices += "price_per_hour_spot " + sql_create_table_real + ", "
    sql_create_table_prices += "price_per_month_spot " + sql_create_table_real + ", "
    sql_create_table_prices += "price_per_hour_hybridbenefit " + sql_create_table_real + ", "
    sql_create_table_prices += "price_per_month_hybridbenefit " + sql_create_table_real + ", "
    sql_create_table_prices += "price_per_hour_one_year_reserved_hybridbenefit " + sql_create_table_real + ", "
    sql_create_table_prices += "price_per_month_one_year_reserved_hybridbenefit " + sql_create_table_real + ", "
    sql_create_table_prices += "price_per_hour_three_year_reserved_hybridbenefit " + sql_create_table_real + ", "
    sql_create_table_prices += "price_per_month_three_year_reserved_hybridbenefit " + sql_create_table_real + ", "
    sql_create_table_prices += "price_per_hour_one_year_savings_hybridbenefit " + sql_create_table_real + ", "
    sql_create_table_prices += "price_per_month_one_year_savings_hybridbenefit " + sql_create_table_real + ", "
    sql_create_table_prices += "price_per_hour_three_year_savings_hybridbenefit " + sql_create_table_real + ", "
    sql_create_table_prices += "price_per_month_three_year_savings_hybridbenefit " + sql_create_table_real + ", "
    sql_create_table_prices += "price_per_hour_spot_hybridbenefit " + sql_create_table_real + ", "
    sql_create_table_prices += "price_per_month_spot_hybridbenefit " + sql_create_table_real
    sql_create_table_prices += sql_add_last
    sql_create_table_prices += "\n"

    sql_create_table_prices_currency = ""
    sql_create_table_prices_currency += "CREATE TABLE IF NOT EXISTS az_prices_currency ("
    sql_create_table_prices_currency += "id " + sql_create_table_autoinc + ", "
    sql_create_table_prices_currency += "currency " + sql_create_table_str50 + ", "
    sql_create_table_prices_currency += "currency_info " + sql_create_table_str100 + ", "
    sql_create_table_prices_currency += "currency_name " + sql_create_table_str50 + ", "
    sql_create_table_prices_currency += "currency_symbol " + sql_create_table_str50 + ", "
    sql_create_table_prices_currency += "currency_conversion " + sql_create_table_real + ", "
    sql_create_table_prices_currency += "currency_conversion_onprem " + sql_create_table_real + ", "
    sql_create_table_prices_currency += "currency_conversion_modern " + sql_create_table_real
    sql_create_table_prices_currency += sql_add_last
    sql_create_table_prices_currency += "\n"

    try:
        if not is_silent_enabled:
            print(f"Export Azure VM prices to SQL notation ({notation_name}) in file: {sql_prices_output_filename}")
        if is_logging_enabled:
            logs.append(f"OK: Export Azure VM prices to SQL notation ({notation_name}) in file: {sql_prices_output_filename}")
        with open(sql_prices_output_filename, 'w', encoding='utf-8') as sql_file:
            prices_list_records = prices_list['prices_list']
            prices_list_records = dict(sorted(prices_list_records.items(), key=lambda item: (item[1]['cores'], item[1]['ram_gb'], item[1]['disk_size_gb'])))
            
            i = 0
            
            max_bar = len(prices_list_records)
            with alive_bar(max_bar, title=f"Export prices records to SQL notation ({notation_name})", disable=is_silent_enabled) as bar:
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
                    str_has_paygo = str(az_bool_notation(price_item_record['has_paygo'], sql_notation=notation))
                    str_has_spot = str(az_bool_notation(price_item_record['has_spot'], sql_notation=notation))
                    str_is_in_preview = str(az_bool_notation(price_item_record['is_in_preview'], sql_notation=notation))
                    str_is_vcpu = str(az_bool_notation(price_item_record['is_vcpu'], sql_notation=notation))
                    str_is_constrained_core = str(az_bool_notation(price_item_record['is_constrained_core'], sql_notation=notation))
                    str_is_base_vm = str(az_bool_notation(price_item_record['is_base_vm'], sql_notation=notation))
                    str_region = price_item_record['region']
                    str_region_name = price_item_record['region_name']
                    str_country = price_item_record['country']
                    str_country_name = price_item_record['country_name']
                    str_geographic = price_item_record['geographic']
                    str_geographic_name = price_item_record['geographic_name']
                    str_price_available = str(az_bool_notation(price_item_record['price_available'], sql_notation=notation))
                    str_price_hybridbenefit = str(az_bool_notation(price_item_record['price_hybridbenefit'], sql_notation=notation))
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
                   
                    if i == 0:
                        if sql_add_first.strip() != "":
                            sql_file.write(sql_add_first)
                        sql_file.write(sql_create_table_prices)

                    sql_file.write(sql_insert_price)

                    i += 1

                    if not is_silent_enabled:
                        bar.text = str_offer_name
                        bar()

            if not is_silent_enabled:
                print(f"Exported Azure VM prices count {i} to SQL notation ({notation_name}) file: {sql_prices_output_filename}")
            if is_logging_enabled:
                logs.append(f"OK: Exported Azure VM prices count {i} to SQL notation ({notation_name}) file {sql_prices_output_filename}")

            if is_add_currency_sql:
                currencies_prices_list_records = prices_list['currencies_list']
                currencies_prices_list_records = dict(sorted(currencies_prices_list_records.items()))     

                i = 0

                max_bar = len(currencies_prices_list_records)
                with alive_bar(max_bar, title=f"Export prices currencies record to SQL notation ({notation_name})", disable=is_silent_enabled) as bar:
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

                        if i == 0:
                            sql_file.write(sql_create_table_prices_currency)

                        sql_file.write(sql_insert_price_currency)

                        i += 1

                        if not is_silent_enabled:
                            bar.text = str_currency
                            bar()

                if not is_silent_enabled:
                    print(f"Exported Azure VM prices currencies count {i} to SQL notation ({notation_name}) file: {sql_prices_output_filename}")
                if is_logging_enabled:
                    logs.append(f"OK: Exported Azure VM prices currencies count {i} to SQL notation ({notation_name}) file {sql_prices_output_filename}")

            sql_file.close()

    except Exception as e:
        if not is_silent_enabled:
            print(f"Unable to export Azure VM prices to SQL notation ({notation_name}) file {sql_prices_output_filename}: {e}")
        if is_logging_enabled:
            logs.append(f"ERR-FILE: Unable to export Azure VM prices to SQL notation ({notation_name}) file {sql_prices_output_filename}: {e}")

    return logs
