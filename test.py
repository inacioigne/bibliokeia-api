from src.db.init_db import session
from src.db.models import Item, Exemplar
from src.schemas.marc_schemas import Marc_Bibliographic, Exemplar_Schema
from pydantic import BaseModel
from typing import Dict, List, Optional
from copy import deepcopy
from datetime import date

item = session.query(Item).filter_by(id = 1 ).first()

def get_exemplares(item):
  exs  = list()
  for ex in item.exemplares:
    d = ex.__dict__
    d.pop('_sa_instance_state')
    
    exs.append(
      d
    )
  return exs

x = get_exemplares(item)







