import asyncio
from handlers.client import Client
from signature import Mybot

from middlewares.check_sub import Checked


async def start():
    bot_instance = Mybot()

    await bot_instance.db.create_tables()

    bot_instance.dp.message.middleware(Checked())
    handlers = Client(bot_instance)
    
    print("""
        𝙱𝚈 𝙱𝙱𝚈𝙻𝙵𝙶 𝙰𝙽𝙳 𝚃𝙷𝙴𝚈𝚆𝙷𝙾𝚁𝙴𝙵 𝚃𝙴𝙰𝙼 𝙱𝚈 𝙷𝚂
    """)

    await handlers.register_handler()
    await bot_instance.dp.start_polling(bot_instance.bot)
    

if __name__ == '__main__':
    asyncio.run(start())