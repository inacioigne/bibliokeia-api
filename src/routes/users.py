import imp
from fastapi import APIRouter, Depends, Form, HTTPException
from src.schemas.users import UsuarioResponse, UserCreateRequest
from src.schemas.response.user_response import UserResponse
from src.db.models import User
from pydantic import BaseModel
from src.db.init_db import session
from typing import List
from src.utils.getAll import get_all
from security import verify_password, criar_token_jwt

router = APIRouter()

class Response(BaseModel):
    msg: str

@router.post("/", response_model=UserResponse)
async def add_item(create_request: UserCreateRequest):
    atributos = create_request.dict(exclude_unset=True)
    user = User(**atributos)
    session.add(user)
    session.commit()

    return  {'id':user.id,'name':user.name,'email':user.email}

@router.get("/")
@get_all(User)
async def list_item():
    pass

@router.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    user = session.query(User).filter_by(name = username).first()
    #user = await User.objects.get_or_none(email=username)
    if not user or not verify_password(password, user.hash_password):
        raise HTTPException(status_code=403,
                            detail="Email ou nome de usuário incorretos"
                           )
    return {
        "access_token": criar_token_jwt({'id': user.id, 'name': user.name} ),
        "token_type": "bearer",
        "user": {"id": user.id, "name": user.name }
    }
 