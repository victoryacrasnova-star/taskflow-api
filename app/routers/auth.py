from fastapi import APIRouter

from app.core.security import hash_password
from app.database import SessionLocal
from app.schemas import UserCreate
from app.models import User

router = APIRouter()

@router.post("/register")
def register(user: UserCreate):
    db=SessionLocal()

    hashed_password = hash_password(user.password)


    new_user = User(
        email=user.email,
        password_hash=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered"}
