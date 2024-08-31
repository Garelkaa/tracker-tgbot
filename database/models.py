import aiosqlite

class Database:
    def __init__(self, db_file) -> None:
        self.db_file = db_file


    async def connect(self):
        self.conn = await aiosqlite.connect(self.db_file)


    async def create_tables(self):
        async with aiosqlite.connect(self.db_file) as db:
            await db.execute('''
                CREATE TABLE IF NOT EXISTS track_code_entity (
                    id INTEGER PRIMARY KEY,
                    code varchar(255) NOT NULL,
                    deletedAt timestamp(6) NULL DEFAULT NULL,
                    createdAt double NOT NULL,
                    updatedAt double NOT NULL DEFAULT 0,
                    createdById double DEFAULT NULL,
                    updatedById double DEFAULT NULL,
                    deletedById double DEFAULT NULL,
                    receiver text NOT NULL,
                    status tinyint NOT NULL
                )
            ''')

            await db.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    uid INTEGER,
                    url TEXT,
                    status INTEGER DEFAULT 0
                )
            ''')

            await db.commit()


    async def get_track_code(self, code: int):
        async with aiosqlite.connect(self.db_file) as db:
            resp = await db.execute("SELECT * FROM track_code_entity WHERE code = ?", (code,))

            result = await resp.fetchone()
            return bool(result)


    async def check_admins(self, uid: int):
        async with aiosqlite.connect(self.db_file) as db:
            resp = await db.execute('''SELECT * FROM users WHERE uid = ?''', (uid,))

            return bool(await resp.fetchone())


    async def get_admins(self):
        ...
