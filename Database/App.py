import sqlite3

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