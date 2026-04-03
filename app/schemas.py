from pydantic import BaseModel, ConfigDict
from typing import Optional

"""USER"""

class UserCreate(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str

class UserLogin(BaseModel):
    email: str
    password: str

"""TOKEN"""

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    access_token: str

"""Project CRUD"""

class ProjectCreate(BaseModel):
    name: str
    description: str

class ProjectRead(BaseModel):
    id: int
    name: str
    description: str
    owner_id: int

    model_config = ConfigDict(from_attributes=True)

class ProjectUpdate(BaseModel):
    name: str
    description: str

"""Task CRUD""" #доработать, добавить опциональность

class TaskCreate(BaseModel):
    description: str
    title: str
    assignee_id: int = None

class TaskRead(BaseModel):
    id: int
    status: str
    description: str
    title: str
    project_id: int
    assignee_id: int = None

    model_config = ConfigDict(from_attributes=True)

class TaskUpdate(BaseModel):
    optional: bool
    status: str
    description: str
    title: str
    project_id: int

"""Task Status CRUD"""

class TaskStatus(BaseModel): #доработать, добавить опциональность
    new: bool
    in_progress: bool
    done: bool
