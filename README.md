# Azure VM (Virtual Machine) Price Importer

This program allows you to download VM price lists from a specific region or all Azure regions (*currently 59 as of January 2026*).

The downloaded price list for a specific Azure region can then be processed and saved to an exchange file in `JSON` format. 

In addition, the price list for a selected Azure region can be exported from the `JSON` exchange file to several different formats, including `CSV`, `Excel` (`XLSX`), `SQLite`, `SQL` notation for `SQLite`, `MySQL`, and `PostgreSQL` databases.

This application therefore works in three (3) modes:
1. **Downloading** price list data for a specified single region or all Azure regions. The downloaded price lists are saved to a data package file in **AZPX** (**AZ**ure **P**rices packbo**X**) format.
2.	**Saving** processed price list data for a specific Azure region to an exchange file in JSON format, based on data previously downloaded in mode one ***(1)*** – **AZPX** package file.
3.	**Exporting** previously saved processed price lists in `JSON` format from mode two ***(2)*** to another format, including: `CSV`, `Excel` (`XLSX`), `SQLite`, `SQL` notation for `SQLite`, `MySQL`, and `PostgreSQL` databases.

Additionally, the application is able to list all currently available Azure regions (*currently 59 – as of January 2026*).

## Syntax of the `azure-vm-price-importer.exe` for all commands:

**Usage:** `azure-vm-price-importer.exe` {`download`, `save`, `export`, `available-regions`, `version`, `help`} ...

**Commands:**

* `download` - Download Azure VM prices for specific Azure region or All regions to AZPX file.
* `save` - Save the parsed Azure VM pricing structure from the AZPX file for a specific Azure region to a JSON file.

* `export` - Export Azure VM pricing data for a specific Azure region to the following formats: CSV, Excel (XLSX), SQLite database, SQL notation for databases (SQLite, MySQL, PostgreSQL).
* `available-regions` - Show list of all available Azure regions.
* `version` - Show information about the application version.
* `help` - Show this help message and exit.

## Syntax of the `azure-vm-price-importer.exe` for ***`download`*** commands

**Usage:** `azure-vm-price-importer.exe` ***`download`*** --path `PATH` --region `REGION` [--silent-mode {yes,no}] [--logs {yes,no}] [--help]

**Options:**
* `--path`, `-p` `PATH` - Path to the output file in **AZPX** format with downloaded data from Azure regarding price lists for a given region or all available regions.
* `--region`, `-r` `REGION` - Name of the region or value **`all`** if price lists of all regions are to be downloaded.
* `--silent-mode`, `-s {yes,no}` - Turn silent mode on or off.
* `--logs`, `-l {yes,no}` - Turning logging mode on or off to file logs_azure_vm_price_importer_*YYYYMMDDhhmmss*.log.
* `--help`, `-h` - Show this help message and exit.

## Syntax of the `azure-vm-price-importer.exe` for ***`save`*** commands

**Usage:** `azure-vm-price-importer.exe` ***`save`*** --azpx-load `AZPX_LOAD` --region `REGION` --path `PATH` --json `JSON` [--silent-mode {yes,no}] [--logs {yes,no}] [--help]

**Options:**
* `--azpx-load`, `-a` `AZPX_LOAD` - The name of the **AZPX** file with downloaded Azure VM price lists for the region being processed or from all regions.       
* `--region`, `-r` `REGION` - The name of the region for which the Azure VM price list will be processed to **JSON** format.
* `--path`, `-p` `PATH` - Path location of the **JSON** file with the resulting Azure VM pricing.
* `--json`, `-j` `JSON` - The name of the **JSON** file or **`auto`** for an automatically generated name containing the Azure VM pricing.
* `--silent-mode`, `-s {yes,no}` - Turn silent mode on or off.
* `--logs`, `-l {yes,no}` - Turning logging mode on or off to file logs_azure_vm_price_importer_*YYYYMMDDhhmmss*.log.
* `--help`, `-h` - Show this help message and exit.

## Syntax of the `azure-vm-price-importer.exe` for ***`export`*** commands

**Usage:** `azure-vm-price-importer.exe` ***`export`*** --json `JSON` --path `PATH` --format {csv,xlsx,sqlite,sql-sqlite,sql-mysql,sql-postgresql} --export `EXPORT` [--export-currency `EXPORT_CURRENCY`] [--delimiter `DELIMITER`] [--numeric `NUMERIC`] [--overwrite-sqlite {yes,no}] [--add-currency {yes,no}] [--silent-mode {yes,no}] [--logs {yes,no}] [--help]

**Options:**
* `--json`, `-j` `JSON` - The name of the **JSON** file with processed Azure VM pricing for a single region selected.
* `--path`, `-p` `PATH` - Path location of the exported file with the resulting Azure VM prices in the following formats: `CSV`, `Excel` (`XLSX`), `SQLite` database, `SQL` notation for databases (`SQLite`, `MySQL`, `PostgreSQL`).
* `--format`, `-f {csv,xlsx,sqlite,sql-sqlite,sql-mysql,sql-postgresql}` - Select one of the exported data formats: `CSV`, `Excel` (`XLSX`), `SQLite`, `SQL` notation for `SQLite`, `MySQL` and `PostgreSQL` databases.
* `--export`, `-e` `EXPORT` - The name of the resulting file for the exported data, or **`auto`** for the automatically generated name containing the Azure VM pricing.
* `--export-currency`, `-c` `EXPORT_CURRENCY` - The name of the resulting `CSV` file of the exported currency data, or **`auto`** for an automatically generated name that includes the Azure currency converter.
* `--delimiter`, `-d` `DELIMITER` - Column delimiter for `CSV` format. Default value is ` ; ` (*semicolon*).
* `--numeric`, `-n` `NUMERIC` - Numeric separator character. Default value is ` , ` (*comma*).
* `--overwrite-sqlite`, `-o {yes,no}` - Overwrite `SQLite` database.
* `--add-currency`, `-a {yes,no}` - Add data on currency conversion to `SQLite` database or `SQL` notation for `SQLite`, `MySQL` and `PostgreSQL` databases.
* `--silent-mode`, `-s {yes,no}` - Turn silent mode on or off.
* `--logs`, `-l {yes,no}` - Turning logging mode on or off to file logs_azure_vm_price_importer_*YYYYMMDDhhmmss*.log.
* `--help`, `-h` - Show this help message and exit.

## Syntax of the `azure-vm-price-importer.exe` for ***`available-regions`*** commands

**Usage:** `azure-vm-price-importer.exe` ***`available-regions`***

Show list of all available Azure regions.

## Syntax of the `azure-vm-price-importer.exe` for ***`version`*** commands

**Usage:** `azure-vm-price-importer.exe` ***`version`***

Show information about the application version.

## Syntax of the `azure-vm-price-importer.exe` for ***`help`*** commands

**Usage:** `azure-vm-price-importer.exe` **`help`**

Show this help message and exit.

---

## Copyright &copy; 2025 - 2026 by Sebastian Stybel, [www.BONO.Edu.PL](https://www.bono.edu.pl/)
