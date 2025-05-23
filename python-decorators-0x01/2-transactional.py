import sqlite3
import functools


def transactional(func):
    """ This function perfroms a db transaction"""
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()
            return result
        except Exception as err:
            print(f"Error occured {err}")
            conn.rollback()
    return wrapper


def with_db_connection(func):
    """ creates a connection using with"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with sqlite3.connect("users.db") as conn:
            return func(conn, *args, **kwargs)
    return wrapper


@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    return cursor.execute("UPDATE users SET email = ? WHERE id = ?",
                          (new_email, user_id))

# Update user's email with automatic transaction handling


print(update_user_email(user_id=1, new_email='abdul_abdul@hotmail.com'))
