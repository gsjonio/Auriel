"""
Async database session and engine configuration.

:param database_url: DSN for database (from env/config).
:return: `async_sessionmaker` instance for creating `AsyncSession` objects.
"""

import os
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql+asyncpg://user:pass@localhost:5432/db"
)

engine = create_async_engine(DATABASE_URL, future=True, echo=False)
async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Yield an async SQLAlchemy session.

    :yield: AsyncSession
    """
    async with async_session() as session:
        yield session
