from aiogram import Bot, Dispatcher
import config as cfg

from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from database.models import Database


class Mybot:
    def __init__(self):
        self.bot = Bot(token=cfg.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
        self.dp = Dispatcher()
        self.db = Database('db.db')
        