import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    mobile TEXT NOT NULL,
    password TEXT NOT NULL,
    transaction_id TEXT,
    status TEXT DEFAULT 'Pending',
    wallet REAL DEFAULT 0
)
""")

conn.commit()
conn.close()

print("Database created successfully!")
