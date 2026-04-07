from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.core.security import hash_password, verify_password, create_access_token, decode_access_token
from app.database import get_db
from app.schemas import UserCreate, UserResponse, UserLogin, Token
from app.models import User
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
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

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == form_data.username).first()
    if existing_user is None:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    if verify_password(form_data.password, existing_user.password_hash) is False:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    access_token = create_access_token(existing_user.email)
    return {
        "access_token": access_token,
        "token_type": "bearer"
        }

def get_current_user(token = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    email = decode_access_token(token)
    if email is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    return user

@router.get("/me", response_model=UserResponse)
def me(current_user: User = Depends(get_current_user)):
    return current_user