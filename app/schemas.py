from pydantic import BaseModel
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    description: str
    day: str

class TaskCreate(TaskBase):
    id: int

class Task(TaskBase):
    id: int
    created_at: datetime

# class TaskUpdate(BaseModel):
#     id: int
#     title: str
#     description: str
#     day: str