from pydantic import BaseModel, Field, validator
from security import get_password_hash


class UsuarioResponse(BaseModel):
    id: int
    name: str
    email: str

class UserCreateRequest(BaseModel):
    name: str
    email: str
    hash_password: str = Field(alias='password')

    @validator('hash_password', pre=True)
    def hash_the_password(cls, v):
        return get_password_hash(v)