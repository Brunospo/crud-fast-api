from models.postgresql.settings.base import Base
from models.postgresql.settings.connection import db_connection_handler

async def create_tables() -> None:
    import models.postgresql.entities.course
    print('Criando Banco de dados...')

    db_connection_handler.connect_to_db()
    engine = db_connection_handler.get_engine()

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        print("Tabelas criadas co sucesso")

if __name__ == '__main__':
    import asyncio

    asyncio.run(create_tables())
    