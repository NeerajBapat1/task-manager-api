# Task Management API

This is a FastAPI-based Task Management API that allows users to register, authenticate, and manage tasks.

## Features
- User Registration & Authentication (JWT-based)
- Task CRUD operations (Create, Read, Update, Delete)
- Secure endpoints for authenticated users
- SQLite database with SQLAlchemy ORM
- Background task reminders for upcoming tasks
- Auto-generated API documentation at `/docs`

## Installation

1. **Clone the repository:**
   git clone https://github.com/NeerajBapat1/task-manager-api.git
   cd task-manager-api

2. **Create a virtual environment:**
- python -m venv venv or virtualenv venv
# Linus/Mac: source venv/bin/activate    
# Windows: venv\Scripts\activate

3. **Install dependencies:**
- pip install -r requirements.txt

4. **Run the FastAPI app:**
- uvicorn app.main:app --reload
# OR
- python run.py

## API Endpoints

# Authentication

- POST /register → Register a new user
- POST /login → Authenticate and return a JWT token

# Task Management
- GET /tasks → Fetch all tasks (only for authenticated users)
- POST /tasks → Create a new task
- PUT /tasks/{task_id} → Update a task
- DELETE /tasks/{task_id} → Delete a task

# API Documentation
Once the server is running, you can view the API documentation at:

- Swagger UI → http://127.0.0.1:8000/docs
- Redoc → http://127.0.0.1:8000/redoc

# Testing with Postman
- Import the postman/task_manager.postman_collection.json file into Postman and test the endpoints.