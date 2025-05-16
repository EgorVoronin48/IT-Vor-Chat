import asyncio
import sqlite3
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

bot = Bot("7021048853:AAH8kf3kH141FiXnn04snayk-aTbBQXutWo")
dp = Dispatcher()


async def create_tables():
    try:
        with sqlite3.connect("bd/tg.db") as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL UNIQUE,
                    username TEXT,
                    first_name TEXT,
                    last_name TEXT,
                    register_date TEXT DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
    except Exception as e:
        print(f"Ошибка при создании таблиц: {e}")

@dp.message(Command("start"))
async def start_handler(message: Message):
    try:
        with sqlite3.connect("bd/tg.db") as conn:
            cursor = conn.cursor()
            cursor.execute(
                """INSERT OR IGNORE INTO users 
                (user_id, username, first_name, last_name) 
                VALUES (?, ?, ?, ?)""",
                (message.from_user.id, message.from_user.username,
                 message.from_user.first_name, message.from_user.last_name)
            )
            conn.commit()
        await message.answer(f"Привет, {message.from_user.first_name}! 👋")
    except Exception as e:
        print(f"Error in start_handler: {e}")


@dp.message(lambda message: message.text == "Составить тест")
async def create_test_handler(message: Message):
    await message.answer("Функция в разработке")

@dp.message(lambda message: message.text == "Пройти тест")
async def take_test_handler(message: Message):
    await message.answer("Функция в разработке")        


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
