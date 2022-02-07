from src.db.init_db import session
from src.db.models import Item
from src.schemas.requests_body import Model_Item, Model_Item_Edit
#from src.schemas.marc_schemas import Marc_Bibliographic
from src.functions.cataloguing import edit_item
import xml.etree.ElementTree as et
from xml.dom import minidom
import httpx
import json
import re
from sqlalchemy import update
from copy import deepcopy
import collections
from random import randint
from pydantic import BaseModel
from typing import Dict, List, Optional


class Tag_245(BaseModel):
    a: str

class Datafield(BaseModel):
    tag_245: Tag_245

class Controlfield(BaseModel):
  tag_008: str

class Marc_Bibliographic(BaseModel):
    leader = '01602cam a2200325 a 4500'
    controlfield = Controlfield
    datafield: Datafield

record = Marc_Bibliographic(
  datafield=Datafield(tag_245={'a': 'A poesia mineira no século XX'})

record.json()

    """
j = json.dumps(Marc_Bibliographic.schema(), indent=2)
with open('schema.json', 'w') as out:
  out.write(j)



datafield = Datafield(tag_245={'a': 'A poesia mineira no século XX'})

record = Marc_Bibliographic(
  datafield=Datafield(tag_245={'a': 'A poesia mineira no século XX'})
)"""