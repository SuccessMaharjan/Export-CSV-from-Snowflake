# Export CSV from Snowflake
This repository provides code for exporting
CSV files from a Snowflake schema and load the exported CSV files into
another Snowflake account. 

## Prerequisites

- Snowflake accounts (to export
from and to import to) 

## Usage

1. Fork the Repository: 
- Click the "Fork" button on the top right corner of this repository. 

2. Clone the repository: 
```sh
git clone https://github.com/YOUR_USERNAME/Export-CSV-from-Snowflake.git
```
Note: Replace YOUR_USERNAME with your GitHub username. 

3. Navigate to the directory: 
```sh
cd Export-CSV-from-Snowflake
```

4. Create the target database and schema in the target Snowflake:
```sh
Create database <db-name>
Create schema <schema-name>
```

5. Create .env file:
```sh
SNOWFLAKE_USER=\<username\>
SNOWFLAKE_PASSWORD=\<password\> SNOWFLAKE_ACCOUNT=\<account-name\>
SNOWFLAKE_WAREHOUSE=\<warehouse\> SNOWFLAKE_ROLE=\<role\>

SNOWFLAKE_DATABASE=\<db-name-for-source-tables\>
SNOWFLAKE_SCHEMA=\<schema-name-for-source-tables\>

CSV_FILE_PATH=\<your-path\>/Export-CSV-from-Snowflake/extracted_csv
DBT_SEEDS_FOLDER=\<your-path\>/Export-CSV-from-Snowflake/loadcsv/seeds
CSV_FILES_DIRECTORY=\<your-path\>/Export-CSV-from-Snowflake/extracted_csv

TARGET_SNOWFLAKE_USER=\<username\>
TARGET_SNOWFLAKE_PASSWORD=\<password\>
TARGET_SNOWFLAKE_ACCOUNT=\<account-name\>
TARGET_SNOWFLAKE_WAREHOUSE=\<warehouse\> TARGET_SNOWFLAKE_ROLE=\<role\>
```

6. Run make command: 
```sh
make
```
