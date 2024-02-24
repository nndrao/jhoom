pip install pandas sqlalchemy pyodbc

import pandas as pd
from sqlalchemy import create_engine
import urllib

# Specify your SQL Server connection details
server = 'your_server_name'
database = 'your_database_name'
username = 'your_username'
password = 'your_password'
driver= 'ODBC Driver 17 for SQL Server' # or another driver as per your SQL Server setup
table_name = 'your_table_name' # The table you want to insert the data into

# Read data from Excel file
excel_file_path = 'your_excel_file_path.xlsx'
sheet_name = 'your_sheet_name'
df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

# Define the connection URL
connection_str = (
    f"mssql+pyodbc://{username}:{password}@{server}/{database}"
    f"?driver={urllib.parse.quote_plus(driver)}"
)

# Create the database engine
engine = create_engine(connection_str)

# Insert the DataFrame into the SQL table
df.to_sql(table_name, engine, if_exists='append', index=False)

print("Data imported successfully.")
