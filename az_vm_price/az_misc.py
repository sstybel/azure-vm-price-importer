import os
import shutil
import requests
from datetime import datetime

def az_create_filename(filename, path=".\\temp\\", prefix_filename="temp", fileextension=".json"):
    str_timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    return f"{path}{prefix_filename}_{filename}_{str_timestamp}{fileextension}"

def az_create_pathname(pathame, path=".\\"):
    str_timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    return f"{path}{pathame}_{str_timestamp}\\"

def az_download_url_to_filename(url, output_filename):
    result = ""

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(response.text)

        result = f"OK: Downloaded {len(response.content)} bytes from \"{url}\" to \"{output_filename}\" file."
    except requests.exceptions.RequestException as e:
        result = f"ERR-URL: Download from {url} to {output_filename} failed: {e}"
    except IOError as e:
        result = f"ERR-FILE: Create file {output_filename} failed: {e}"

    return result

def az_create_directory(path=".\\temp\\", if_exists_delete=False):
    result = ""
    
    try:
        if not os.path.exists(path):
            os.makedirs(path)
            result = f"OK: Created directory {path} and is ready."
        else:
            if if_exists_delete:
                shutil.rmtree(path)
                os.makedirs(path)
                result = f"OK: Removed and recreated directory {path} and is ready."
            else:
                result = f"OK: Directory {path} exist and is ready."
    except Exception as e:
        result = f"ERR-DIR: Unable to create directory {path}: {e}"
    return result

def az_delete_directory(path=".\\temp\\", files_to_delete=None, if_exists_delete_directory=False, enable_logging=False):
    logs = []

    for file in files_to_delete:
        file_name = files_to_delete[file]
        try:
            if os.path.exists(file_name):
                os.remove(file_name)
                result = f"OK: Deleted file: {file_name}"
            else:
                result = f"ERR-FILE: File not found, cannot delete: {file_name}"
        except Exception as e:
            result = f"ERR-FILE: Error deleting file {file_name}: {e}"
        if enable_logging:
            logs.append(result)

    try:
        if if_exists_delete_directory and os.path.exists(path):
            shutil.rmtree(path)
            result = f"OK: Removed directory {path}."
        else:
            result = f"OK: The {path} directory still exists."
    except Exception as e:
        result = f"ERR-DIR: Error deleting directory {path}: {e}"
    if enable_logging:
        logs.append(result) 

    return logs

def az_print_table(table, align="", hasHeader=False, pad=2, isGrid=False):
    table = [row[:] for row in table]
    numRows, numCols = len(table), len(table[0])
    align = align.ljust(numCols, "L")
    align = ["RC".find(c) + 1 for c in align]
    widths = [max(len(row[col]) for row in table) for col in range(numCols)]
    
    if hasHeader:
        for x in range(numCols):
            table[0][x] = table[0][x].center(widths[x])
    for y in range(hasHeader,numRows):
        for x in range(numCols):
            c = table[y][x]
            table[y][x] = [c.ljust, c.rjust, c.center][align[x]](widths[x])

    P = " " * pad
    LSEP, SEP, RSEP = "│" + P, P + "│" + P, P + "│"
    lines = ["─" * (widths[col] + pad * 2) for col in range(numCols)]

    drawLine = [isGrid] * numRows
    drawLine[0] |= hasHeader
    drawLine[-1] = False
    if hasHeader or isGrid:
        gridLine = "├" + "┼".join(lines) + "┤"

    print("┌" + "┬".join(lines) + "┐")
    for y in range(numRows):
        print(LSEP + SEP.join(table[y]) + RSEP)
        if drawLine[y]:
            print(gridLine)
    print("└" + "┴".join(lines) + "┘")

def az_show_list_available_regions(az_regions={}):
    table = [
        ['Id', 'Region Name', 'Region Full Name', 'Country Name', 'Geographic Name'], 
    ]

    i = 1

    for region in az_regions:
        str_id = str(i)
        str_region = az_regions[region]['region']
        str_region_name = az_regions[region]['region_name']
        str_country_name = az_regions[region]['country_name']
        str_geographic_name = az_regions[region]['geographic_name']
        table_row = [str_id, str_region, str_region_name, str_country_name, str_geographic_name]
        table.append(table_row)
        i += 1

    az_print_table(table, align="RLLLL", hasHeader=True)