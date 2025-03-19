from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_register_user():
    response = client.post("/auth/register", json={
        "full_name": "John Doe",
        "email": "john@example.com",
        "password": "test123",
        "role": "user"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_user():
    response = client.post("/auth/login", data={
        "username": "john@example.com",
        "password": "test123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()
