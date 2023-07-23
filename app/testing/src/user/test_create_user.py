import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_user(client: AsyncClient, supervisor_headers):
    body = {
        "email": "user@example.com",
        "password": "username"
    }
    response = await client.post("/user", json=body, headers=supervisor_headers)
    assert response.status_code == 200

# test_apis.py
def test_create_user(test_client):
    response = test_client.post("/users", json={"name": "John"})
    assert response.status_code == 200
    assert response.json()["name"] == "John"