from uuid import uuid4
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

"""
1. Авторизация
2. Логин
3. Создание проекта
4. Создание задачи
"""

def test_create_task():
    email = f'test{uuid4()}@test.com'
    password = '123456'

    register_response = client.post(
        '/register',
        json={
            'email': email,
            'password': password,
        }
    )

    assert register_response.status_code == 200

    login_response = client.post(
        '/login',
        data={
            'username': email,
            'password': password,
        }
    )

    assert login_response.status_code == 200

    token = login_response.json()['access_token']

    project_response = client.post(
        '/projects',
        json={
            'name': "Test Project",
            'description': "Test Description",
        },
        headers = {
            'Authorization': f'Bearer {token}',
        }
    )
    assert project_response.status_code == 200

    project_data = project_response.json()
    project_id = project_data['id']

    task_response = client.post(
        f'/projects/{project_id}/tasks',
        json={
            "title": "Test Task",
            "description": "Test Description",
            "assignee_id":  None,
            "priority": 0
        },
        headers = {
            'Authorization': f'Bearer {token}',
        }
    )
    assert task_response.status_code == 200

    task_data = task_response.json()

    assert task_data['title'] == "Test Task"
    assert task_data['description'] == "Test Description"
    assert task_data['status'] == "new"
    assert task_data['project_id'] == project_id