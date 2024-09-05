import psycopg2
from dotenv import load_dotenv
import os

# env
load_dotenv()
db_host = os.getenv('POSTGRESQL_DB_HOST')
db_user = os.getenv('POSTGRESQL_DB_USER')
db_password = os.getenv('POSTGRESQL_DB_PASSWORD')
db_name = os.getenv('POSTGRESQL_DB')
db_port = os.getenv('POSTGRESQL_DB_PORT')

#pgadmin
conn = psycopg2.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    dbname=db_name,
    port=db_port
)

# this i gpt'd
cursor = conn.cursor()
with open('database/cabinet.sql', 'r') as sql_file:
    sql_commands = sql_file.read()
cursor.execute(sql_commands)
conn.commit()
cursor.close()
conn.close()
print("SQL file executed successfully")
