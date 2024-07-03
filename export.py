import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
import pandas as pd
import logging
from sqlalchemy.exc import SQLAlchemyError

# Enable logging
logging.basicConfig(level=logging.DEBUG)

# Load environment variables from .env file
load_dotenv()

# Accessing environment variables
snowflake_account = os.getenv("SNOWFLAKE_ACCOUNT")
snowflake_user = os.getenv("SNOWFLAKE_USER")
snowflake_password = os.getenv("SNOWFLAKE_PASSWORD")
snowflake_role = os.getenv("SNOWFLAKE_ROLE")
snowflake_database = os.getenv("SNOWFLAKE_DATABASE")
snowflake_warehouse = os.getenv("SNOWFLAKE_WAREHOUSE")
snowflake_schema = os.getenv("SNOWFLAKE_SCHEMA")
csv_file_path = os.getenv("CSV_FILE_PATH")

logging.debug(f"Snowflake Account: {snowflake_account}")

# Constructing the connection URL
connection_string = (
    f'snowflake://{snowflake_user}:{snowflake_password}@{snowflake_account}'
    f'/?warehouse={snowflake_warehouse}&database={snowflake_database}&role={snowflake_role}&schema={snowflake_schema}'
)

try:
    engine = create_engine(connection_string)
    conn = engine.connect()
    print("Connection successful!")
except SQLAlchemyError as e:
    print(f"Error connecting to Snowflake: {e}")

logging.debug(f"Connection string: {connection_string}")

# Create a SQLAlchemy engine
engine = create_engine(connection_string)

try:
    # Query to get all table names in the schema
    table_query = text(f"""
    SELECT table_name 
    FROM information_schema.tables 
    WHERE table_schema = '{snowflake_schema}'
    """)

    with engine.connect() as connection:
        tables = connection.execute(table_query).fetchall()

    # Iterate over each table and export its data to a CSV file
    for table_name, in tables:
        logging.debug(f"Exporting table: {table_name}")
        # Query to get all data from the table
        data_query = f"SELECT * FROM {snowflake_schema}.{table_name}"
        
        data = pd.read_sql(data_query, engine)

        # Define the CSV file path
        csv_file_path_with_table = os.path.join(csv_file_path, f"{table_name}.csv")
        
        # Create the directory if it does not exist
        os.makedirs(os.path.dirname(csv_file_path_with_table), exist_ok=True)

        # Export data to CSV
        data.to_csv(csv_file_path_with_table, index=False)
        logging.debug(f"Data from table {table_name} exported to {csv_file_path_with_table}")

except Exception as e:
    logging.error(f"An error occurred: {e}")

finally:
    # Close the engine
    engine.dispose()