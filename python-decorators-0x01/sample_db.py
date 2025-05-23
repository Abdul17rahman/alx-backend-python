import sqlite3
import os


db_path = os.path.join(os.getcwd(), "users.db")

with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
    """)

    conn.commit()

    print(f"Database created at {db_path}")


