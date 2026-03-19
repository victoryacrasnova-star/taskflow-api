from fastapi import APIRouter, HTTPException

from app.core.security import hash_password, verify_password
from app.database import SessionLocal
from app.schemas import UserCreate, UserResponse, UserLogin
from app.models import User

router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate):
    db = SessionLocal()

    try:

        existing_user = db.query(User).filter(User.email == user.email).first()
        if existing_user:
            raise HTTPException(status_code=409, detail="Email already registered")

        hashed_password = hash_password(user.password)

        new_user = User(
            email=user.email,
            password_hash=hashed_password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"id": new_user.id,
                "email": new_user.email}
    finally:
        db.close()

@router.post("/login")
def login(user: UserLogin):
    db = SessionLocal()
    try:
        existing_user = db.query(User).filter(User.email == user.email).first()
        if existing_user is None:
            raise HTTPException(status_code=401, detail="Email or password not correct")
        if verify_password(user.password, existing_user.password_hash) is False:
            raise HTTPException(status_code=401, detail="Email or password not correct")
        else:
            return {"message": "Login successful"}

    finally:
        db.close()