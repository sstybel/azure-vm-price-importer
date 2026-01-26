import os
import sys
import argparse
from datetime import datetime

from az_vm_price import az_oss
from az_vm_price import az_category
from az_vm_price import az_regions
from az_vm_price import az_download
from az_vm_price import az_export_json
from az_vm_price import az_export_csv
from az_vm_price import az_export_xls
from az_vm_price import az_export_sqlite
from az_vm_price import az_export_sql
from az_vm_price import az_pack
from az_vm_price import az_prices
from az_vm_price import az_infos
from az_vm_price import az_logs
from az_vm_price import az_misc

str_version = "1.00"
str_app_name ="Azure VM Prices Importer - ver. " + str_version
str_author = "Copyright (c) 2025 - 2026 by Sebastian Stybel, www.BONO.Edu.PL"

pathname = "az_price_data"
path = ".\\"

file_currencies = "azure_currencies"
file_regions = "azure_regions" 
file_resources = "azure_resources"
file_oss = "azure_oss"
file_metadata = "azure_metadata"
file_sku_details = "azure_sku_details" # file_sku_details + "_{os}"
file_sku_calculator = "azure_sku_calculator" # file_sku_calculator + "_{region}"
file_sku_region = "azure_sku_region" # file_sku_region + "_{os}_{region}"

azure_oss = {}
azure_regions = {}
azure_vm_series = {}
azure_initial_data = {}
azure_detail_price_data = {}
azure_regions_prices_data = {}
azure_calculator_price_data = {}
azure_config_pack = {}

log_filename = az_misc.az_create_filename("azure_vm_price_importer", path=".\\", prefix_filename="logs", fileextension=".log")

is_unknown_region = False

is_logging_enabled = False
is_silent_enabled = False

is_delete_files_enabled = False
is_delete_directory_enabled = False

is_load_pack = False
is_save_pack = False

is_import_json = False
is_export_json = False

export_format = ""

is_export_csv = False

is_export_xls = False

is_export_sqlite = False
is_overwrite_sqlite = False
is_add_currency_sqlite = False

is_export_sql = False
is_add_currency_sql = False
sql_notation = ""

json_prices_input_filename = ""
json_prices_output_filename = ""

csv_prices_output_filename = ""
csv_prices_currencies_output_filename = ""
xlsx_prices_output_filename = ""
sqlite_prices_outout_filename = ""
sql_prices_outout_filename = ""

