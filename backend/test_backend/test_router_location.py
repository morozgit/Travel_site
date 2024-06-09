import httpx
from fastapi.testclient import TestClient

from backend.main import app
import pytest

client = TestClient(app)


@pytest.mark.asyncio
async def test_get_locations():
  response = client.get("location/all_location")
  print('response', response)
  assert response.status_code == 200


# @pytest.mark.asyncio
# async def test_get_location():
#   response = client.get("location/2")
#   print('response', response)
#   assert response.status_code == 200