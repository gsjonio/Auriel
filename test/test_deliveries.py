"""
Tests for deliveries endpoints using in-memory SQLite.

:module: test.test_deliveries
"""

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from database.session import get_session
from main import app
from models.base import Base


@pytest.fixture
async def db_session():
    engine = create_async_engine(
        "sqlite+aiosqlite:///:memory:", future=True, echo=False
    )
    async_session = async_sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
    )
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with async_session() as session:
        yield session
    await engine.dispose()


@pytest.fixture
async def test_app(db_session):
    async def get_test_session():
        async with db_session as s:
            yield s

    app.dependency_overrides[get_session] = get_test_session
    yield app
    app.dependency_overrides.pop(get_session, None)


@pytest.mark.asyncio
async def test_create_and_get_delivery(test_app):
    async with AsyncClient(app=test_app, base_url="http://test") as ac:
        payload = {
            "recipient_name": "John Doe",
            "description": "Package",
            "tracking_number": "ABC123",
        }
        res = await ac.post("/deliveries/", json=payload)
        assert res.status_code == 201
        data = res.json()
        assert data["recipient_name"] == "John Doe"
        res2 = await ac.get(f"/deliveries/{data['id']}")
        assert res2.status_code == 200
        assert res2.json()["id"] == data["id"]
