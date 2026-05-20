from uuid import uuid4
from fastapi.testclient import TestClient
from sqlalchemy.sql.functions import current_user

from app.main import app

client = TestClient(app)

def test_create_task():
    email = f"test{uuid4()}@test.com"
    password = "123456"

    register_response = client.post(
        "/register",
        json={
            "email": email,
            "password": password,
        }
    )

    assert register_response.status_code == 200

    login_response = client.post(
        "/login",
        data={
            "username": email,
            "password": password,
        }
    )

    assert login_response.status_code == 200

    token = login_response.json()["access_token"]

    project_response = client.post(
        "/projects",
        json={
            "name": "Test Project",
            "description": "Test Project",
        },
        headers={
            "Authorization": f"Bearer {token}",
        }
    )

    assert project_response.status_code == 200

    project_data = project_response.json()
    project_id = project_data["id"]
    tasks_response = client.post(
        f"/projects/{project_id}/tasks",
        json={
            "title": "Test Task",
            "description": "Test Task",
            "assignee_id": None,
            "priority": 0,
        }
    )

    assert tasks_response.status_code == 200

    tasks_data = tasks_response.json()

    assert tasks_data["title"] == "Test Task"
    assert tasks_data["description"] == "Test Task"
    assert tasks_data["project_id"] == project_id
    assert tasks_data["status"] == "new"