from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
)

import os

class DbConnectionHandler:
    def __init__(self) -> None:
        pg_user = os.getenv("POSTGRES_USER", "postgres")
        pg_pass = os.getenv("POSTGRES_PASSWORD", "postgres")
        pg_host = os.getenv("POSTGRES_HOST", "localhost")
        pg_port = os.getenv("POSTGRES_PORT", "5432")
        pg_db   = os.getenv("POSTGRES_DB",   "mydb")

        self.__connection_string = (
            f"postgresql+asyncpg://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}"
        )

        self.__engine = None
        self.session: AsyncSession = None

    def connect_to_db(self) -> None:
        
        self.__engine = create_async_engine(
            self.__connection_string,
            echo=False,
        )
    
    def get_engine(self):
        return self.__engine
    
    async def __aenter__(self):
        
        async_session = async_sessionmaker(
            self.__engine,
            expire_on_commit=False,
            class_=AsyncSession,
            autoflush=False,
        )
        
        self.session = async_session()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()

db_connection_handler = DbConnectionHandler()
