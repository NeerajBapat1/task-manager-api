import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_task():
    token_response = client.post("/login", json={"username": "testuser", "password": "testpass"})
    token = token_response.json()["access_token"]

    response = client.post("/tasks",
                           json={"title": "New Task", "description": "Test task", "due_date": "2025-03-20T10:00:00"},
                           headers={"Authorization": f"Bearer {token}"})
    
    assert response.status_code == 200
    assert response.json()["title"] == "New Task"

def test_get_tasks():
    token_response = client.post("/login", json={"username": "testuser", "password": "testpass"})
    token = token_response.json()["access_token"]

    response = client.get("/tasks", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)