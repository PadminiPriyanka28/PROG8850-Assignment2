import mysql.connector
import os

# Get MySQL credentials from GitHub Secrets
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

def execute_sql_script():
    try:
        # Connect to MySQL
        connection = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE
        )
        cursor = connection.cursor()

        # Read and execute SQL file
        with open("schema.sql", "r") as file:
            sql_script = file.read()
            for statement in sql_script.split(";"):
                if statement.strip():
                    cursor.execute(statement)

        connection.commit()
        print("Database changes applied successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    execute_sql_script()
