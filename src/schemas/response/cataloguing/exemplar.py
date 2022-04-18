from pydantic import BaseModel
from typing import Optional, List


class Exe_Schema(BaseModel):
  id: int
  library: str
  shelf: Optional[str]
  callnumber: str
  collection: Optional[str]
  volume: Optional[str]
  ex: Optional[str]
  number: str
  status: Optional[str]
  


class Response_Exemplares(BaseModel):
  exemplares: List[Exe_Schema]