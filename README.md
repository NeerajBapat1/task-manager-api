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
# Linux/Mac: source venv/bin/activate    
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

- Redoc → http://127.0.0.1:8000/redoc
- Swagger UI → http://127.0.0.1:8000/docs

## How to authorize in Swagger UI:

1. Obtain a JWT Token:
- Navigate to the '/login/' endpoint in Swagger UI.
- Click "Try it out" and enter your username and password.
- Click "Execute" to send the request.
- If the credentials are correct, the API will return a response containing a JWT token:
  {
  "access_token": "your_generated_token_here",
  "token_type": "bearer"
   }

2. Authorize Using the Token:
- Click the 'Authorize' button in the top right corner of Swagger UI.
- Enter your token in the format:
   Bearer "your_generated_token_here"
- Click 'Authorize' and then Close.

3. Revoking the Authorization:
- Click the 'Authorize' button again.
- Click 'Logout' to revoke the token.

# Testing with Postman
- Import the postman/task_manager.postman_collection.json file into Postman and test the endpoints.

## Testing with Pytest:

- pip install pytest
- pytest test.py