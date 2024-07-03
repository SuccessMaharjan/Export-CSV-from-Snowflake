import os
from dotenv import load_dotenv
import yaml


# Load environment variables from .env file
load_dotenv()

# Accessing environment variables
snowflake_account = os.getenv("TARGET_SNOWFLAKE_ACCOUNT")
snowflake_user = os.getenv("TARGET_SNOWFLAKE_USER")
snowflake_password = os.getenv("TARGET_SNOWFLAKE_PASSWORD")
snowflake_role = os.getenv("TARGET_SNOWFLAKE_ROLE")
snowflake_database = os.getenv("TARGET_SNOWFLAKE_DATABASE")
snowflake_warehouse = os.getenv("TARGET_SNOWFLAKE_WAREHOUSE")
snowflake_schema = os.getenv("TARGET_SNOWFLAKE_SCHEMA")


# Creating the data transformation dictionary
loadcsv = {
   "loadcsv":{
    "outputs": {
        "dev": {
            "type": "snowflake",
            "account": snowflake_account,
            "user": snowflake_user,
            "password": snowflake_password,
            "role": snowflake_role,
            "database": snowflake_database,
            "warehouse": snowflake_warehouse,
            "schema": snowflake_schema,
            "threads": 4,
            "client_session_keep_alive": True
        }
    },
    "target": "dev"
}
}


with open("profiles.yml", "w") as yaml_file:
    yaml.dump(loadcsv, yaml_file, default_flow_style=False)