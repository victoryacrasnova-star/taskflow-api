from uuid import uuid4
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register():
    email  = f"test_{uuid4()}@test.com"

    response = client.post(
        "/register",
        json={
            "email": email,
            "password": "123456",
        }
    )
    assert response.status_code == 200

def test_login():
    response = client.post(
        "/login",
        data={
            "username": "test@test.com",
            "password": "123456",
        }
    )
    assert response.status_code == 200