import asyncio
import aiosqlite


async def async_fetch_users():
    async with aiosqlite.connect("users.db") as db:
        cursor = await db.cursor()
        await cursor.execute("SELECT * FROM users")
        results = await cursor.fetchall()
        return results

async def async_fetch_older_users():
    async with aiosqlite.connect("users.db") as db:
        cursor = await db.cursor()
        await cursor.execute("SELECT * FROM users WHERE age > 40")
        results = await cursor.fetchall()
        return row


async def fetch_concurrently():
    await asyncio.gather(async_fetch_users(), async_fetch_older_users())

asyncio.run(fetch_concurrently())