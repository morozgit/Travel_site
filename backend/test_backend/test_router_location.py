import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_locations(ac: AsyncClient):
    response = await ac.get("/location/all_location")
    print(response.json())
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_get_location(ac: AsyncClient):
    response = await ac.get("/location/2")
    print(f"locations {response.json()}")
    assert response.status_code == 200