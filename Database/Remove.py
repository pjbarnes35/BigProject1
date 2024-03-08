import sqlite3

# Function to remove all tables from the database
def remove_tables(table):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect("QnA2.db")
        cursor = conn.cursor()

        # Fetch all table names
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        # Drop each table
        for table in tables:
            cursor.execute(f"DROP TABLE IF EXISTS {table[0]}")
            print(f"Dropped table: {table[0]}")

        # Commit the changes
        conn.commit()
        print("All tables removed successfully.")

    except sqlite3.Error as e:
        print("Error occurred:", e)

    finally:
        # Close the database connection
        if conn:
            conn.close()

# Remove tables from the database
remove_tables('table1')
