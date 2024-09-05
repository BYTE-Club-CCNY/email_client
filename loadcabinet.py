import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Get database credentials from environment variables
db_host = os.getenv('POSTGRESQL_DB_HOST')
db_user = os.getenv('POSTGRESQL_DB_USER')
db_password = os.getenv('POSTGRESQL_DB_PASSWORD')
db_name = os.getenv('POSTGRESQL_DB')
db_port = os.getenv('POSTGRESQL_DB_PORT')

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    dbname=db_name,
    port=db_port
)

# Create a cursor object
cursor = conn.cursor()

# Read and execute the SQL file
with open('database/cabinet.sql', 'r') as sql_file:
    sql_commands = sql_file.read()

cursor.execute(sql_commands)

# Commit changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("SQL file executed successfully")
