from src.db.init_db import session
from src.db.models import Item, Exemplar
from src.schemas.marc_schemas import Marc_Bibliographic, Exemplar_Schema
from pydantic import BaseModel
from typing import Dict, List, Optional
from copy import deepcopy
from datetime import date

item = session.query(Item).filter_by(id = 5 ).first()

{"Ind1": '0', "Ind2": '0', "a": 'Os miseráveis ', "c": 'Victor Hugox'}







