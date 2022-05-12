import os
from datetime import datetime, timedelta
from typing import Any, Union, Dict
from jose import jwt
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")

SECRET_KEY = os.getenv('SECRET_KEY', 'sadasddsadsasad')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM', 'HS512')
ACCESS_TOKEN_EXPIRE_HOURS = 24

def criar_token_jwt(subject: Union[Dict, Any]) -> str:
    expire = datetime.utcnow() + timedelta(
        hours=ACCESS_TOKEN_EXPIRE_HOURS
    )
    to_encode = {"exp": expire, "sub": dict(subject)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS512")
    return encoded_jwt

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
