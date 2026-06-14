import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO members (name, age, plan)
VALUES (?, ?, ?)
""", ("Manoj", 24, "Monthly"))

conn.commit()
conn.close()

print("Member added successfully!")