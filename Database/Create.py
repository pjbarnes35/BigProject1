import sqlite3

# Function to create tables for each category
def create_tables(cursor):
    categories = ["business_app", "business_comm2", "finance", "advanced_analytics", "business_strategy"]
    for category in categories:
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {category} (id INTEGER PRIMARY KEY, question TEXT, answer TEXT)")

# Function to insert data into the tables
def insert_data(cursor):
    categories = ["business_app", "business_comm2", "finance", "advanced_analytics", "business_strategy"]
    for category in categories:
        for i in range(1, 11):
            cursor.execute(f"INSERT INTO {category} (question, answer) VALUES (?, ?)", (f"Question {i} for {category}", f"Answer {i} for {category}"))

# Function to fetch all tables and data
def fetch_data(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    data = {}
    for table in tables:
        cursor.execute(f"SELECT * FROM {table[0]}")
        data[table[0]] = cursor.fetchall()
    return data

# Main Quiz Bowl application
def quiz_bowl():
    # Connect to the SQLite database
    conn = sqlite3.connect("QnA.db")
    cursor = conn.cursor()

    # Create tables and insert data
    create_tables(cursor)
    insert_data(cursor)
    conn.commit()

    # Fetch all data
    all_data = fetch_data(cursor)
    print("Tables and data fetched from the database:")
    print(all_data)

    # Main application logic goes here

    # Close the database connection
    conn.close()

if __name__ == "__main__":
    quiz_bowl()
