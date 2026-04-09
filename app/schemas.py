from pydantic import BaseModel, ConfigDict
from typing import Optional
from enum import Enum
from datetime import datetime

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

"""Task CRUD"""

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

class TaskStatusEnum(str, Enum):
    new = "new"
    in_progress = "in_progress"
    done = "done"

class TaskUpdate(BaseModel):
    description: Optional[str] = None
    title: Optional[str] = None
    assignee_id: Optional[int] = None
    status: Optional[TaskStatusEnum] = None

"""CRUD Comments"""

class CommentCreate(BaseModel):
    content: str
    reply_to_comment_id: Optional[int] = None

class CommentRead(BaseModel):
    id: int
    content: str
    task_id: int
    author_id: int

    reply_to_comment_id: Optional[int] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CommentUpdate(BaseModel):
    content: Optional[str] = None