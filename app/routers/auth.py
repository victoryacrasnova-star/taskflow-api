from fastapi import APIRouter, HTTPException


from app.core.security import hash_password, verify_password, create_access_token, decode_access_token
from app.database import SessionLocal
from app.schemas import UserCreate, UserResponse, UserLogin, Token, TokenData
from app.models import User
from fastapi import Request, Depends
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

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

@router.post("/login", response_model=Token)
def login(user: UserLogin):
    db = SessionLocal()
    try:
        existing_user = db.query(User).filter(User.email == user.email).first()
        if existing_user is None:
            raise HTTPException(status_code=401, detail="Invalid email or password")

        if verify_password(user.password, existing_user.password_hash) is False:
            raise HTTPException(status_code=401, detail="Invalid email or password")

        access_token = create_access_token(existing_user.email)
        return {
            "access_token": access_token,
            "token_type": "bearer"
            }
    finally:
        db.close()

@router.get("/me", response_model=UserResponse)
def me(token = Depends(oauth2_scheme)):
    db = SessionLocal()
    try:

        email = decode_access_token(token)
        user = db.query(User).filter(User.email == email).first()
        if user is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return user
    finally:
        db.close()
