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
  edition: Optional[str]
  year: Optional[str]
  volume: Optional[str]
  library: str
  shelf: Optional[str]
  status: Optional[str]
  collection: Optional[str]

class Exe(BaseModel):
  exs: List[Exemplar_Schema]

