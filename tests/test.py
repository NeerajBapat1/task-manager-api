import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Sample user credentials
test_user = {"username": "testuser", "password": "testpassword"}

# Test user registration
def test_register_user():
    response = client.post("/register", json=test_user)
    assert response.status_code == 201
    assert response.json()["message"] == "User registered successfully"

# Test duplicate registration
def test_register_duplicate_user():
    response = client.post("/register", json=test_user)
    assert response.status_code == 400  # Assuming you handle duplicate users
    assert "User already exists" in response.json()["detail"]

# Test login success
def test_login_success():
    response = client.post("/login", data=test_user)
    assert response.status_code == 200
    assert "access_token" in response.json()

# Test login failure (wrong password)
def test_login_wrong_password():
    response = client.post("/login", data={"username": "testuser", "password": "wrongpass"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"

# Test login failure (non-existent user)
def test_login_non_existent_user():
    response = client.post("/login", data={"username": "nouser", "password": "password123"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"

# Helper function to get auth token
def get_auth_token():
    response = client.post("/login", data=test_user)
    return response.json()["access_token"]

# Test creating a task (Success)
def test_create_task():
    token = get_auth_token()
    response = client.post(
        "/tasks",
        headers={"Authorization": f"Bearer {token}"},
        json={"title": "Test Task", "description": "This is a test task"}
    )
    assert response.status_code == 201
    assert response.json()["title"] == "Test Task"

# Test creating a task (Unauthorized)
def test_create_task_unauthorized():
    response = client.post("/tasks", json={"title": "Unauthorized Task", "description": "Should not be created"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Not authenticated"

# Test fetching all tasks (Success)
def test_get_tasks():
    token = get_auth_token()
    response = client.get("/tasks", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test fetching all tasks (Unauthorized)
def test_get_tasks_unauthorized():
    response = client.get("/tasks")
    assert response.status_code == 401
    assert response.json()["detail"] == "Not authenticated"

# Test updating a task (Success)
def test_update_task():
    token = get_auth_token()
    response = client.put(
        "/tasks/1",
        headers={"Authorization": f"Bearer {token}"},
        json={"title": "Updated Task", "description": "Updated Description", "completed": True}
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Task updated successfully"

# Test updating a non-existent task
def test_update_nonexistent_task():
    token = get_auth_token()
    response = client.put(
        "/tasks/999",
        headers={"Authorization": f"Bearer {token}"},
        json={"title": "Updated Task", "description": "Updated Description", "completed": True}
    )
    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"

# Test updating a task (Unauthorized)
def test_update_task_unauthorized():
    response = client.put(
        "/tasks/1",
        json={"title": "Updated Task", "description": "Updated Description", "completed": True}
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Not authenticated"

# Test deleting a task (Success)
def test_delete_task():
    token = get_auth_token()
    response = client.delete("/tasks/1", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()["message"] == "Task deleted successfully"

# Test deleting a non-existent task
def test_delete_nonexistent_task():
    token = get_auth_token()
    response = client.delete("/tasks/999", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"

# Test deleting a task (Unauthorized)
def test_delete_task_unauthorized():
    response = client.delete("/tasks/1")
    assert response.status_code == 401
    assert response.json()["detail"] == "Not authenticated"