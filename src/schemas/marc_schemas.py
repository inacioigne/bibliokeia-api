from re import T
from pydantic import BaseModel, parse_obj_as
from typing import Dict, List, Optional



class Tag_100(BaseModel):
    a: Optional[str]
    d: Optional[str]

class Tag_245(BaseModel):
    a: Optional[str]
    b: Optional[str]

class Tag_300(BaseModel):
    a: Optional[str]
    c: Optional[str]

class Tag_490(BaseModel):
    a: Optional[str]
    v: Optional[str]

class Tag_500(BaseModel):
    a: Optional[str]

class Tag_650(BaseModel):
    a: Optional[str]

class Tag_700(BaseModel):
    a: Optional[str]

class Tag_800(BaseModel):
    a: Optional[str]

class Datafield(BaseModel):
    tag_100: Optional[Tag_100]
    tag_245: Optional[Tag_245]
    tag_300: Optional[Tag_300]
    tag_490: Optional[Tag_490]
    tag_500: Optional[Tag_500]
    tag_650: Optional[Tag_650]
    tag_700: Optional[Tag_700]
    tag_800: Optional[Tag_800]

    

class Controlfield(BaseModel):
  tag_008: str

class Marc_Bibliographic(BaseModel):
    leader: str
    controlfield: List[Dict]
    datafield: List[Dict]

