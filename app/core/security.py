from jose import jwt
from pwdlib import PasswordHash
from datetime import datetime, timedelta

from app.schemas import UserResponse

SECRET_KEY = "hfg46565787"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(email: str) -> str:

    payload = {
        "sub": email,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    return jwt.encode(
        payload,SECRET_KEY,
        algorithm=ALGORITHM
    )

def decode_access_token(token: str) -> str:
    payload = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )
    return payload["sub"]

password_hash = PasswordHash.recommended()

def hash_password(password: str) -> str:
    return password_hash.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_hash.verify(plain_password, hashed_password)


