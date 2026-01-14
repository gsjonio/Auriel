"""
Pytest fixtures for async testing.

:module: test.conftest
"""

import pytest_asyncio
from httpx import AsyncClient

from main import app


@pytest_asyncio.fixture
async def async_client():
    """
    Provides an `httpx.AsyncClient` for testing FastAPI app.

    :yield: AsyncClient
    """
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
