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


status_dict = {
    0: {
                        "title": 'Оформление',
                        "description": 'Ваш заказ создан, ожидает обработки данных',
                    },

                    1: {
                        "title": 'Сортировка',
                        "description": 'Данные переданы на склад, товар проходит проверку и подготавливается к отправке (2-5 дней)'
                    },

                    2: {
                        "title": 'Отправка',
                        "description": 'Заказ отправлен в РФ'
                    },

                    3: {
                        "title": 'Таможенный контроль',
                        "description": 'Груз прибыл в Россию, проходит таможенный контроль'
                    },

                    4: {
                        "title": 'Таможенное оформление завершено',
                        "description": 'Товар передан в логистическую компанию по России',
                    },

                    5: {
                        "title": 'Сортировка',
                        "description": 'Товар проходит сортировку на Московском складе, для дальнейшей отправки на Ваш адрес',
                    },

                    6: {
                        "title": 'Ожидает отправки на Ваш адрес',
                        "description": 'Товар готовят к отправке с нашего склада в Москве'
                    }
                }


class Client:
    def __init__(self, bot: Mybot):
        self.bot = bot.bot
        self.dp = bot.dp
        self.db = bot.db 
    
    
    async def register_handler(self):
        self.dp.message(CommandStart())(self.start) 
        self.dp.callback_query(F.data == "why_order")(self.why_order)
        self.dp.callback_query(F.data == 'done_sub')(self.done_sub)
        self.dp.callback_query(F.data == 'get_info')(self.info_order)
        self.dp.callback_query(F.data == 'check_code')(self.load_user_track)
        self.dp.message(GetTrack.track)(self.check_user_track)
        self.dp.callback_query(F.data == 'new_code')(self.send_new_code)
        self.dp.callback_query(F.data == 'cancel', GetTrack.track)(self.back_main_menu)


    async def start(self, m: Message):
        await m.reply("Главная страница", reply_markup=await inline.main_menu())

    
    async def done_sub(self, call: CallbackQuery):
        if call.message.chat.type == 'private':
            chat_member = await call.message.bot.get_chat_member(chat_id=sub_channel_id, user_id=call.from_user.id)
            
            if chat_member.status == 'left':
                await call.message.answer(
                    f"✅Для использования бота, вы должны быть подписаны на канал:", reply_markup=await inline.check_sub(url=sub_channel_link))
            else:
                await call.message.edit_text("Главная страница", reply_markup=await inline.main_menu())
       
    
    async def why_order(self, call: CallbackQuery):
        await call.message.reply(why_order_message)
        await self.start(m=call.message)
    

    async def load_user_track(self, call: CallbackQuery, state: FSMContext):
        
        await call.message.answer("Введите трек-код", reply_markup=await inline.info_track())
        await state.set_state(GetTrack.track)
    

    async def info_order(self, call:  CallbackQuery, state: FSMContext):
        await call.message.reply(info_message)

        await call.message.answer("Введите трек-код", reply_markup=await inline.info_track())
        await state.set_state(GetTrack.track)
        

    async def check_user_track(self, m: Message, state: FSMContext):
        if m.text.isdigit():
            resp = await self.db.get_track_code(code=int(m.text))

            if resp:
                await m.answer(f"<b>Введён трек-код</b>:\n\n {m.text}")

                dt = datetime.fromtimestamp(float(resp[4]) / float(1000)) + timedelta(hours=3)

                months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
                formatted_date = dt.strftime(f'%d-{months[dt.month - 1]} %Y в %H:%M:%S +03:00')

                send_message = track_info.format(
                    track_id=m.text,
                    status=status_dict[resp[9]]['title'],
                    desc=status_dict[resp[9]]['description'],
                    user=resp[8],
                    date=formatted_date)
                
                await m.answer(send_message, reply_markup=await inline.cancel_menu())
            else:
                await m.answer("<b>Трек-код не найден</b>")

            await state.clear()
    
    
    async def send_new_code(self, call: CallbackQuery, state: FSMContext):
        await self.load_user_track(call=call, state=state)
    

    async def back_main_menu(self, call: CallbackQuery, state: FSMContext):
        await state.clear()
        await self.start(m=call.message)
