import mysql.connector
from os import getenv
from dotenv import load_dotenv
import csv
import uuid

load_dotenv()

config = {
    "host": "localhost",
    "user": getenv("MYSQL_USRNAME"),
    "password": getenv("MYSQL_PASS")
}


def connect_db():
    db = mysql.connector.connect(**config)
    return db


def create_database(connection):
    cursor = connection.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")


def connect_to_prodev():
    config["database"] = "ALX_prodev"
    return connect_db()


def create_table(connection):
    cursor = connection.cursor()

    cursor.execute(""" CREATE TABLE IF NOT EXISTS user_data(user_id CHAR(36), Primary Key,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255), NOT NULL,
    age DECIMAL, NOT NULL)
    """)


def insert_data(connection, data):
    cursor = connection.cursor()

    with open(data) as dt:
        reader = csv.reader(dt)

        next(reader)

        for row in reader:
            user_id = uuid.uuid4()
            name, email, age = row

            cursor.execute("""
                    INSERT INTO user_data (user_id, name, email, age)
                    VALUES (%s, %s, %s, %s)
                """, (user_id, name, email, age))
    connection.commit()
