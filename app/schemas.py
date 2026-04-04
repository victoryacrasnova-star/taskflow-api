from anyio.abc import TaskStatus
from pydantic import BaseModel, ConfigDict
from typing import Optional
from enum import Enum

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
    title: str

    description: Optional[str] = None
    assignee_id: Optional[int] = None

class TaskRead(BaseModel):
    id: int
    status: str
    title: str
    project_id: int

    description: Optional[str] = None
    assignee_id: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)

class TaskUpdate(BaseModel):
    description: Optional[str] = None
    title: Optional[str] = None
    assignee_id: Optional[int] = None


"""Task Status CRUD"""

class TaskStatusEnum(str, Enum):
    new = "new"
    in_progress = "in_progress"
    done = "done"

class TaskStatusUpdate(BaseModel): #доработать, добавить опциональность
    status: TaskStatusEnum