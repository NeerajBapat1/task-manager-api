from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class User(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6)

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    due_date: datetime
    owner_id: int

    class Config:
        from_attributes = True
        
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = None
    due_date: datetime

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    due_date: datetime
    owner_id: int

    class Config:
        from_attributes = True
        
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[datetime] = None