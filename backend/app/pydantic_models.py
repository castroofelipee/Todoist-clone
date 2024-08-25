from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False
    due_date: Optional[datetime] = None


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: str
    profile_pic: Optional[str] = None


class UserCreate(UserBase):
    github_id: int


class User(UserBase):
    id: int
    created_at: datetime
    tasks: list[Task] = []

    class Config:
        orm_mode = True
