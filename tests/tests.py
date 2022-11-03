import pytest
from httpx import AsyncClient

from main import app


@pytest.mark.asyncio
async def test_post():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        params = {"url": "https://google.com"}
        response = await ac.post("/long_url", params=params)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/test")
    assert response.status_code == 200
