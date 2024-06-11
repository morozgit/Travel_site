import pytest
from httpx import AsyncClient

# @pytest.mark.asyncio
# async def test_get_locations():
#     transport = ASGITransport(app=app)
#     async with AsyncClient(transport=transport, base_url="http://test") as client:
#         response = await client.get("/location/all_location")
#         assert response.status_code == 200

# @pytest.mark.asyncio
# async def test_get_location():
#     transport = ASGITransport(app=app)
#     async with AsyncClient(transport=transport, base_url="http://test") as client:
#         response = await client.get("/location/2")
#         assert response.status_code == 200
@pytest.mark.asyncio
async def test_get_locations(ac: AsyncClient):
    response = await ac.get("/location/all_location")
    print(response)
    assert response.status_code == 200