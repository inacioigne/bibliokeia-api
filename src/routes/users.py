from fastapi import APIRouter, Depends, Form, HTTPException
from src.schemas.users import UsuarioResponse, UserCreateRequest
from src.db.models import User

router = APIRouter()

@router.post("/", response_model=UsuarioResponse)
async def add_item(create_request: UserCreateRequest):
    atributos = create_request.dict(exclude_unset=True)
    usuario = User(**atributos)
    return await usuario.save()