import sqlite3
import functools
from datetime import datetime

# decorator to lof SQL queries


def log_queries(fn):
    def wrapper(*args, **kwargs):
        print(kwargs['query'])
        fn(*args, **kwargs)
    return wrapper


@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


# fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
