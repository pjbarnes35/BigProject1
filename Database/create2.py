import sqlite3
conn = sqlite3.connect("QnA2.db")
cr = conn.cursor()

# #creates new tables
# cr.execute("""
#     CREATE TABLE IF NOT EXISTS Buss_Strat (
#            id INTEGER PRIMARY KEY,
#            Question TEXT,
#            Answer TEXT)
    
# """)