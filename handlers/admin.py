from aiogram import F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from signature import Mybot
from keyboards.client_kb import UserInlineKb as inline
from aiogram.fsm.context import FSMContext

from .text import why_order_message, info_message, track_info
from utils.user_state import GetTrack
from config import sub_channel_id, sub_channel_link

from datetime import datetime, timedelta


class Admins:
    def __init__(self, bot: Mybot) -> None:
        self.bot = bot.bot
        self.dp = bot.dp
        self.db = bot.db
    

    async def register_handlers(self):
        ...


    async def get_admins_bot(self, call: CallbackQuery):
        ...