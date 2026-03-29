from pydantic import BaseModel, ConfigDict

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

"""База TOKEN"""

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    access_token: str

"""База CRUD"""

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