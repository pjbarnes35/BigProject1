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

# ANSI escape codes for colors
class colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'

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
            user_answer = input("Answer: ")
            if user_answer.upper() == question[2]:
                print(colors.GREEN + "Correct!")
            else:
                print(colors.RED + f"Wrongo! The answer was {question[2]}")
            print(colors.RESET)
    else:
        print(colors.RED + "Invalid choice! Please enter a number between 1 and 5.")
        print(colors.RESET)

    conn.close()

# Run the quiz bowl
quiz_bowl()
