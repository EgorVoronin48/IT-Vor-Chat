import sqlite3
from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from typing import Dict
from keyboards import (
    inline_k_1_question, inline_k_2_question, inline_k_3_question,
    inline_k_4_question, inline_k_5_question, inline_k_6_question,
    inline_k_7_question, inline_k_8_question, inline_k_9_question,
    inline_k_10_question, main_menu
)


class StartSurvey:
    def __init__(self, bot: Bot):
        self.bot = bot
        self.user_states: Dict[int, Dict] = {}

    async def handle_start_link(self, message: Message, friend_id: str):
        try:
            if not friend_id.isdigit():
                await message.answer("❌ Некорректный ID друга")
                return

            user_id = message.from_user.id
            friend_id = int(friend_id)

            if user_id == friend_id:
                await message.answer("❌ Нельзя проходить тест о себе")
                return

            if not await self._check_friend_exists(friend_id):
                await message.answer("❌ Пользователь не создал тест")
                return

            self.user_states[user_id] = {
                "friend_id": friend_id,
                "answers": {},
                "current_question": 1
            }

            await self._send_question(user_id)

        except Exception as e:
            await message.answer("⚠️ Ошибка запуска теста")
            print(f"Error in handle_start_link: {e}")

    async def handle_callback(self, callback: CallbackQuery):
        try:
            user_id = callback.from_user.id
            if user_id not in self.user_states:
                await callback.answer("❌ Тест не начат", show_alert=True)
                return

            data_parts = callback.data.split('_')
            print(data_parts)
            if len(data_parts) != 3:
                await callback.answer("❌ Некорректные данные")
                return

            q_num_str, field, value = data_parts
            q_num = int(q_num_str)

            state = self.user_states[user_id]
            state["answers"][field] = value
            state["current_question"] = q_num + 1

            await callback.message.delete()

            if q_num >= 10:
                await self._complete_test(user_id, callback.message)
            else:
                await self._send_question(user_id)

        except Exception as e:
            await callback.answer("⚠️ Ошибка обработки")
            print(f"Error in handle_callback: {e}")

    async def _send_question(self, user_id: int):
        state = self.user_states.get(user_id)
        if not state:
            return

        current_q = state["current_question"]
        questions = self._get_questions_list()

        if 1 <= current_q <= len(questions):
            await self.bot.send_message(
                user_id,
                questions[current_q - 1]["text"],
                reply_markup=questions[current_q - 1]["keyboard"]
            )

    def _get_questions_list(self):

        return [
            {
                "text": "1. Какой любимый цвет у вашего друга? 🌈",
                "keyboard": inline_k_1_question,
                "field": "color"
            },
            {
                "text": "2. Какое любимое блюдо у вашего друга? 🍽️",
                "keyboard": inline_k_2_question,
                "field": "food"
            },
            {
                "text": "3. Какой любимый фильм/сериал у вашего друга? 🎬",
                "keyboard": inline_k_3_question,
                "field": "film"
            },
            {
                "text": "4. Какая любимая музыка у вашего друга? 🎵",
                "keyboard": inline_k_4_question,
                "field": "music"
            },
            {
                "text": "5. Какое любимое время года у вашего друга? 🌸☀️🍂❄️",
                "keyboard": inline_k_5_question,
                "field": "yeartime"
            },
            {
                "text": "6. Какой любимый напиток у вашего друга? 🥤",
                "keyboard": inline_k_6_question,
                "field": "drink"
            },
            {
                "text": "7. Как ваш друг предпочитает отдыхать? 🏖️",
                "keyboard": inline_k_7_question,
                "field": "rest"
            },
            {
                "text": "8. Какое любимое животное у вашего друга? 🐾",
                "keyboard": inline_k_8_question,
                "field": "animal"
            },
            {
                "text": "9. Какой любимый праздник у вашего друга? 🎉",
                "keyboard": inline_k_9_question,
                "field": "holiday"
            },
            {
                "text": "10. Какой любимый вид спорта у вашего друга? ⚽",
                "keyboard": inline_k_10_question,
                "field": "sport"
            }
        ]

    async def _check_friend_exists(self, friend_id: int) -> bool:
        try:
            with sqlite3.connect("bd/tg.db") as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT 1 FROM survey WHERE user_id = ?", (friend_id,))
                return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error in _check_friend_exists: {e}")
            return False

    async def _complete_test(self, user_id: int, message: Message):
        state = self.user_states.pop(user_id, None)
        if not state:
            return

        try:
            from completion import save_answers, calculate_match, get_correct_answers

            state["answers"]["friend_id"] = state["friend_id"]
            await save_answers(user_id, state["answers"], "friend")

            percent = await calculate_match(user_id, state["friend_id"], state["answers"])

            if percent is None:
                await message.answer("⚠️ Не удалось рассчитать совпадения")
                return

            answers_comparison = await get_correct_answers(user_id, state["friend_id"])

            result_message = (
                f"📊 Результат: {percent:.1f}% совпадений\n"
                f"ID друга: {state['friend_id']}\n\n"
                "🔍 Сравнение ответов:\n"
            )

            field_names = {
                'color': '🎨 Любимый цвет',
                'food': '🍽️ Любимая еда',
                'film': '🎬 Любимый фильм/сериал',
                'music': '🎵 Любимая музыка',
                'yeartime': '🌦️ Любимое время года',
                'drink': '🥤 Любимый напиток',
                'rest': '🏖️ Отдых',
                'animal': '🐾 Любимое животное',
                'holiday': '🎉 Любимый праздник',
                'sport': '⚽ Любимый спорт'
            }

            for field, name in field_names.items():
                user_answer = answers_comparison['user_answers'].get(field, '❌ Нет ответа')
                correct_answer = answers_comparison['correct_answers'].get(field, '❌ Нет ответа')

                result_message += (
                    f"\n{name}:\n"
                    f"Ваш ответ: {user_answer}\n"
                    f"Правильный ответ: {correct_answer}\n"
                )

            await message.answer(result_message, reply_markup=main_menu)

            friend_name = message.from_user.first_name
            print(friend_name)

            try:
                await self.bot.send_message(
                    state["friend_id"],
                    f"👤 Пользователь {friend_name} прошел ваш тест!\n"
                    f"📊 Результат: {percent:.1f}% совпадений"
                )
            except Exception as e:
                print(f"Error sending notification to test creator: {e}")

        except Exception as e:
            await message.answer("⚠️ Ошибка при расчете совпадений")
            print(f"Error in _complete_test: {e}")