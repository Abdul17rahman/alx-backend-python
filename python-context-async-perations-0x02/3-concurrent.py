import asyncio
import aiosqlite
import os

db_path = os.path.join(os.getcwd(), "../python-decorators-0x01/users.db")


async def async_fetch_users():
    async with aiosqlite.connect(db_path) as db:
        async with db.execute("SELECT * FROM users") as cursor:
            users = await cursor.fetchall()
            print("All users:")
            for user in users:
                print(user)
            return users


async def async_fetch_older_users():
    async with aiosqlite.connect(db_path) as db:
        async with db.execute("SELECT * FROM users WHERE id = 1") as cursor:
            older_users = await cursor.fetchall()
            print("\nFirst User:")
            for user in older_users:
                print(user)
            return older_users


async def fetch_concurrently():
    await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )


asyncio.run(fetch_concurrently())
