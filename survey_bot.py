from aiogram import Bot
from aiogram.types import Message

class Survey:
    def __init__(self, bot: Bot):
        self.bot = bot
        self.user_sessions = {}

    async def start_survey(self, message: Message):
        user_id = message.from_user.id
        self.user_sessions[user_id] = {"answers": {}, "current_q": 1}
        await self._send_question(user_id)

    async def _send_question(self, user_id: int):
        current_q = self.user_sessions[user_id]["current_q"]
        await self.bot.send_message(user_id, f"Вопрос {current_q}")