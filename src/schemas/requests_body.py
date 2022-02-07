from pydantic import BaseModel
from typing import Dict, List, Optional

class Test_Item(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    tax: float = 10.5
    tags: List[str] = []

class Controlfield(BaseModel):
    tag_008: str

class Model_Item_Edit(BaseModel):
    datafield: Dict = None
    controlfield = Controlfield

class Model_Item(BaseModel):
    marc_100_a: str
    marc_245_a: str
    marc_260_a: str
    marc_260_b: Optional[str] = ''
    marc_260_c: str


class Request_Item(BaseModel):
    url: str
    server: str


class Request_Authority(BaseModel):
    url: str
    server: str
    format: str

class Request_Subjects(BaseModel):
    url: str
    server: str
    format: str