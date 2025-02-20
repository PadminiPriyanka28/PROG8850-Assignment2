import os
import mysql.connector
from mysql.connector import Error

# Fetch MySQL credentials from environment variables
host = os.getenv('MYSQL_HOST')
user = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')
database = os.getenv('MYSQL_DATABASE')

# Define the path to the SQL file
sql_file_path = 'schema.sql'

def execute_sql_script():
    """Connect to the MySQL database and execute the SQL script."""
    try:
        # Establishing a connection to the database
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        if connection.is_connected():
            print(f"Connected to the database {database} at {host}")
            cursor = connection.cursor()

            # Read and execute the SQL script from the file
            with open(sql_file_path, 'r') as file:
                sql_script = file.read()
                cursor.execute(sql_script, multi=True)  # Execute multi-statements from file
                connection.commit()
                print("SQL script executed successfully.")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

# Run the SQL script
execute_sql_script()
