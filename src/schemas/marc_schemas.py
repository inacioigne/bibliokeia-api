from re import T
from pydantic import BaseModel, parse_obj_as
from typing import Dict, List, Optional



class TagMarc(BaseModel):
  id: str
  tag: str
  ind1: Optional[str] = None
  ind2: Optional[str] = None
  marc: str
  subcampos: Dict

class Marc_Bibliographic(BaseModel):
    leader: str
    controlfield: Dict
    datafield: Dict

