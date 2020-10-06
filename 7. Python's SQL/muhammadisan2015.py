import sqlite3
import pandas as pd

df = pd.read_csv('pulau_indonesia.csv').fillna('')

conn = sqlite3.connect('muhammadisan2015.db')
cur = conn.cursor()

create_table = '''CREATE TABLE IF NOT EXISTS pulau_indonesia (No INTEGER, 
                                                              Provinsi TEXT, 
                                                              Pulau_Bernama INTEGER, 
                                                              Pulau_Tak_Bernama INTEGER, 
                                                              Total INTEGER);'''
                                                              
cur.execute(create_table)
conn.commit()

for i in range(len(df.index)):
  pulau_indonesia = tuple(df.iloc[i])
  insert_into = "INSERT OR IGNORE INTO pulau_indonesia VALUES(?, ?, ?, ?, ?);"
  cur.execute(insert_into, pulau_indonesia)
  conn.commit()

cur.execute("SELECT * FROM pulau_indonesia;")
conn.commit()
all_results = cur.fetchall()

cur.close()
conn.close()

print(all_results)