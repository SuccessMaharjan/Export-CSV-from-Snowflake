import streamlit as st
import subprocess
from dotenv import load_dotenv, set_key, dotenv_values
import os

# Load environment variables from a .env file
load_dotenv()

# Define a function to update the .env file
def update_env(key, value):
    dotenv_path = '.env'
    # Remove any surrounding quotes from the value
    cleaned_value = value.strip().strip("'").strip('"')
    # Open the .env file and update the key-value pair
    with open(dotenv_path, 'r') as file:
        lines = file.readlines()

    with open(dotenv_path, 'w') as file:
        for line in lines:
            if line.startswith(key):
                file.write(f"{key}={cleaned_value}\n")
            else:
                file.write(line)


# Function to run the Makefile
def run_makefile():
    result = subprocess.run(['make'], capture_output=True, text=True)
    return result.stdout, result.stderr

st.title('Configure Environment and Export Snowflake CSV Data')

# Input fields for user to enter values for the .env file
st.subheader('Snowflake Configuration')
snowflake_user = st.text_input('SNOWFLAKE_USER')
snowflake_password = st.text_input('SNOWFLAKE_PASSWORD', type='password')
snowflake_account = st.text_input('SNOWFLAKE_ACCOUNT')
snowflake_warehouse = st.text_input('SNOWFLAKE_WAREHOUSE')
snowflake_role = st.text_input('SNOWFLAKE_ROLE')
snowflake_database = st.text_input('SNOWFLAKE_DATABASE')
snowflake_schema = st.text_input('SNOWFLAKE_SCHEMA')

st.subheader('File Paths')
path_prefix = st.text_input('Path prefix for file paths')

# Construct full paths
csv_file_path = path_prefix + '/Export-CSV-from-Snowflake/extracted_csv'
dbt_seeds_folder = path_prefix + '/Export-CSV-from-Snowflake/loadcsv/seeds'
csv_files_directory = path_prefix + '/Export-CSV-from-Snowflake/extracted_csv'

st.subheader('Target Snowflake Configuration')
target_snowflake_user = st.text_input('TARGET_SNOWFLAKE_USER')
target_snowflake_password = st.text_input('TARGET_SNOWFLAKE_PASSWORD', type='password')
target_snowflake_account = st.text_input('TARGET_SNOWFLAKE_ACCOUNT')
target_snowflake_warehouse = st.text_input('TARGET_SNOWFLAKE_WAREHOUSE')
target_snowflake_role = st.text_input('TARGET_SNOWFLAKE_ROLE')
target_snowflake_database = st.text_input('TARGET_SNOWFLAKE_DATABASE')
target_snowflake_schema = st.text_input('TARGET_SNOWFLAKE_SCHEMA')

# Button to update the .env file and run the Makefile
if st.button('Export Snowflake CSV Data'):
    status_placeholder = st.empty()
    
    # Update the .env file with the provided values
    update_env('SNOWFLAKE_USER', snowflake_user)
    update_env('SNOWFLAKE_PASSWORD', snowflake_password)
    update_env('SNOWFLAKE_ACCOUNT', snowflake_account)
    update_env('SNOWFLAKE_WAREHOUSE', snowflake_warehouse)
    update_env('SNOWFLAKE_ROLE', snowflake_role)
    update_env('SNOWFLAKE_DATABASE', snowflake_database)
    update_env('SNOWFLAKE_SCHEMA', snowflake_schema)
    update_env('CSV_FILE_PATH', csv_file_path)
    update_env('DBT_SEEDS_FOLDER', dbt_seeds_folder)
    update_env('CSV_FILES_DIRECTORY', csv_files_directory)
    update_env('TARGET_SNOWFLAKE_USER', target_snowflake_user)
    update_env('TARGET_SNOWFLAKE_PASSWORD', target_snowflake_password)
    update_env('TARGET_SNOWFLAKE_ACCOUNT', target_snowflake_account)
    update_env('TARGET_SNOWFLAKE_WAREHOUSE', target_snowflake_warehouse)
    update_env('TARGET_SNOWFLAKE_ROLE', target_snowflake_role)
    update_env('TARGET_SNOWFLAKE_DATABASE', target_snowflake_database)
    update_env('TARGET_SNOWFLAKE_SCHEMA', target_snowflake_schema)
    
    with st.spinner('Exporting CSV...'):
        status_placeholder.info('Exporting CSV...')
        stdout, stderr = run_makefile()
        status_placeholder.success('CSV Export and Load to Target Snowflake completed.')

    st.subheader('Output')
    st.text(stdout)
    st.subheader('Errors')
    st.text(stderr)
