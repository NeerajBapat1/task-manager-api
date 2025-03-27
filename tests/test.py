import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import get_db, SessionLocal

client = TestClient(app)

def override_get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# User Authentication Tests
def test_register_user():
    response = client.post("/register/", json={"username": "testuser", "password": "testpassword"})
    assert response.status_code == 200

def test_login_user():
    response = client.post("/login/", json={"username": "testuser", "password": "testpassword"})
    assert response.status_code == 200
    return response.json()["access_token"]

# Task Management Tests
def test_create_task():
    token = test_login_user()
    response = client.post("/tasks/", json={"title": "Test Task", "description": "Task Description", "due_date": "2025-04-01T00:00:00"}, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200

def test_get_tasks():
    token = test_login_user()
    response = client.get("/tasks/", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200

def test_update_task():
    token = test_login_user()
    response = client.put("/tasks/1", json={"title": "Updated Task"}, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200

def test_delete_task():
    token = test_login_user()
    response = client.delete("/tasks/1", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200

def test_send_reminder():
    response = client.post("/background-tasks/")
    assert response.status_code == 200