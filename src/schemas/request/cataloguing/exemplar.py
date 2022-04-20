from pydantic import BaseModel
from typing import Optional, List


class Exe_Schema(BaseModel):
  library: str
  shelf: Optional[str]
  callnumber: str
  collection: Optional[str]
  volume: Optional[str]
  ex: Optional[str]
  number: str
  status: Optional[str]

class Request_Exemplares(BaseModel):
  exemplares: List[Exe_Schema]

class Request_Del_Exemplares(BaseModel):
  exemplares: List[int]

