from uuid import uuid4

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_project_without_token():
    response = client.post(
        "/projects",
        json={
            "name": "Test Project",
            "description": "Test description",
        }
    )
    assert response.status_code == 401

def test_create_project_with_token():
    email = f"test_{uuid4()}@test.com"
    register_response = client.post(
        "/register",
        json={
            "email": email,
            "password": "123456",
        }
    )
    assert register_response.status_code == 200

    login_response = client.post(
        "/login",
        data={
            "username": email,
            "password": "123456",
        }
    )

    assert login_response.status_code == 200

    data = login_response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"

    token = data["access_token"]

    project_response = client.post(
        "/projects",
        json={
            "name": "Test Project",
            "description": "Test description",
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    assert project_response.status_code == 200

    project_data = project_response.json()

    assert project_data["name"] == "Test Project"
    assert project_data["description"] == "Test description"
    assert "owner_id" in project_data
