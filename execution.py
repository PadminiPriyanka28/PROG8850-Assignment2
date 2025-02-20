import mysql.connector
import os

# Database connection details (use GitHub Secrets)
db_config = {
    "host": os.getenv("MYSQL_HOST"),         # Azure MySQL host
    "user": os.getenv("MYSQL_USER"),         # MySQL username
    "password": os.getenv("MYSQL_PASSWORD"), # MySQL password
    "database": os.getenv("MYSQL_DATABASE")  # MySQL database name
}

def execution_script():
    try:
        # Attempt to connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        print("Connected to MySQL successfully!")

        # Example SQL execution (Change this to your desired script)
        cursor.execute("SELECT NOW();")
        result = cursor.fetchone()
        print(f"Current MySQL time: {result}")

        # You can add other SQL commands here

        # Commit the changes
        conn.commit()

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Always close the connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    execution_script()
