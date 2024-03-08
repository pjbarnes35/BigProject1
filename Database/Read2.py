import sqlite3
conn = sqlite3.connect("QnA2.db")
cr = conn.cursor()

# Function to fetch all tables and data
def fetch_data(cursor):
    cr.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cr.fetchall()
    data = {}
    for table in tables:
        cursor.execute(f"SELECT * FROM {table[0]}")
        data[table[0]] = cursor.fetchall()
    return data
print(fetch_data(cr))