from pydantic import BaseModel
from typing import Dict


class Marc_Bibliographic(BaseModel):
    leader: str
    controlfield: Dict
    datafield: Dict