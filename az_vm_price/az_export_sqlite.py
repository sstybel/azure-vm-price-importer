import sqlite3
from alive_progress import alive_bar

def az_bool_to_num(bool_value=False):
    num_bool = 0

    if  bool_value == True:
        num_bool = 1

    return num_bool

def az_export_prices_list_to_sqlite(sqlite_prices_output_filename, prices_list={}, is_silent_enabled=False, is_logging_enabled=True):
    logs = []

    sqlit_create_table_prices = ""
    sqlit_create_table_prices += "CREATE TABLE IF NOT EXISTS az_vm_prices ("
    sqlit_create_table_prices += "id INTEGER PRIMARY KEY AUTOINCREMENT,"
    sqlit_create_table_prices += "name TEXT,"
    sqlit_create_table_prices += "series TEXT,"
    sqlit_create_table_prices += "instance_name TEXT,"
    sqlit_create_table_prices += "offer_name TEXT,"
    sqlit_create_table_prices += "tier TEXT,"
    sqlit_create_table_prices += "os TEXT,"
    sqlit_create_table_prices += "category TEXT,"
    sqlit_create_table_prices += "cores REAL,"
    sqlit_create_table_prices += "ram_gb REAL,"
    sqlit_create_table_prices += "disk_size_gb REAL,"
    sqlit_create_table_prices += "has_paygo NUMERIC,"
    sqlit_create_table_prices += "has_spot NUMERIC,"
    sqlit_create_table_prices += "is_in_preview NUMERIC,"
    sqlit_create_table_prices += "is_vcpu NUMERIC,"
    sqlit_create_table_prices += "is_constrained_core NUMERIC,"
    sqlit_create_table_prices += "is_base_vm NUMERIC,"
    sqlit_create_table_prices += "region TEXT,"
    sqlit_create_table_prices += "region_name TEXT,"
    sqlit_create_table_prices += "country TEXT,"
    sqlit_create_table_prices += "country_name TEXT,"
    sqlit_create_table_prices += "geographic TEXT,"
    sqlit_create_table_prices += "geographic_name TEXT,"
    sqlit_create_table_prices += "price_available NUMERIC,"
    sqlit_create_table_prices += "price_hybridbenefit NUMERIC,"
    sqlit_create_table_prices += "price_per_hour REAL,"
    sqlit_create_table_prices += "price_per_month REAL,"
    sqlit_create_table_prices += "price_per_hour_one_year_reserved REAL,"
    sqlit_create_table_prices += "price_per_month_one_year_reserved REAL,"
    sqlit_create_table_prices += "price_per_hour_three_year_reserved REAL,"
    sqlit_create_table_prices += "price_per_month_three_year_reserved REAL,"
    sqlit_create_table_prices += "price_per_hour_one_year_savings REAL,"
    sqlit_create_table_prices += "price_per_month_one_year_savings REAL,"
    sqlit_create_table_prices += "price_per_hour_three_year_savings REAL,"
    sqlit_create_table_prices += "price_per_month_three_year_savings REAL,"
    sqlit_create_table_prices += "price_per_hour_spot REAL,"
    sqlit_create_table_prices += "price_per_month_spot REAL,"
    sqlit_create_table_prices += "price_per_hour_hybridbenefit REAL,"
    sqlit_create_table_prices += "price_per_month_hybridbenefit REAL,"
    sqlit_create_table_prices += "price_per_hour_one_year_reserved_hybridbenefit REAL,"
    sqlit_create_table_prices += "price_per_month_one_year_reserved_hybridbenefit REAL,"
    sqlit_create_table_prices += "price_per_hour_three_year_reserved_hybridbenefit REAL,"
    sqlit_create_table_prices += "price_per_month_three_year_reserved_hybridbenefit REAL,"
    sqlit_create_table_prices += "price_per_hour_one_year_savings_hybridbenefit REAL,"
    sqlit_create_table_prices += "price_per_month_one_year_savings_hybridbenefit REAL,"
    sqlit_create_table_prices += "price_per_hour_three_year_savings_hybridbenefit REAL,"
    sqlit_create_table_prices += "price_per_month_three_year_savings_hybridbenefit REAL,"
    sqlit_create_table_prices += "price_per_hour_spot_hybridbenefit REAL,"
    sqlit_create_table_prices += "price_per_month_spot_hybridbenefit REAL)"

    sqlit_create_table_prices_currency = ""
    sqlit_create_table_prices_currency += "CREATE TABLE IF NOT EXISTS az_prices_currency ("
    sqlit_create_table_prices_currency += "id INTEGER PRIMARY KEY AUTOINCREMENT,"
    sqlit_create_table_prices_currency += "currency TEXT,"
    sqlit_create_table_prices_currency += "currency_info TEXT,"
    sqlit_create_table_prices_currency += "currency_name TEXT,"
    sqlit_create_table_prices_currency += "currency_symbol TEXT,"
    sqlit_create_table_prices_currency += "currency_conversion REAL,"
    sqlit_create_table_prices_currency += "currency_conversion_onprem REAL,"
    sqlit_create_table_prices_currency += "currency_conversion_modern REAL)"

    try:
        if not is_silent_enabled:
            print(f"Export Azure VM prices to SQLite Data Base in file: {sqlite_prices_output_filename}")
        if is_logging_enabled:
            logs.append(f"OK: Export Azure VM prices to SQLite Data Base in file: {sqlite_prices_output_filename}")
        with sqlite3.connect(sqlite_prices_output_filename) as sqlite_prices_file:
            if not is_silent_enabled:
                print(f"Connect to SQLite Data Base in file: {sqlite_prices_output_filename}")
            if is_logging_enabled:
                logs.append(f"OK: Connect to SQLite Data Base in file: {sqlite_prices_output_filename}")
            
            db_cursor = sqlite_prices_file.cursor()
            
            db_cursor.execute(sqlit_create_table_prices)
            db_cursor.execute(sqlit_create_table_prices_currency)
            
            sqlite_prices_file.commit

            if not is_silent_enabled:
                print(f"Create tables if not exist in SQLite Data Base of file: {sqlite_prices_output_filename}")
            if is_logging_enabled:
                logs.append(f"OK: Create tables if not exist in SQLite Data Base of file: {sqlite_prices_output_filename}")

            prices_list_records = prices_list['prices_list']
            prices_list_records = dict(sorted(prices_list_records.items(), key=lambda item: (item[1]['cores'], item[1]['ram_gb'], item[1]['disk_size_gb'])))
            
            i = 0
            
            max_bar = len(prices_list_records)
            with alive_bar(max_bar, title="Export prices records to SQLite Data Base", disable=is_silent_enabled) as bar:
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
                    str_has_paygo = str(az_bool_to_num(price_item_record['has_paygo']))
                    str_has_spot = str(az_bool_to_num(price_item_record['has_spot']))
                    str_is_in_preview = str(az_bool_to_num(price_item_record['is_in_preview']))
                    str_is_vcpu = str(az_bool_to_num(price_item_record['is_vcpu']))
                    str_is_constrained_core = str(az_bool_to_num(price_item_record['is_constrained_core']))
                    str_is_base_vm = str(az_bool_to_num(price_item_record['is_base_vm']))
                    str_region = price_item_record['region']
                    str_region_name = price_item_record['region_name']
                    str_country = price_item_record['country']
                    str_country_name = price_item_record['country_name']
                    str_geographic = price_item_record['geographic']
                    str_geographic_name = price_item_record['geographic_name']
                    str_price_available = str(az_bool_to_num(price_item_record['price_available']))
                    str_price_hybridbenefit = str(az_bool_to_num(price_item_record['price_hybridbenefit']))
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

                    sqlite_insert_price = ""
                    sqlite_insert_price += "INSERT INTO az_vm_prices("
                    sqlite_insert_price += "name, series, instance_name, offer_name, tier, os, category, cores, ram_gb, disk_size_gb, has_paygo, has_spot, is_in_preview, is_vcpu, "
                    sqlite_insert_price += "is_constrained_core, is_base_vm, region, region_name, country, country_name, geographic, geographic_name, price_available, price_hybridbenefit, "
                    sqlite_insert_price += "price_per_hour, price_per_month, price_per_hour_one_year_reserved, price_per_month_one_year_reserved, price_per_hour_three_year_reserved, "
                    sqlite_insert_price += "price_per_month_three_year_reserved, price_per_hour_one_year_savings, price_per_month_one_year_savings, price_per_hour_three_year_savings, "
                    sqlite_insert_price += "price_per_month_three_year_savings, price_per_hour_spot, price_per_month_spot, price_per_hour_hybridbenefit, price_per_month_hybridbenefit, "
                    sqlite_insert_price += "price_per_hour_one_year_reserved_hybridbenefit, price_per_month_one_year_reserved_hybridbenefit, price_per_hour_three_year_reserved_hybridbenefit, "
                    sqlite_insert_price += "price_per_month_three_year_reserved_hybridbenefit, price_per_hour_one_year_savings_hybridbenefit, price_per_month_one_year_savings_hybridbenefit, "
                    sqlite_insert_price += "price_per_hour_three_year_savings_hybridbenefit, price_per_month_three_year_savings_hybridbenefit, price_per_hour_spot_hybridbenefit, "
                    sqlite_insert_price += "price_per_month_spot_hybridbenefit) "
                    sqlite_insert_price += "VALUES ("
                    sqlite_insert_price += f"'{str_name}', '{str_series}', '{str_instance_name}', '{str_offer_name}', '{str_tier}', '{str_os}', '{str_category}', '{str_cores}', "
                    sqlite_insert_price += f"'{str_ram_gb}', '{str_disk_size_gb}', '{str_has_paygo}', '{str_has_spot}', '{str_is_in_preview}', '{str_is_vcpu}', '{str_is_constrained_core}', "
                    sqlite_insert_price += f"'{str_is_base_vm}', '{str_region}', '{str_region_name}', '{str_country}', '{str_country_name}', '{str_geographic}', '{str_geographic_name}', "
                    sqlite_insert_price += f"'{str_price_available}', '{str_price_hybridbenefit}', '{str_price_per_hour}', '{str_price_per_month}', '{str_price_per_hour_one_year_reserved}', "
                    sqlite_insert_price += f"'{str_price_per_month_one_year_reserved}', '{str_price_per_hour_three_year_reserved}', '{str_price_per_month_three_year_reserved}', "
                    sqlite_insert_price += f"'{str_price_per_hour_one_year_savings}', '{str_price_per_month_one_year_savings}', '{str_price_per_hour_three_year_savings}', "
                    sqlite_insert_price += f"'{str_price_per_month_three_year_savings}', '{str_price_per_hour_spot}', '{str_price_per_month_spot}', "
                    sqlite_insert_price += f"'{str_price_per_hour_hybridbenefit}', '{str_price_per_month_hybridbenefit}', '{str_price_per_hour_one_year_reserved_hybridbenefit}', "
                    sqlite_insert_price += f"'{str_price_per_month_one_year_reserved_hybridbenefit}', '{str_price_per_hour_three_year_reserved_hybridbenefit}', '{str_price_per_month_three_year_reserved_hybridbenefit}', "
                    sqlite_insert_price += f"'{str_price_per_hour_one_year_savings_hybridbenefit}', '{str_price_per_month_one_year_savings_hybridbenefit}', '{str_price_per_hour_three_year_savings_hybridbenefit}', "
                    sqlite_insert_price += f"'{str_price_per_month_three_year_savings_hybridbenefit}', '{str_price_per_hour_spot_hybridbenefit}', '{str_price_per_month_spot_hybridbenefit}'"
                    sqlite_insert_price += ")"

                    db_cursor.execute(sqlite_insert_price)

                    i += 1

                    if not is_silent_enabled:
                        bar.text = str_offer_name
                        bar()

            sqlite_prices_file.commit()

            if not is_silent_enabled:
                print(f"Exported Azure VM prices count {i} to SQLite Data Base file: {sqlite_prices_output_filename}")
            if is_logging_enabled:
                logs.append(f"OK: Exported Azure VM prices count {i} to SQLite Data Base file {sqlite_prices_output_filename}")

            currencies_prices_list_records = prices_list['currencies_list']
            currencies_prices_list_records = dict(sorted(currencies_prices_list_records.items()))     

            i = 0

            max_bar = len(currencies_prices_list_records)
            with alive_bar(max_bar, title="Export prices currencies record to SQLite Data Base", disable=is_silent_enabled) as bar:
                for currencies_price_item in currencies_prices_list_records:
                    currencies_price_item_record = currencies_prices_list_records[currencies_price_item]
                    str_currency = currencies_price_item
                    str_currency_name = currencies_price_item_record['name']
                    str_currency_info = currencies_price_item_record['info']
                    str_currency_symbol = currencies_price_item_record['symbol']
                    str_currency_conversion = str(currencies_price_item_record['conversion'])
                    str_currency_conversion_onprem = str(currencies_price_item_record['conversion_onprem'])
                    str_currency_conversion_modern = str(currencies_price_item_record['conversion_modern'])

                    sqlite_insert_price_currency = ""
                    sqlite_insert_price_currency += "INSERT INTO az_prices_currency("
                    sqlite_insert_price_currency += "currency, currency_info, currency_name, currency_symbol, currency_conversion, currency_conversion_onprem, currency_conversion_modern) "
                    sqlite_insert_price_currency += "VALUES ("
                    sqlite_insert_price_currency += f"'{str_currency}', '{str_currency_info}', '{str_currency_name}', '{str_currency_symbol}', '{str_currency_conversion}', '{str_currency_conversion_onprem}', '{str_currency_conversion_modern}'"
                    sqlite_insert_price_currency += ")"

                    db_cursor.execute(sqlite_insert_price_currency)
                    i += 1

                    if not is_silent_enabled:
                        bar.text = str_currency
                        bar()
            
            sqlite_prices_file.commit()

            if not is_silent_enabled:
                print(f"Exported Azure VM prices currencies count {i} to SQLite Data Base file: {sqlite_prices_output_filename}")
            if is_logging_enabled:
                logs.append(f"OK: Exported Azure VM prices currencies count {i} to SQLite Data Base file {sqlite_prices_output_filename}")

    except Exception as e:
        if not is_silent_enabled:
            print(f"Unable to export Azure VM prices to SQLite Data Base file {sqlite_prices_output_filename}: {e}")
        if is_logging_enabled:
            logs.append(f"ERR-FILE: Unable to export Azure VM prices to SQLite Data Base file {sqlite_prices_output_filename}: {e}")

    return logs
