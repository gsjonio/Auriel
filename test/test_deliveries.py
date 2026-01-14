"""
Tests for deliveries endpoints using in-memory SQLite.

:module: test.test_deliveries
"""

import pytest
import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from database.session import get_session
from main import app
from models.base import Base


@pytest_asyncio.fixture
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


@pytest_asyncio.fixture
async def test_app(db_session):
    async def get_test_session():
        async with db_session as s:
            yield s

    app.dependency_overrides[get_session] = get_test_session
    yield app
    app.dependency_overrides.pop(get_session, None)


@pytest.mark.asyncio
async def test_create_and_get_delivery(db_session):
    async def get_test_session():
        yield db_session

    app.dependency_overrides[get_session] = get_test_session
    async with AsyncClient(app=app, base_url="http://test") as ac:
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
    app.dependency_overrides.pop(get_session, None)


@pytest.mark.asyncio
async def test_delete_delivery(db_session):
    async def get_test_session():
        yield db_session

    app.dependency_overrides[get_session] = get_test_session
    async with AsyncClient(app=app, base_url="http://test") as ac:
        payload = {
            "recipient_name": "To Delete",
            "description": "To be deleted",
            "tracking_number": "DEL123",
        }
        res = await ac.post("/deliveries/", json=payload)
        assert res.status_code == 201
        did = res.json()["id"]
        resdel = await ac.delete(f"/deliveries/{did}")
        assert resdel.status_code == 204
        resget = await ac.get(f"/deliveries/{did}")
        assert resget.status_code == 404
    app.dependency_overrides.pop(get_session, None)


@pytest.mark.asyncio
async def test_delete_not_found(db_session):
    async def get_test_session():
        yield db_session

    app.dependency_overrides[get_session] = get_test_session
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resdel = await ac.delete("/deliveries/9999")
        assert resdel.status_code == 404
    app.dependency_overrides.pop(get_session, None)
