import sqlite3
import os


class DatabaseConnection:
    def __init__(self, path):
        self.conn = sqlite3.connect(path)

    def __enter__(self):
        return self.conn

    def __exit__(self, exec_type, exc_val, exc_tb):
        self.conn.close()


db_path = os.path.join(os.getcwd(), "../python-decorators-0x01/users.db")

with DatabaseConnection(db_path) as db_conn:
    cursor = db_conn.cursor()

    result = cursor.execute("SELECT * FROM users")

    print(result.fetchall())
