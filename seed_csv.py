import shutil
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define the paths to the dbt seeds folder and the directory containing the CSV files
dbt_seeds_folder = os.getenv('DBT_SEEDS_FOLDER')
csv_files_directory = os.getenv('CSV_FILES_DIRECTORY')

# List all CSV files in the directory
csv_files = [f for f in os.listdir(csv_files_directory) if f.endswith('.csv')]

# Copy each CSV file to the dbt seeds folder
for csv_file in csv_files:
    source_file = os.path.join(csv_files_directory, csv_file)
    destination_file = os.path.join(dbt_seeds_folder, csv_file)

    try:
        shutil.copyfile(source_file, destination_file)
        print(f"File '{csv_file}' copied successfully to dbt seeds folder.")
    except Exception as e:
        print(f"Error copying file '{csv_file}': {e}")