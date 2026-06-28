import sqlite3

conn = sqlite3.connect("PersonagensDB.db")
cursor = conn.cursor()
cursor.execute("""
            CREATE TABLE IF NOT EXISTS personagens(
               nome TEXT NOT NULL,
               raca TEXT NOT NULL,
               alinhamento TEXT NOT NULL,
               saga TEXT NOT NULL,
               universo TEXT NOT NULL,
               grupo TEXT NOT NULL,
               planeta TEXT NOT NULL,
               status TEXT NOT NULL
               )   
               """)
conn.commit()
conn.close()