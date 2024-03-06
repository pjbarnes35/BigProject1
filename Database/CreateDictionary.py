import sqlite3

# Create a connection to the database
conn = sqlite3.connect("QnA.db")

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# SQL statements to create tables for the 5 classes
sql_queries = [
    """
    CREATE TABLE IF NOT EXISTS Business_Applications_Development (
        QuestionID INTEGER PRIMARY KEY AUTOINCREMENT,
        Question TEXT,
        Answer TEXT
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Advanced_Business_Analytics (
        QuestionID INTEGER PRIMARY KEY AUTOINCREMENT,
        Question TEXT,
        Answer TEXT
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Business_Communications_2 (
        QuestionID INTEGER PRIMARY KEY AUTOINCREMENT,
        Question TEXT,
        Answer TEXT
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Business_Strategy (
        QuestionID INTEGER PRIMARY KEY AUTOINCREMENT,
        Question TEXT,
        Answer TEXT
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Principles_of_Finance (
        QuestionID INTEGER PRIMARY KEY AUTOINCREMENT,
        Question TEXT,
        Answer TEXT
    )
    """
]

# Execute each SQL statement
for query in sql_queries:
    cursor.execute(query)

# Commit the changes and close the connection
conn.commit()
conn.close()
