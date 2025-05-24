import sqlite3
import os


class ExecuteQuery:
    def __init__(self, path, query):
        self.conn = sqlite3.connect(path)
        self.query = query

    def __enter__(self):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(self.query)
        except Exception as e:
            print(f"Error: {e}")
        return self.cursor

    def __exit__(self, type, value, traceback):
        if type:
            self.conn.rollback()
        else:
            if self.query.strip().lower().startswith(("insert", "update", "delete")):
                self.conn.commit()
        self.conn.close()


db_path = os.path.join(os.getcwd(), "../python-decorators-0x01/users.db")


with ExecuteQuery(db_path, "SELECT * FROM users WHERE age = 1") as ex:
    print(ex.fetchall())
