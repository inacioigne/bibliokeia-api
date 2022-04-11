from pydantic import BaseModel, ValidationError
from typing import Optional
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from src.db.models import User
from security import SECRET_KEY, JWT_ALGORITHM
from jose import jwt
from src.db.init_db import session

class TokenPayload(BaseModel):
    sub: Optional[int] = None

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl="/usuarios/login"
)

async def get_usuario_logado(
    token: str = Depends(reusable_oauth2)
) -> User:
    try:
        payload = jwt.decode(
            token, SECRET_KEY, algorithms=[JWT_ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    #user = await User.objects.get_or_none(id=token_data.sub)
    user = session.query(User).filter_by(id = token_data.sub).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user