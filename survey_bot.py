from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from typing import Dict
from keyboards import main_menu, get_survey_keyboard

class Survey:
    def __init__(self, bot: Bot):
        self.bot = bot
        self.user_sessions: Dict[int, Dict] = {}

    async def start_survey(self, message: Message):
        try:
            user_id = message.from_user.id
            self.user_sessions[user_id] = {
                "answers": {},
                "current_q": 1,
                "type": "self"
            }
            await self._send_question(user_id)
        except Exception as e:
            await message.answer("⚠️ Ошибка запуска теста")
            print(f"Error in start_survey: {e}")

    async def process_callback(self, callback: CallbackQuery):
        try:
            user_id = callback.from_user.id
            if user_id not in self.user_sessions:
                await callback.answer("❌ Сессия устарела", show_alert=True)
                return

            data_parts = callback.data.split('_')
            if len(data_parts) < 3:
                await callback.answer("❌ Некорректные данные")
                return

            if data_parts[0] == 'survey':
                _, q_num_str, field, value = data_parts[:4]
            else:
                q_num_str, field, value = data_parts[:3]

            try:
                q_num = int(q_num_str)
            except ValueError:
                await callback.answer("❌ Некорректный номер вопроса")
                return

            session = self.user_sessions[user_id]
            session["answers"][field] = value
            session["current_q"] = q_num + 1

            await callback.message.delete()

            if q_num >= 10:
                await self._complete_survey(user_id, callback.message)
            else:
                await self._send_question(user_id)

        except Exception as e:
            await callback.answer("⚠️ Ошибка обработки")
            print(f"Error in process_callback: {e}")

    async def _send_question(self, user_id: int):
        session = self.user_sessions.get(user_id)
        if not session:
            return

        current_q = session["current_q"]
        question_text = self._get_question_text(current_q)
        keyboard = get_survey_keyboard(current_q)

        await self.bot.send_message(
            user_id,
            question_text,
            reply_markup=keyboard
        )

    def _get_question_text(self, q_num: int) -> str:
        """Возвращает красочные вопросы с эмодзи"""
        questions = [
            "1. 🌈 Выбери свой любимый цвет из предложенных вариантов:",
            "2. 🍴 Какая кухня и какое блюдо тебе нравятся больше всего?",
            "3. 🎥 Какой фильм или сериал ты мог бы пересматривать бесконечно?",
            "4. 🎧 Под какую музыку ты любишь расслабляться или танцевать?",
            "5. 🌸❄️☀️🍂 Какое время года поднимает тебе настроение?",
            "6. 🧃 Какой напиток ты предпочитаешь в повседневной жизни?",
            "7. ✈️ Где и как ты идеально проводишь свой отдых?",
            "8. 🐶 Если бы ты мог завести любое животное, кого бы выбрал?",
            "9. 🎄 Какой праздник для тебя самый особенный?",
            "10. 🏆 Какой вид спорта тебе интересен как зрителю или участнику?"
        ]

        return questions[q_num - 1] if 1 <= q_num <= 10 else "🚫 Такого вопроса нет в опросе"

    async def _complete_survey(self, user_id: int, message: Message):
        from completion import save_answers
        session = self.user_sessions.pop(user_id, None)
        if not session:
            return

        success = await save_answers(user_id, session["answers"], "self")
        if success:
            await message.answer(
                "✅ Тест сохранен! Поделитесь ссылкой:\n"
                f"https://t.me/vorchateg_bot?start={user_id}",
                reply_markup=main_menu
            )
        else:
            await message.answer("⚠️ Не удалось сохранить тест")
