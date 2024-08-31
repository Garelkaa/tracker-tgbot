import asyncio
from handlers.client import Client
from handlers.admin import Admins
from signature import bot_instance

from middlewares.check_sub import Checked


async def start():
    await bot_instance.db.create_tables()

    bot_instance.dp.message.middleware(Checked())
    handlers = Client(bot_instance)
    admin = Admins(bot_instance)
    
    print("""
        𝙱𝚈 𝙱𝙱𝚈𝙻𝙵𝙶 𝙰𝙽𝙳 𝚃𝙷𝙴𝚈𝚆𝙷𝙾𝚁𝙴𝙵 𝚃𝙴𝙰𝙼 𝙱𝚈 𝙷𝚂
    """)

    await handlers.register_handler()
    await admin.register_handlers()
    await bot_instance.dp.start_polling(bot_instance.bot)
    

if __name__ == '__main__':
    asyncio.run(start())