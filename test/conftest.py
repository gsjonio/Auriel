"""
Pytest fixtures for async testing.

:module: test.conftest
"""

import pytest_asyncio
from httpx import ASGITransport, AsyncClient

from main import app


@pytest_asyncio.fixture
async def async_client():
    """
    Provides an `httpx.AsyncClient` for testing FastAPI app via ASGI transport.

    :yield: AsyncClient
    """
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
