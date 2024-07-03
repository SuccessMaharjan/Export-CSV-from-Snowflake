import snowflake.connector
import os
from dotenv import load_dotenv

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

try:
    # Establishing the connection
    conn = snowflake.connector.connect(
        user=snowflake_user,
        password=snowflake_password,
        account=snowflake_account,
        warehouse=snowflake_warehouse,
        database=snowflake_database,
        schema=snowflake_schema,
        role=snowflake_role
    )

    # Create a cursor object
    cur = conn.cursor()

    # Execute a simple query
    cur.execute("SELECT CURRENT_VERSION()")
    result = cur.fetchone()
    print(f"Snowflake version: {result[0]}")

except Exception as e:
    print(f"Failed to connect to Snowflake: {e}")

finally:
    # Close the connection
    conn.close()
