import pytest
from httpx import AsyncClient

from main import app


@pytest.mark.asyncio
async def test_post():
    async with AsyncClient(app=app, base_url="http://localhost") as ac:
        params = {"url": "https://google.com"}
        response = await ac.post("/long_url", params=params)
        assert response.status_code == 200
        
        short_url = response.json()['response']
        short_url = short_url.split('/')[-1]
        response = await ac.get(f"/resolved_url/{short_url}")
        
        assert response.status_code == 200
        assert response.json() == {"resolved":"https://google.com"}
