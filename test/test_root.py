"""
Basic tests for root endpoints.

:module: test.test_root
"""

import pytest


@pytest.mark.asyncio
async def test_root(async_client):
    response = await async_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
