# conftest.py
import pytest
from fastapi.testclient import TestClient
from api.user.routes import router

@pytest.fixture(scope="module")
def test_client():
    return TestClient(router)