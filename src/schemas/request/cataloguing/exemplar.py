from pydantic import BaseModel
from typing import Optional, List


class Exe_Schema(BaseModel):
  number: str
  callnumber: str
  volume: Optional[str]
  library: str
  shelf: Optional[str]
  status: Optional[str]
  collection: Optional[str]


class Exemplares(BaseModel):
  exemplares: List[Exe_Schema]