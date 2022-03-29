from src.db.init_db import session
from src.db.models import Item
from src.schemas.marc_schemas import Marc_Bibliographic
from pydantic import BaseModel
from typing import Dict, List, Optional
from copy import deepcopy


class TagMarc(BaseModel):
  id: str
  tag: str
  ind1: Optional[str] = None
  ind2: Optional[str] = None
  subfields: Dict

tagMarc = {'id': '53',
 'marc': 'datafield',
  'tag': '040', 
  'ind1': 'undefined', 
  'ind2': 'undefined',
  'marc': "datafield",
  "subcampos": {
    "a":"BR-MnINPA",
    "b": "eng"
  }
  }

def update_item(tagMarc: TagMarc):
  
  item = session.query(Item).filter_by(id = tagMarc['id']).first()
  marc = deepcopy(item.marc)
  marc[tagMarc['marc']][tagMarc['tag']] = tagMarc['subcampos']

  item.marc = marc
  #session.add(item)
  session.commit()

  return item


