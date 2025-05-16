import asyncio
from aiogram import Bot, Dispatcher

bot = Bot("7021048853:AAH8kf3kH141FiXnn04snayk-aTbBQXutWo")
dp = Dispatcher()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())