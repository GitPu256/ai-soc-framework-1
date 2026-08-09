import sqlite3
import json

# Create a real SQLite connection
connection = sqlite3.connect("soc.db", check_same_thread=False)

# Create table if it doesn't exist
connection.execute("""
CREATE TABLE IF NOT EXISTS severity_table (
    sorted_values TEXT
)
""")

def save(data):
    print("Saving to database:", data)
    connection.execute(
        "INSERT INTO severity_table (sorted_values) VALUES (?)",
        (json.dumps(data),)
    )
    connection.commit()
