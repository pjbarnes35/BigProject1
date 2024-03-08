import sqlite3
conn = sqlite3.connect("QnA2.db")
cr = conn.cursor()

#creates new tables
# cr.execute("""
#     CREATE TABLE IF NOT EXISTS Advanced_Analytics (
#            id INTEGER PRIMARY KEY,
#            Question TEXT,
#            Answer TEXT)
    
# """)