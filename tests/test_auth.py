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
    email = f"test_{uuid4()}@test.com"
    response_register = client.post(
       "/register",
       json={"email": email,
             "password": "123456",}
   )
    assert response_register.status_code == 200

    response_login = client.post(
        "/login",
        data={"username": email,
              "password": "123456"}
    )
    assert response_login.status_code == 200

    data = response_login.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"
