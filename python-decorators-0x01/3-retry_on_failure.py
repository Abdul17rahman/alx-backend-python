import time
import sqlite3
import functools

# paste your with_db_decorator here

""" your code goes here"""


def with_db_connection(func):
    """ creates a connection using with"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with sqlite3.connect("users.db") as conn:
            return func(conn, *args, **kwargs)
    return wrapper


def retry_on_failure(retries, delay):
    """ This is a decorator factory"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for num in range(retries, retries + 1):
                try:
                    return func(*args, *(kwargs))
                except:
                    if num < retries:
                        time.sleep(delay)
        return wrapper
    return decorator


@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

# attempt to fetch users with automatic retry on failure


users = fetch_users_with_retry()
print(users)
