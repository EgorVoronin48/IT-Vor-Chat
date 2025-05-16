from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Составить тест"), KeyboardButton(text="Пройти тест")],
        [KeyboardButton(text="Моя статистика"), KeyboardButton(text="Сбросить мой тест")]
    ],
    resize_keyboard=True
)