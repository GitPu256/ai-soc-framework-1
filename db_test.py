import sqlite3

print("DATABASE TEST START")

conn = sqlite3.connect("soc.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM results")
rows = cursor.fetchall()

print("DB Rows:")
for row in rows:
    print(row)

conn.close()

print("DATABASE TEST COMPLETE")