if __name__ == "__main__":
    is_cmd_ok = False

    parser = argparse.ArgumentParser(add_help=False)
    subparser = parser.add_subparsers(dest="command", title="Commands")
    
    sp_cmd_download = subparser.add_parser("download", help="Download Azure VM prices for specific Azure region or All regions to AZPX file.", add_help=False)
    sp_cmd_download.add_argument("--path", "-p", default=".\\", help="Path to the output file in AZPX format with downloaded data from Azure regarding price lists for a given region or all available regions.", required=(not('--help' in sys.argv) and not('-h' in sys.argv)))
    sp_cmd_download.add_argument("--region", "-r", default="all", help="Name of the region or value 'all' if price lists of all regions are to be downloaded.", required=(not('--help' in sys.argv) and not('-h' in sys.argv)))
    sp_cmd_download.add_argument("--silent-mode", "-s", choices=['yes', 'no'], default="no", help="Turn silent mode on or off.")
    sp_cmd_download.add_argument("--logs", "-l", choices=['yes', 'no'], default="no", help=f"Turning logging mode on or off to file {log_filename}.")
    sp_cmd_download.add_argument("--help", "-h", help="Show this help message and exit.", action="store_true", )

    sp_cmd_save = subparser.add_parser("save", help="Save the parsed Azure VM pricing structure from the AZPX file for a specific Azure region to a JSON file.", add_help=False)
    sp_cmd_save.add_argument("--azpx-load", "-a", help="The name of the AZPX file with downloaded Azure VM price lists for the region being processed or from all regions.", required=(not('--help' in sys.argv) and not('-h' in sys.argv)))
    sp_cmd_save.add_argument("--region", "-r", help="The name of the region for which the Azure VM price list will be processed to JSON format.", required=(not('--help' in sys.argv) and not('-h' in sys.argv)))
    sp_cmd_save.add_argument("--path", "-p", help="Path location of the JSON file with the resulting Azure VM pricing.", required=(not('--help' in sys.argv) and not('-h' in sys.argv)))
    sp_cmd_save.add_argument("--json", "-j", help="The name of the JSON file or 'auto' for an automatically generated name containing the Azure VM pricing.", required=(not('--help' in sys.argv) and not('-h' in sys.argv)))
    sp_cmd_save.add_argument("--silent-mode", "-s", choices=['yes', 'no'], default="no", help="Turn silent mode on or off.")
    sp_cmd_save.add_argument("--logs", "-l", choices=['yes', 'no'], default="no", help=f"Turning logging mode on or off to file {log_filename}.")
    sp_cmd_save.add_argument("--help", "-h", help="Show this help message and exit.", action="store_true")

    sp_cmd_export = subparser.add_parser("export", help="Export Azure VM pricing data for a specific Azure region to the following formats: CSV, Excel (XLSX), SQLite database, SQL notation for databases (SQLite, MySQL, PostgreSQL).", add_help=False)
    sp_cmd_export.add_argument("--json", "-j", help="The name of the JSON file with processed Azure VM pricing for a single region selected.", required=(not('--help' in sys.argv) and not('-h' in sys.argv)))
    sp_cmd_export.add_argument("--path", "-p", help="Path location of the exported file with the resulting Azure VM prices in the following formats: CSV, Excel (XLSX), SQLite database, SQL notation for databases (SQLite, MySQL, PostgreSQL).", required=(not('--help' in sys.argv) and not('-h' in sys.argv)))
    sp_cmd_export.add_argument("--format", "-f", help="Select one of the exported data formats: CSV, Excel (XLSX), SQLite, SQL notation for SQLite, MySQL and PostgreSQL databases.", choices=['csv', 'xlsx', 'sqlite', 'sql-sqlite', 'sql-mysql', 'sql-postgresql'], required=(not('--help' in sys.argv) and not('-h' in sys.argv)))
    sp_cmd_export.add_argument("--export", "-e", help="The name of the resulting file for the exported data, or 'auto' for the automatically generated name containing the Azure VM pricing.", required=(not('--help' in sys.argv) and not('-h' in sys.argv)))
    sp_cmd_export.add_argument("--export-currency", "-c", help="The name of the resulting CSV file of the exported currency data, or 'auto' for an automatically generated name that includes the Azure currency converter.", required=(not('--help' in sys.argv) and not('-h' in sys.argv) and ('csv' in sys.argv)))
    sp_cmd_export.add_argument("--delimiter", "-d", help="Column delimiter for CSV format. Default value is  ' ; ' (semicolon).", default=";")
    sp_cmd_export.add_argument("--numeric", "-n", help="Numeric separator character. Default value is  ' , ' (comma).", default=",")
    sp_cmd_export.add_argument("--overwrite-sqlite", "-o", choices=['yes', 'no'], default="no", help="Overwrite SQLite database.")
    sp_cmd_export.add_argument("--add-currency", "-a", choices=['yes', 'no'], default="no", help="Add data on currency conversion to SQLite database or SQL notation for SQLite, MySQL and PostgreSQL databases.")
    sp_cmd_export.add_argument("--silent-mode", "-s", choices=['yes', 'no'], default="no", help="Turn silent mode on or off.")
    sp_cmd_export.add_argument("--logs", "-l", choices=['yes', 'no'], default="no", help=f"Turning logging mode on or off to file {log_filename}.")
    sp_cmd_export.add_argument("--help", "-h", help="Show this help message and exit.", action="store_true")

    sp_cmd_regions = subparser.add_parser("available-regions", help="Show list of all available Azure regions.", description="Show list of all available Azure regions.", add_help=False)

    sp_cmd_version = subparser.add_parser("version", help="Show information about the application version.", description="Show information about the application version.", add_help=False)
    
    sp_cmd_help = subparser.add_parser("help", help="Show this help message and exit.", description="Show this help message and exit.", add_help=False)

    args = parser.parse_args()
    
    command = str(args.command).lower()
    if (command == "download"):
        if args.help:
            sp_cmd_download.print_help()
        else:
            is_cmd_ok = True
            if args.silent_mode:
                is_silent_enabled = (str(args.silent_mode).lower() == 'yes')
            if args.logs:
                is_logging_enabled = (str(args.logs).lower() == 'yes')
            if args.region:
                arg_region = str(args.region).lower()
                azure_prices_of_region = arg_region
            if args.path:
                arg_path = os.path.dirname(str(args.path) + "\\") + "\\"
                path_base = arg_path.strip()
                az_misc.az_create_directory(arg_path, False)
                path = az_misc.az_create_pathname(pathname, path=arg_path)
            is_load_pack = False
            is_save_pack = True
            is_import_json = False
            is_export_json = False
            is_delete_files_enabled = True
            is_delete_directory_enabled = True
    elif (command == "save"):
        if args.help:
            sp_cmd_save.print_help()
        else:
            is_cmd_ok = True
            if args.silent_mode:
                is_silent_enabled = (str(args.silent_mode).lower() == 'yes')
            if args.logs:
                is_logging_enabled = (str(args.logs).lower() == 'yes')
            if args.azpx_load:
                arg_azpx = str(args.azpx_load).lower()
                azpx_input_filename = arg_azpx
            if args.region:
                arg_region = str(args.region).lower()
                azure_prices_of_region = arg_region
            if args.path:
                arg_path = os.path.dirname(str(args.path) + "\\") + "\\"
                path_base = arg_path.strip()
                az_misc.az_create_directory(arg_path, False)
                path = arg_path.strip()
            if args.json:
                arg_json = str(args.json).lower().strip()
                if arg_json == 'auto':
                    json_auto_filename = az_misc.az_create_filename(filename="vm_prices_" + azure_prices_of_region, path=path, prefix_filename="az", fileextension=".json")
                    json_prices_output_filename = json_auto_filename
                else:
                    json_prices_output_filename = path + arg_json
            is_load_pack = True
            is_save_pack = False
            is_import_json = False
            is_export_json = True
            is_delete_files_enabled = True
            is_delete_directory_enabled = True
    elif (command == "export"):
        if args.help:
            sp_cmd_export.print_help()
        else:
            is_cmd_ok = True
            if args.silent_mode:
                is_silent_enabled = (str(args.silent_mode).lower() == 'yes')
            if args.logs:
                is_logging_enabled = (str(args.logs).lower() == 'yes')
            if args.json:
                arg_json = str(args.json).lower()
                json_prices_input_filename = arg_json
            if args.path:
                arg_path = os.path.dirname(str(args.path) + "\\") + "\\"
                path_base = arg_path.strip()
                az_misc.az_create_directory(arg_path, False)
                path = arg_path.strip()
            if args.format:
                arg_format = str(args.format).lower()
                arr_format = arg_format.split("-")
                export_format = arr_format[0]
                if len(arr_format) > 1:
                    sql_notation = arr_format[1]
            if args.export:
                arg_export = str(args.export).lower()
                if arg_export == 'auto':
                    csv_export_auto_filename = az_misc.az_create_filename(filename="vm_prices_###region###", path=path, prefix_filename="az", fileextension=".csv")
                    csv_prices_output_filename = csv_export_auto_filename
                    xlsx_export_auto_filename = az_misc.az_create_filename(filename="vm_prices_###region###", path=path, prefix_filename="az", fileextension=".xlsx")
                    xlsx_prices_output_filename = xlsx_export_auto_filename
                    sqlite_export_auto_filename = az_misc.az_create_filename(filename="vm_prices_###region###", path=path, prefix_filename="az", fileextension=".sqlite")
                    sqlite_prices_outout_filename = sqlite_export_auto_filename
                    sql_export_auto_filename = az_misc.az_create_filename(filename="vm_prices_###region###_" +sql_notation, path=path, prefix_filename="az", fileextension=".sql")
                    sql_prices_outout_filename = sql_export_auto_filename
                else:
                    csv_prices_output_filename = path + arg_export
                    xlsx_prices_output_filename = csv_prices_output_filename
                    sqlite_prices_outout_filename = csv_prices_output_filename
                    sql_prices_outout_filename = csv_prices_output_filename
            if args.export_currency:
                arg_currency_export = str(args.export_currency).lower()
                if arg_currency_export == 'auto':
                    csv_currency_export_auto_filename = az_misc.az_create_filename(filename="vm_prices_currencies_###region###", path=path, prefix_filename="az", fileextension=".csv")
                    csv_prices_currencies_output_filename = csv_currency_export_auto_filename
                else:
                    csv_prices_currencies_output_filename = path + arg_currency_export
            if args.delimiter:
                arg_delimiter = str(args.delimiter).lower()
            else:
                arg_delimiter = ";"
            if args.numeric:
                arg_numeric = str(args.numeric).lower()
            else:
                arg_numeric = ","
            if args.overwrite_sqlite:
                arg_overwrite_sqlite = str(args.overwrite_sqlite).lower()
                is_overwrite_sqlite =  (arg_overwrite_sqlite == 'yes')
            else:
                is_overwrite_sqlite = True
            if args.add_currency:
                arg_add_currency = str(args.add_currency).lower()
                is_add_currency_sqlite =  (arg_add_currency == 'yes')
                is_add_currency_sql = is_add_currency_sqlite
            else:
                is_add_currency_sqlite = True
                is_add_currency_sql = True

            is_import_json = True
            if  export_format == "csv":
                is_export_csv = True
            elif export_format == "xlsx":
                is_export_xls = True
            elif export_format == "sqlite":
                is_export_sqlite = True
            elif export_format == "sql":
                is_export_sql = True
    elif (command == "available-regions"):
        path = az_misc.az_create_pathname(pathname, path=path)
        logs, azure_initial_data = az_download.az_download_initial_data(path=path, file_currencies=file_currencies, file_regions=file_regions, file_resources=file_resources, file_oss=file_oss, file_metadata=file_metadata, enable_silent=True, enable_logging=False)
        logs, azure_regions = az_regions.az_list_regions(azure_initial_data['regions'], enable_silent=True, enable_logging=False)
        az_misc.az_show_list_available_regions(azure_regions)
        files_to_delete = azure_initial_data
        logs = az_misc.az_delete_directory(path, files_to_delete, if_exists_delete_directory=True, enable_logging=False)
    elif (command == "version"):
        az_infos.print_app_title(str_app_name, str_author, False)
    elif (command == "help"):
        parser.print_help()
        print("")
        sp_cmd_download.print_help()
        print("")
        sp_cmd_save.print_help()
        print("")
        sp_cmd_export.print_help()
        print("")
        sp_cmd_regions.print_help()
        print("")
        sp_cmd_version.print_help()
        print("")
        sp_cmd_help.print_help()
    else:
        parser.print_usage()

    if is_cmd_ok:
        start_process = datetime.now()

        az_infos.print_app_title(str_app_name, str_author, is_silent_enabled)
        if is_logging_enabled:
            az_infos.print_start_logs(log_filename, is_silent_enabled)

        az_logs.log_create(log_filename, is_logging_enabled)
        az_logs.log_app_title(log_filename, str_app_name, str_author, is_logging_enabled)
        az_logs.log_start_logs(log_filename, is_logging_enabled)

        if not is_import_json:
            if not is_load_pack:
                logs, azure_initial_data = az_download.az_download_initial_data(path=path, file_currencies=file_currencies, file_regions=file_regions, file_resources=file_resources, file_oss=file_oss, file_metadata=file_metadata, enable_silent=is_silent_enabled, enable_logging=is_logging_enabled)
                az_logs.log_messages(log_filename, logs, is_logging_enabled)
            else:
                logs, path, azure_prices, azure_initial_data, azure_detail_price_data, azure_regions_prices_data, azure_calculator_price_data, azure_config_pack = az_pack.az_load_config_pack(path=path, pack_filename=azpx_input_filename, enable_silent=is_silent_enabled, enable_logging=is_logging_enabled)
                az_logs.log_messages(log_filename, logs, is_logging_enabled)        

            logs, azure_regions = az_regions.az_list_regions(path_base + azure_initial_data['regions'], is_silent_enabled, is_logging_enabled)
            az_logs.log_messages(log_filename, logs, is_logging_enabled)

            if (not is_load_pack) and (not((azure_prices_of_region in azure_regions) or (azure_prices_of_region == 'all'))):
                if not is_silent_enabled:
                    print(f"An unknown Azure region ({azure_prices_of_region}) was specified.")
                if is_logging_enabled:
                    logs.append(f"ERR: An unknown Azure region ({azure_prices_of_region}) was specified.")
                az_logs.log_messages(log_filename, logs, is_logging_enabled)
                is_unknown_region = True
            
            if (not is_import_json) and (is_export_json) and (is_load_pack) and (not(azure_prices_of_region in azure_regions)):
                if not is_silent_enabled:
                    print(f"An unknown Azure region ({azure_prices_of_region}) was specified.")
                if is_logging_enabled:
                    logs.append(f"ERR: An unknown Azure region ({azure_prices_of_region}) was specified.")
                az_logs.log_messages(log_filename, logs, is_logging_enabled)
                is_unknown_region = True

            if not is_unknown_region:
                logs, azure_oss = az_oss.az_list_oss(path_base + azure_initial_data['oss'], is_silent_enabled, is_logging_enabled)
                az_logs.log_messages(log_filename, logs, is_logging_enabled)
                
                logs, azure_vm_series = az_oss.az_list_vm_series(path_base + azure_initial_data['oss'], is_silent_enabled, is_logging_enabled)
                az_logs.log_messages(log_filename, logs, is_logging_enabled)

                logs, azure_categories = az_category.az_list_categories(path_base + azure_initial_data['metadata'], is_silent_enabled, is_logging_enabled)
                az_logs.log_messages(log_filename, logs, is_logging_enabled)

                if not is_load_pack:
                    logs, azure_detail_price_data, azure_regions_prices_data = az_download.az_download_regions_prices_data(path=path, file_sku_details=file_sku_details, file_sku_region=file_sku_region, az_region=azure_prices_of_region, az_oss=azure_oss, az_regions=azure_regions, enable_silent=is_silent_enabled, enable_logging=is_logging_enabled)
                    az_logs.log_messages(log_filename, logs, is_logging_enabled)

                if not is_load_pack:
                    logs, azure_calculator_price_data = az_download.az_download_calculator_prices_data(path=path, file_sku_calculator=file_sku_calculator, az_region=azure_prices_of_region, az_regions=azure_regions, enable_silent=is_silent_enabled, enable_logging=is_logging_enabled)
                    az_logs.log_messages(log_filename, logs, is_logging_enabled)

                if not is_load_pack and is_save_pack:
                    logs, azure_config_pack = az_pack.az_save_config_pack(path=path, az_region=azure_prices_of_region, initial_data=azure_initial_data, detail_price_data=azure_detail_price_data, regions_prices_data=azure_regions_prices_data, calculator_price_data=azure_calculator_price_data, enable_silent=is_silent_enabled, enable_logging=is_logging_enabled)
                    az_logs.log_messages(log_filename, logs, is_logging_enabled)

                if is_export_json:
                    logs, azure_prices_list = az_prices.az_prices_list_for_region(path=path_base, az_region=azure_prices_of_region, az_regions=azure_regions, initial_data=azure_initial_data, detail_price_data=azure_detail_price_data, regions_prices_data=azure_regions_prices_data, calculator_price_data=azure_calculator_price_data, categories=azure_categories, is_silent_enabled=is_silent_enabled, is_logging_enabled=is_logging_enabled)
                    az_logs.log_messages(log_filename, logs, is_logging_enabled)

                    logs = az_export_json.az_export_prices_list_to_json(json_prices_output_filename, prices_list=azure_prices_list, is_silent_enabled=is_silent_enabled, is_logging_enabled=is_logging_enabled)
                    az_logs.log_messages(log_filename, logs, is_logging_enabled)
        else:
            if is_import_json:
                logs, azure_prices_list = az_export_json.az_import_prices_list_from_json(json_prices_input_filename, is_silent_enabled=is_silent_enabled, is_logging_enabled=is_logging_enabled)
                az_logs.log_messages(log_filename, logs, is_logging_enabled) 

                azure_prices_of_region = azure_prices_list["region"]

                csv_prices_output_filename = csv_prices_output_filename.replace("###region###", azure_prices_of_region)
                csv_prices_currencies_output_filename = csv_prices_currencies_output_filename.replace("###region###", azure_prices_of_region)
                xlsx_prices_output_filename = xlsx_prices_output_filename.replace("###region###", azure_prices_of_region)
                sqlite_prices_outout_filename = sqlite_prices_outout_filename.replace("###region###", azure_prices_of_region)
                sql_prices_outout_filename = sql_prices_outout_filename.replace("###region###", azure_prices_of_region)

            if is_export_csv:
                logs = az_export_csv.az_export_prices_list_to_csv(csv_prices_output_filename, csv_prices_currencies_output_filename, delimiter=arg_delimiter, numeric=arg_numeric, prices_list=azure_prices_list, is_silent_enabled=is_silent_enabled, is_logging_enabled=is_logging_enabled)
                az_logs.log_messages(log_filename, logs, is_logging_enabled)
                
            if is_export_xls:
                logs = az_export_xls.az_export_prices_list_to_xls(xlsx_prices_output_filename, delimiter=arg_delimiter, numeric=arg_numeric, prices_list=azure_prices_list, is_silent_enabled=is_silent_enabled, is_logging_enabled=is_logging_enabled)
                az_logs.log_messages(log_filename, logs, is_logging_enabled)

            if is_export_sqlite:
                logs = az_export_sqlite.az_export_prices_list_to_sqlite(sqlite_prices_outout_filename, prices_list=azure_prices_list, is_overwrite_sqlite=is_overwrite_sqlite, is_add_currency_sqlite=is_add_currency_sqlite, is_silent_enabled=is_silent_enabled, is_logging_enabled=is_logging_enabled)
                az_logs.log_messages(log_filename, logs, is_logging_enabled)

            if is_export_sql:
                logs = az_export_sql.az_export_prices_list_to_sql(sql_prices_outout_filename, sql_notation=sql_notation, prices_list=azure_prices_list, is_add_currency_sql=is_add_currency_sql, is_silent_enabled=is_silent_enabled, is_logging_enabled=is_logging_enabled)
                az_logs.log_messages(log_filename, logs, is_logging_enabled)

        if not is_import_json and is_delete_files_enabled:
            files_to_delete = azure_initial_data | azure_detail_price_data | azure_regions_prices_data | azure_calculator_price_data | azure_config_pack
            logs = az_misc.az_delete_directory(path, files_to_delete, is_delete_directory_enabled, is_logging_enabled)
            az_infos.print_cleanup_files(path=path, count_files=len(files_to_delete), delete_directory=is_delete_directory_enabled, is_silent_enabled=is_silent_enabled)
            az_logs.log_cleanup_files(log_filename, path=path, count_files=len(files_to_delete), delete_directory=is_delete_directory_enabled, is_logging_enabled=is_logging_enabled)
            az_logs.log_messages(log_filename, logs, is_logging_enabled)

        if is_logging_enabled:
            az_infos.print_stop_logs(log_filename, is_silent_enabled)
        az_logs.log_stop_logs(log_filename, is_logging_enabled) 

        end_process = datetime.now()
        delta_process = end_process - start_process 

        az_infos.print_end_process(time_process=delta_process, is_silent_enabled=is_silent_enabled)
        az_logs.log_end_process(time_process=delta_process, log_filename=log_filename, is_logging_enabled=is_logging_enabled)
