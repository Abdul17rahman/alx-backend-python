import time
import sqlite3
import functools


query_cache = {}


def with_db_connection(func):
    """ creates a connection using with"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with sqlite3.connect("users.db") as conn:
            return func(conn, *args, **kwargs)
    return wrapper


def cache_query(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs['query']
        if query is None:
            return func(*args, **kwargs)

        if query in query_cache:
            return query_cache[query]

        res = func(*args, **kwargs)
        query_cache[query] = res
        return res
    return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


# First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")


# Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")

print(query_cache)
print(users)
