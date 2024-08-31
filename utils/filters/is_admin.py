from aiogram.types import Message
from aiogram.filters import BaseFilter

from signature import bot_instance
from keyboards.client_kb import UserInlineKb as inline


class IsAdmin(BaseFilter):
    async def __call__(self, m: Message) -> bool:
        if await bot_instance.db.check_admins(uid=m.from_user.id):
            await m.answer("<b>tracker-bot</b> - Главная страница", reply_markup=await inline.main_menu_admin())
