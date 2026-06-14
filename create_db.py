import sqlite3

# Connect to database (creates it if it doesn't exist)
conn = sqlite3.connect("database.db")

# Create cursor
cursor = conn.cursor()

# Create members table
cursor.execute("""
CREATE TABLE IF NOT EXISTS members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    plan TEXT NOT NULL
)
""")

# Save changes
conn.commit()

# Close connection
conn.close()

print("Database and table created successfully!")