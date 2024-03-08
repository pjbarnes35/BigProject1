import sqlite3
import random

# Connect to the database
conn = sqlite3.connect("QnA2.db")
cr = conn.cursor()

# Function to fetch questions from a specific table
def fetch_questions(table):
    cr.execute(f"SELECT * FROM {table}")
    return cr.fetchall()

# Function to display options and get user's choice
def choose_table():
    print("Choose a table to get questions from:")
    print("1. Finance")
    print("2. Advanced Business Analytics")
    print("3. Business Communications 2")
    print("4. Business Strategy")
    print("5. Business Development Applications")
    choice = input("Enter your choice (1-5): ")
    return choice

# Main function to run the quiz bowl
def quiz_bowl():
    choice = choose_table()
    tables = ["Finance", "Advanced_Analytics", "Buss_Comm2", "Buss_Strat", "Buss_Dev_App43"]
    
    if choice.isdigit() and 1 <= int(choice) <= len(tables):
        chosen_table = tables[int(choice) - 1]
        questions = fetch_questions(chosen_table)
        random.shuffle(questions)
        
        for question in questions:
            print(question[1])
            userAnswer = input("Answer: ")
            if userAnswer.upper() == question[2]:
                print("Correct!")
            else:
                print("Wrongo! The answer was", question[2])
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
    
    conn.close()

# Run the quiz bowl
quiz_bowl()
