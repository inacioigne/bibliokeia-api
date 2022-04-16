from pydantic import BaseModel
from typing import Dict


class Marc_Bibliographic(BaseModel):
    leader: str
    controlfields: Dict
    datafields: Dict

class Field_Marc(BaseModel):
    tag: str
    subfields: Dict