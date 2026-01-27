# Azure VM (Virtual Machine) Price Importer

This program allows you to download VM price lists from a specific region or all Azure regions (*currently 59 regions as of January 2026*).

The downloaded price list for a specific Azure region can then be processed and saved to an exchange file in `JSON` format. 

In addition, the price list for a selected Azure region can be exported from the `JSON` exchange file to several different formats, including `CSV`, `Excel` (`XLSX`), `SQLite`, `SQL` notation for `SQLite`, `MySQL`, and `PostgreSQL` databases.

This application therefore works in three (3) modes:
1. **Downloading** price list data for a specified single region or all Azure regions. The downloaded price lists are saved to a data package file in **AZPX** (**AZ**ure **P**rices packbo**X**) format.
2.	**Saving** processed price list data for a specific Azure region to an exchange file in JSON format, based on data previously downloaded in mode one ***(1)*** – **AZPX** package file.
3.	**Exporting** previously saved processed price lists in `JSON` format from mode two ***(2)*** to another format, including: `CSV`, `Excel` (`XLSX`), `SQLite`, `SQL` notation for `SQLite`, `MySQL`, and `PostgreSQL` databases.

Additionally, the application is able to list all currently available Azure regions (*currently 59 regions – as of January 2026*).

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

| Id | Region Name | Region Full Name | Country Name | Geographic Name | 
|-----|-----|-----|-----|-----|
| 1 | us-central | Central US | United States | North America | 
| 2 | us-east | East US | United States | North America | 
| 3 | us-east-2 | East US 2 | United States | North America | 
| 4 | us-north-central | North Central US | United States | North America | 
| 5 | us-south-central | South Central US | United States | North America | 
| 6 | us-west-central | West Central US | United States | North America | 
| 7 | us-west | West US | United States | North America | 
| 8 | us-west-2 | West US 2 | United States | North America | 
| 9 | us-west-3 | West US 3 | United States | North America | 
| 10 | united-kingdom-south | UK South | United Kingdom | Europe | 
| 11 | united-kingdom-west | UK West | United Kingdom | Europe | 
| 12 | uae-central | UAE Central | United Arab Emirates | Asia | 
| 13 | uae-north | UAE North | United Arab Emirates | Asia | 
| 14 | switzerland-north | Switzerland North | Switzerland | Europe | 
| 15 | switzerland-west | Switzerland West | Switzerland | Europe | 
| 16 | sweden-central | Sweden Central | Sweden | Europe | 
| 17 | sweden-south | Sweden South | Sweden | Europe | 
| 18 | spain-central | Spain Central | Spain | Europe | 
| 19 | qatar-central | Qatar Central | Qatar | Asia | 
| 20 | poland-central | Poland Central | Poland | Europe | 
| 21 | norway-east | Norway East | Norway | Europe | 
| 22 | norway-west | Norway West | Norway | Europe | 
| 23 | new-zealand-north | New Zealand North | New Zealand | Oceania | 
| 24 | mexico-central | Mexico Central | Mexico | North America | 
| 25 | malaysia-west | Malaysia West | Malaysia | Oceania | 
| 26 | korea-central | Korea Central | Korea | Asia | 
| 27 | korea-south | Korea South | Korea | Asia | 
| 28 | japan-east | Japan East | Japan | Asia | 
| 29 | japan-west | Japan West | Japan | Asia | 
| 30 | italy-north | Italy North | Italy | Europe | 
| 31 | israel-central | Israel Central | Israel | Asia | 
| 32 | indonesia-central | Indonesia Central | Indonesia | Asia | 
| 33 | central-india | Central India | India | Asia | 
| 34 | south-india | South India | India | Asia | 
| 35 | west-india | West India | India | Asia | 
| 36 | germany-north | Germany North | Germany | Europe | 
| 37 | germany-west-central | Germany West Central | Germany | Europe | 
| 38 | france-central | France Central | France | Europe | 
| 39 | france-south | France South | France | Europe | 
| 40 | europe-north | North Europe | Europe | Europe | 
| 41 | europe-west | West Europe | Europe | Europe | 
| 42 | chile-central | Chile Central | Chile | South America | 
| 43 | canada-central | Canada Central | Canada | North America | 
| 44 | canada-east | Canada East | Canada | North America | 
| 45 | brazil-south | Brazil South | Brazil | South America | 
| 46 | brazil-southeast | Brazil Southeast | Brazil | South America | 
| 47 | belgium-central | Belgium Central | Belgium | Europe | 
| 48 | usgov-arizona | US Gov Arizona | Azure Government | North America | 
| 49 | usgov-texas | US Gov Texas | Azure Government | North America | 
| 50 | usgov-virginia | US Gov Virginia | Azure Government | North America | 
| 51 | austria-east | Austria East | Austria | Europe | 
| 52 | australia-central | Australia Central | Australia | Oceania | 
| 53 | australia-central-2 | Australia Central 2 | Australia | Oceania | 
| 54 | australia-east | Australia East | Australia | Oceania | 
| 55 | australia-southeast | Australia Southeast | Australia | Oceania | 
| 56 | asia-pacific-east | East Asia | Asia Pacific | Asia | 
| 57 | asia-pacific-southeast | Southeast Asia | Asia Pacific | Asia | 
| 58 | south-africa-north | South Africa North | Africa | Africa | 
| 59 | south-africa-west | South Africa West | Africa | Africa | 

***Currently 59 regions – as of January 2026***

## Syntax of the `azure-vm-price-importer.exe` for ***`version`*** commands

**Usage:** `azure-vm-price-importer.exe` ***`version`***

Show information about the application version.

## Syntax of the `azure-vm-price-importer.exe` for ***`help`*** commands

**Usage:** `azure-vm-price-importer.exe` **`help`**

Show this help message and exit.

---

## Copyright &copy; 2025 - 2026 by Sebastian Stybel, [www.BONO.Edu.PL](https://www.bono.edu.pl/)
