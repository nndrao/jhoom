import pandas as pd
from sqlalchemy import create_engine

# Parameters
excel_file_path = 'path_to_your_excel_file.xlsx'
database_connection_url = 'mssql+pyodbc://your_username:your_password@your_server_address/your_database?driver=SQL+Server'
table_name = 'your_new_table_name'

# Load Excel file into DataFrame
df = pd.read_excel(excel_file_path)

# Create SQL Alchemy engine
engine = create_engine(database_connection_url)

# Use 'if_exists' parameter as 'fail' to ensure a new table is created, 'replace' to overwrite existing
df.to_sql(table_name, engine, if_exists='fail', index=False)

# No need to explicitly manage connection lifecycle with sqlalchemy
