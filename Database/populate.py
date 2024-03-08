import sqlite3

# Connect to the database
conn = sqlite3.connect("QnA2.db")
cr = conn.cursor()

# Define Function to populate data
def add_QnA(question, answer):
    cr.execute("INSERT INTO Finance (question, answer) VALUES (?, ?)", (question, answer))
    conn.commit()
    print("Question added to Finance :)")

# Adding questions outside the function
add_QnA("What is the Accronym for Cost Of Goods Sold?", "COGS")
add_QnA("What is the acronym for Return on Investment?", "ROI")
add_QnA("Define the term Dividend Yield", "YIELD")
add_QnA("What is the abbreviation for Initial Public Offering?", "IPO")
add_QnA("What is the acronym for Financial Statement Analysis?", "FSA")
add_QnA("What is the term of what is sold on the Stock Market?", "SHARES")
add_QnA("What is the abbreviation for Exchange Traded Fund?", "ETF")
add_QnA("Where is a companies income found?", "INCOME STATEMENT")
add_QnA("What state makes the calculators?", "TEXAS")
add_QnA("Who is the best finance professor? (LAST NAME)", "MOMENI")

# Close the connection
conn.close()
