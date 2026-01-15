import xlsxwriter
from alive_progress import alive_bar

def az_export_prices_list_to_xls(xls_prices_output_filename, prices_list={}, is_silent_enabled=False, is_logging_enabled=True):
    logs = []

    char_currency = "."

    try:
        if not is_silent_enabled:
            print(f"Export Azure VM prices to Excel XLSX file: {xls_prices_output_filename}")
        if is_logging_enabled:
            logs.append(f"OK: Export Azure VM prices to Excel XLSX file {xls_prices_output_filename}")

        workbook = xlsxwriter.Workbook(xls_prices_output_filename, {'strings_to_numbers': True})

        frmHeader = workbook.add_format({'bold': True, 'bg_color': '#FFFF00', 'font_color': '#000000'})
        frmUSDcoma2 = workbook.add_format({'font_color': '#000000', 'num_format': '$# ##0.00'})
        frmUSDcoma2.set_num_format('$# ##0.00')
        frmUSDcoma4 = workbook.add_format({'font_color': '#000000', 'num_format': '$# ##0.0000'})
        frmUSDcoma4.set_num_format('$# ##0.0000')
        frmNum0 = workbook.add_format({'font_color': '#000000', 'num_format': '0'})
        frmNum0.set_num_format('0')
        frmNum1 = workbook.add_format({'font_color': '#000000', 'num_format': '0.0'})
        frmNum1.set_num_format('0.0')
        frmNum2 = workbook.add_format({'font_color': '#000000', 'num_format': '0.00'})
        frmNum2.set_num_format('0.00')
        frmDefault = workbook.add_format({'font_color': '#000000'})

        headers_prices_list = [
            "name", "series", "instance_name", "offer_name", "tier", "os", "category", "cores", "ram_gb", "disk_size_gb",
            "has_paygo", "has_spot", "is_in_preview", "is_vcpu", "is_constrained_core", "is_base_vm", "region",
            "region_name", "country", "country_name", "geographic", "geographic_name", "price_available", "price_hybridbenefit",
            "price_per_hour", "price_per_month", "price_per_hour_one_year_reserved", "price_per_month_one_year_reserved",
            "price_per_hour_three_year_reserved", "price_per_month_three_year_reserved", "price_per_hour_one_year_savings",
            "price_per_month_one_year_savings", "price_per_hour_three_year_savings", "price_per_month_three_year_savings",
            "price_per_hour_spot", "price_per_month_spot", "price_per_hour_hybridbenefit", "price_per_month_hybridbenefit",
            "price_per_hour_one_year_reserved_hybridbenefit", "price_per_month_one_year_reserved_hybridbenefit",
            "price_per_hour_three_year_reserved_hybridbenefit", "price_per_month_three_year_reserved_hybridbenefit",
            "price_per_hour_one_year_savings_hybridbenefit", "price_per_month_one_year_savings_hybridbenefit",
            "price_per_hour_three_year_savings_hybridbenefit", "price_per_month_three_year_savings_hybridbenefit",
            "price_per_hour_spot_hybridbenefit", "price_per_month_spot_hybridbenefit"
        ]
        
        headers_prices_list_currencies = [
            "currency", "currency_name", "currency_info", "currency_symbol", "currency_conversion", "currency_conversion_onprem",
            "currency_conversion_modern"
        ]

        worksheet_prices_list = workbook.add_worksheet("Azure VM Prices")

        for col_num, header in enumerate(headers_prices_list):
            worksheet_prices_list.write(0, col_num, header, frmHeader)

        prices_list_records = prices_list['prices_list']
        prices_list_records = dict(sorted(prices_list_records.items(), key=lambda item: (item[1]['cores'], item[1]['ram_gb'], item[1]['disk_size_gb'])))

        i = 0

        max_bar = len(prices_list_records)
        with alive_bar(max_bar, title="Export prices record to Excel XLSX", disable=is_silent_enabled) as bar:
            for price_item in prices_list_records:
                price_item_record = prices_list_records[price_item]
                str_name = price_item_record['name']
                str_series = price_item_record['series']
                str_instance_name = price_item_record['instance_name']
                str_offer_name = price_item
                str_tier = price_item_record['tier']
                str_os = price_item_record['os']
                str_category = price_item_record['category']
                str_cores = str(price_item_record['cores']).replace(".", char_currency)
                str_ram_gb = str(price_item_record['ram_gb']).replace(".", char_currency)
                str_disk_size_gb = str(price_item_record['disk_size_gb']).replace(".", char_currency)
                str_has_paygo = str(price_item_record['has_paygo']).replace(".", char_currency)
                str_has_spot = str(price_item_record['has_spot']).replace(".", char_currency)
                str_is_in_preview = str(price_item_record['is_in_preview']).replace(".", char_currency)
                str_is_vcpu = str(price_item_record['is_vcpu']).replace(".", char_currency)
                str_is_constrained_core = str(price_item_record['is_constrained_core']).replace(".", char_currency)
                str_is_base_vm = str(price_item_record['is_base_vm']).replace(".", char_currency)
                str_region = price_item_record['region']
                str_region_name = price_item_record['region_name']
                str_country = price_item_record['country']
                str_country_name = price_item_record['country_name']
                str_geographic = price_item_record['geographic']
                str_geographic_name = price_item_record['geographic_name']
                str_price_available = str(price_item_record['price_available'])
                str_price_hybridbenefit = str(price_item_record['price_hybridbenefit'])
                str_price_per_hour = str(price_item_record['price_per_hour']).replace(".", char_currency)
                str_price_per_month = str(price_item_record['price_per_month']).replace(".", char_currency)
                str_price_per_hour_one_year_reserved = str(price_item_record['price_per_hour_one_year_reserved']).replace(".", char_currency)
                str_price_per_month_one_year_reserved = str(price_item_record['price_per_month_one_year_reserved']).replace(".", char_currency)
                str_price_per_hour_three_year_reserved = str(price_item_record['price_per_hour_three_year_reserved']).replace(".", char_currency)
                str_price_per_month_three_year_reserved = str(price_item_record['price_per_month_three_year_reserved']).replace(".", char_currency)
                str_price_per_hour_one_year_savings = str(price_item_record['price_per_hour_one_year_savings']).replace(".", char_currency)
                str_price_per_month_one_year_savings = str(price_item_record['price_per_month_one_year_savings']).replace(".", char_currency)
                str_price_per_hour_three_year_savings = str(price_item_record['price_per_hour_three_year_savings']).replace(".", char_currency)
                str_price_per_month_three_year_savings = str(price_item_record['price_per_month_three_year_savings']).replace(".", char_currency)
                str_price_per_hour_spot = str(price_item_record['price_per_hour_spot']).replace(".", char_currency)
                str_price_per_month_spot = str(price_item_record['price_per_month_spot']).replace(".", char_currency)
                str_price_per_hour_hybridbenefit = str(price_item_record['price_per_hour_hybridbenefit']).replace(".", char_currency)
                str_price_per_month_hybridbenefit = str(price_item_record['price_per_month_hybridbenefit']).replace(".", char_currency)
                str_price_per_hour_one_year_reserved_hybridbenefit = str(price_item_record['price_per_hour_one_year_reserved_hybridbenefit']).replace(".", char_currency)
                str_price_per_month_one_year_reserved_hybridbenefit = str(price_item_record['price_per_month_one_year_reserved_hybridbenefit']).replace(".", char_currency)
                str_price_per_hour_three_year_reserved_hybridbenefit = str(price_item_record['price_per_hour_three_year_reserved_hybridbenefit']).replace(".", char_currency)
                str_price_per_month_three_year_reserved_hybridbenefit = str(price_item_record['price_per_month_three_year_reserved_hybridbenefit']).replace(".", char_currency)
                str_price_per_hour_one_year_savings_hybridbenefit = str(price_item_record['price_per_hour_one_year_savings_hybridbenefit']).replace(".", char_currency)
                str_price_per_month_one_year_savings_hybridbenefit = str(price_item_record['price_per_month_one_year_savings_hybridbenefit']).replace(".", char_currency)
                str_price_per_hour_three_year_savings_hybridbenefit = str(price_item_record['price_per_hour_three_year_savings_hybridbenefit']).replace(".", char_currency)
                str_price_per_month_three_year_savings_hybridbenefit = str(price_item_record['price_per_month_three_year_savings_hybridbenefit']).replace(".", char_currency)
                str_price_per_hour_spot_hybridbenefit = str(price_item_record['price_per_hour_spot_hybridbenefit']).replace(".", char_currency)
                str_price_per_month_spot_hybridbenefit = str(price_item_record['price_per_month_spot_hybridbenefit']).replace(".", char_currency)

                worksheet_prices_list.write(i + 1, 0, str_name, frmDefault)
                worksheet_prices_list.write(i + 1, 1, str_series, frmDefault)
                worksheet_prices_list.write(i + 1, 2, str_instance_name, frmDefault)
                worksheet_prices_list.write(i + 1, 3, str_offer_name, frmDefault)
                worksheet_prices_list.write(i + 1, 4, str_tier, frmDefault)
                worksheet_prices_list.write(i + 1, 5, str_os, frmDefault)
                worksheet_prices_list.write(i + 1, 6, str_category, frmDefault)
                worksheet_prices_list.write(i + 1, 7, str_cores, frmNum0)
                worksheet_prices_list.write(i + 1, 8, str_ram_gb, frmNum1)
                worksheet_prices_list.write(i + 1, 9, str_disk_size_gb, frmNum0)
                worksheet_prices_list.write(i + 1, 10, str_has_paygo, frmDefault)
                worksheet_prices_list.write(i + 1, 11, str_has_spot, frmDefault)
                worksheet_prices_list.write(i + 1, 12, str_is_in_preview, frmDefault)
                worksheet_prices_list.write(i + 1, 13, str_is_vcpu, frmDefault)
                worksheet_prices_list.write(i + 1, 14, str_is_constrained_core, frmDefault)
                worksheet_prices_list.write(i + 1, 15, str_is_base_vm, frmDefault)
                worksheet_prices_list.write(i + 1, 16, str_region, frmDefault)
                worksheet_prices_list.write(i + 1, 17, str_region_name, frmDefault)
                worksheet_prices_list.write(i + 1, 18, str_country, frmDefault)
                worksheet_prices_list.write(i + 1, 19, str_country_name, frmDefault)
                worksheet_prices_list.write(i + 1, 20, str_geographic, frmDefault)
                worksheet_prices_list.write(i + 1, 21, str_geographic_name, frmDefault)
                worksheet_prices_list.write(i + 1, 22, str_price_available, frmDefault)
                worksheet_prices_list.write(i + 1, 23, str_price_hybridbenefit, frmDefault)
                worksheet_prices_list.write(i + 1, 24, str_price_per_hour, frmUSDcoma4)
                worksheet_prices_list.write(i + 1, 25, str_price_per_month, frmUSDcoma2)
                worksheet_prices_list.write(i + 1, 26, str_price_per_hour_one_year_reserved, frmUSDcoma4)
                worksheet_prices_list.write(i + 1, 27, str_price_per_month_one_year_reserved, frmUSDcoma2)
                worksheet_prices_list.write(i + 1, 28, str_price_per_hour_three_year_reserved, frmUSDcoma4)
                worksheet_prices_list.write(i + 1, 29, str_price_per_month_three_year_reserved, frmUSDcoma2)
                worksheet_prices_list.write(i + 1, 30, str_price_per_hour_one_year_savings, frmUSDcoma4)
                worksheet_prices_list.write(i + 1, 31, str_price_per_month_one_year_savings, frmUSDcoma2)
                worksheet_prices_list.write(i + 1, 32, str_price_per_hour_three_year_savings, frmUSDcoma4)
                worksheet_prices_list.write(i + 1, 33, str_price_per_month_three_year_savings, frmUSDcoma2)
                worksheet_prices_list.write(i + 1, 34, str_price_per_hour_spot, frmUSDcoma4)
                worksheet_prices_list.write(i + 1, 35, str_price_per_month_spot, frmUSDcoma2)
                worksheet_prices_list.write(i + 1, 36, str_price_per_hour_hybridbenefit, frmUSDcoma4)
                worksheet_prices_list.write(i + 1, 37, str_price_per_month_hybridbenefit, frmUSDcoma2)
                worksheet_prices_list.write(i + 1, 38, str_price_per_hour_one_year_reserved_hybridbenefit, frmUSDcoma4)
                worksheet_prices_list.write(i + 1, 39, str_price_per_month_one_year_reserved_hybridbenefit, frmUSDcoma2)
                worksheet_prices_list.write(i + 1, 40, str_price_per_hour_three_year_reserved_hybridbenefit, frmUSDcoma4)
                worksheet_prices_list.write(i + 1, 41, str_price_per_month_three_year_reserved_hybridbenefit, frmUSDcoma2)
                worksheet_prices_list.write(i + 1, 42, str_price_per_hour_one_year_savings_hybridbenefit, frmUSDcoma4)
                worksheet_prices_list.write(i + 1, 43, str_price_per_month_one_year_savings_hybridbenefit, frmUSDcoma2)
                worksheet_prices_list.write(i + 1, 44, str_price_per_hour_three_year_savings_hybridbenefit, frmUSDcoma4)
                worksheet_prices_list.write(i + 1, 45, str_price_per_month_three_year_savings_hybridbenefit, frmUSDcoma2)
                worksheet_prices_list.write(i + 1, 46, str_price_per_hour_spot_hybridbenefit, frmUSDcoma4)
                worksheet_prices_list.write(i + 1, 47, str_price_per_month_spot_hybridbenefit, frmUSDcoma2)                

                i += 1

                if not is_silent_enabled:
                    bar.text = str_offer_name
                    bar()

        nrow = i
        ncol = len(headers_prices_list) - 1
        worksheet_prices_list.autofilter(0, 0, nrow, ncol)
        worksheet_prices_list.autofit()
        worksheet_prices_list.freeze_panes(1, 0)

        worksheet_prices_list_currencies = workbook.add_worksheet("Azure Currencies")

        for col_num, header in enumerate(headers_prices_list_currencies):
            worksheet_prices_list_currencies.write(0, col_num, header, frmHeader)
        
        prices_list_currencies_records = prices_list['currencies_list']
        prices_list_currencies_records = dict(sorted(prices_list_currencies_records.items()))

        j = 0

        max_bar = len(prices_list_currencies_records)
        with alive_bar(max_bar, title="Export prices currencies record to Excel XLSX", disable=is_silent_enabled) as bar:
            for currency_item in prices_list_currencies_records:
                currency_item_record = prices_list_currencies_records[currency_item]
                str_currency = currency_item
                str_currency_name = currency_item_record['name']
                str_currency_info = currency_item_record['info']
                str_currency_symbol = currency_item_record['symbol']
                str_currency_conversion = str(currency_item_record['conversion']).replace(".", char_currency)
                str_currency_conversion_onprem = str(currency_item_record['conversion_onprem']).replace(".", char_currency)
                str_currency_conversion_modern = str(currency_item_record['conversion_modern']).replace(".", char_currency)

                worksheet_prices_list_currencies.write(j + 1, 0, str_currency, frmDefault)
                worksheet_prices_list_currencies.write(j + 1, 1, str_currency_name, frmDefault)
                worksheet_prices_list_currencies.write(j + 1, 2, str_currency_info, frmDefault)
                worksheet_prices_list_currencies.write(j + 1, 3, str_currency_symbol, frmDefault)
                worksheet_prices_list_currencies.write(j + 1, 4, str_currency_conversion, frmUSDcoma4)
                worksheet_prices_list_currencies.write(j + 1, 5, str_currency_conversion_onprem, frmUSDcoma4)
                worksheet_prices_list_currencies.write(j + 1, 6, str_currency_conversion_modern, frmUSDcoma4)

                j += 1
                
                if not is_silent_enabled:
                    bar.text = str_currency
                    bar()
        
        nrow = j
        ncol = len(headers_prices_list_currencies) - 1
        worksheet_prices_list_currencies.autofilter(0, 0, nrow, ncol)
        worksheet_prices_list_currencies.autofit()
        worksheet_prices_list_currencies.freeze_panes(1, 0)

        workbook.close()
    except Exception as ex:
        if not is_silent_enabled:
            print(f"Unable to export Azure VM prices to Excel XLSX file {xls_prices_output_filename}: {ex}")
        if is_logging_enabled:
            logs.append(f"ERR-FILE: Unable to export Azure VM prices to Excel XLSX file {xls_prices_output_filename}: {ex}")

    if not is_silent_enabled:
        print(f"Exported Azure VM prices count {i} to Excel XLSX file: {xls_prices_output_filename}")
    if is_logging_enabled:
        logs.append(f"OK: Exported Azure VM prices count {i} to Excel XLSX file {xls_prices_output_filename}")

    if not is_silent_enabled:
        print(f"Exported Azure prices currencies count {j} to Excel XLSX file: {xls_prices_output_filename}")
    if is_logging_enabled:
        logs.append(f"OK: Exported Azure prices currencies count {j} to Excel XLSX file {xls_prices_output_filename}")

    return logs
