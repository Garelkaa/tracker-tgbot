from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Any, Awaitable, Dict, Callable

from keyboards.client_kb import UserInlineKb as inline
from config import sub_channel_id, sub_channel_link

from signature import Mybot


class Checked(BaseMiddleware):
    async def __call__(self,
                       handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
                       event: Message,
                       data: Dict[str, Any]
                       ) -> Any:
        
        
        if await Mybot.db.check_admins(uid=event.from_user.id):
            await event.answer("<b>tracker-bot</b> - Главная страница", reply_markup=inline.main_menu_admin())
        else:
            return await handler(event, data)

        
        if event.from_user.username is not None:
            return await handler(event, data)
        else:
            await event.answer(
                "<b>Для продолжения использования бота, необходимо включить отображение никнейма.</b>"
            )
        if event.chat.type == 'private':
            chat_member = await event.bot.get_chat_member(chat_id=sub_channel_id, user_id=event.from_user.id)
            if chat_member.status == 'left':
                await event.answer(
                    f"✅Для использования бота, вы должны быть подписаны на канал:", reply_markup=await inline.check_sub(url=sub_channel_link)
                )
            else:
                return await handler(event, data)
        else:
            return await handler(event, data)
        