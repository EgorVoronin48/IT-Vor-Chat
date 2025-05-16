import asyncio
import sqlite3
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from survey_bot import Survey
from start_survey import StartSurvey
from completion import get_user_stats, reset_user_survey
from keyboards import main_menu

bot = Bot("7021048853:AAH8kf3kH141FiXnn04snayk-aTbBQXutWo")
dp = Dispatcher()

survey = Survey(bot)
start_survey = StartSurvey(bot)

ADMIN_ID = 6404103603


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
                    register_date TEXT DEFAULT CURRENT_TIMESTAMP,
                    last_action TEXT
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS survey (
                    user_id INTEGER PRIMARY KEY,
                    color TEXT, food TEXT, film TEXT,
                    music TEXT, yeartime TEXT, drink TEXT,
                    rest TEXT, animal TEXT, holiday TEXT, sport TEXT
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS friend_answers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    friend_id INTEGER NOT NULL,
                    color TEXT, food TEXT, film TEXT,
                    music TEXT, yeartime TEXT, drink TEXT,
                    rest TEXT, animal TEXT, holiday TEXT, sport TEXT
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS stats (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    friend_id INTEGER NOT NULL,
                    match_percent REAL,
                    test_date TEXT DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
    except Exception as e:
        print(f"Ошибка при создании таблиц: {e}")


@dp.message(Command("start"))
async def start_handler(message: Message):
    try:
        args = message.text.split()
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

        if len(args) > 1:
            friend_id = args[1]
            if not friend_id.isdigit():
                await message.answer("❌ Некорректный ID друга")
                return
            await start_survey.handle_start_link(message, friend_id)
        else:
            await message.answer(
                f"Привет, {message.from_user.first_name}! 👋\n"
                "Я бот для создания тестов о ваших предпочтениях.\n"
                "Выберите действие:",
                reply_markup=main_menu
            )
    except Exception as e:
        await message.answer("⚠️ Произошла ошибка")
        print(f"Error in start_handler: {e}")


@dp.message(lambda message: message.text == "Составить тест")
async def create_test_handler(message: Message):
    try:
        await survey.start_survey(message)
    except Exception as e:
        await message.answer("⚠️ Не удалось начать тест")
        print(f"Error in create_test_handler: {e}")


@dp.message(lambda message: message.text == "Пройти тест")
async def take_test_handler(message: Message):
    await message.answer(
        "Чтобы пройти тест о друге, используйте его ссылку или команду:\n"
        "/start <ID_друга>"
    )


@dp.message(lambda message: message.text == "Моя статистика")
async def stats_handler(message: Message):
    try:
        stats = await get_user_stats(message.from_user.id)
        if not stats:
            await message.answer("📊 У вас пока нет статистики")
            return

        response = "📊 Ваша статистика:\n\n"
        for stat in stats:
            response += (
                f"👤 Друг: {stat['friend_name']}\n"
                f"📈 Совпадение: {stat['match_percent']:.1f}%\n"
                f"📅 Дата: {stat['date']}\n\n"
            )
        await message.answer(response)
    except Exception as e:
        await message.answer("⚠️ Ошибка при получении статистики")
        print(f"Error in stats_handler: {e}")


@dp.message(lambda message: message.text == "Сбросить мой тест")
async def reset_test_handler(message: Message):
    try:
        success = await reset_user_survey(message.from_user.id)
        if success:
            await message.answer("✅ Ваш тест успешно сброшен")
        else:
            await message.answer("ℹ️ У вас нет сохраненного теста")
    except Exception as e:
        await message.answer("⚠️ Ошибка при сбросе теста")
        print(f"Error in reset_test_handler: {e}")


@dp.callback_query()
async def callback_handler(callback: CallbackQuery):
    try:
        if callback.data.startswith('survey_'):
            await survey.process_callback(callback)
        elif any(callback.data.startswith(f"{i}_") for i in range(1, 11)):
            await start_survey.handle_callback(callback)
        else:
            await callback.answer("Неизвестная команда")
    except Exception as e:
        await callback.answer("⚠️ Ошибка обработки")
        print(f"Error in callback_handler: {e}")


async def main():
    try:
        await create_tables()
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Fatal error: {e}")
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
