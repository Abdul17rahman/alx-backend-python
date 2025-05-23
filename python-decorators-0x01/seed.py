import sqlite3
import os


db_path = os.path.join(os.getcwd(), "users.db")

users = [
    ("Abdul Rahman", "abdul@gmail.com"),
    ("Ham Hamza", "ham@gmail.com"),
    ("Alex Muhozi", "alex@gmail.com"),
    ("Hassan Rashid", "hassan@gmail.com"),
    ("Moha Hassan", "moha@gmail.com"),
    ("Kasbar Zaki", "kasbar@gmail.com")
]

with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()

    cursor.executemany("INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)", users)

    conn.commit()

    print("Database seeded succesfully")

