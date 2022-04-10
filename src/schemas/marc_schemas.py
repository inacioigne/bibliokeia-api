from re import T
from pydantic import BaseModel, parse_obj_as
from typing import Dict, List, Optional



class TagMarc(BaseModel):
  tag: str
  marc: str
  subfield: Dict

class TagsMarc(BaseModel):
  id: str
  marc: Dict

class Marc_Bibliographic(BaseModel):
    leader: str
    controlfield: Dict
    datafield: Dict

class Exemplar_Schema(BaseModel):
  number: str
  callnumber: str
  volume: Optional[str]
  library: str
  shelf: Optional[str]
  status: Optional[str]
  collection: Optional[str]


class Exe(BaseModel):
  exemplares: List[Exemplar_Schema]

