from src.db.init_db import session
from src.db.models import Item, Exemplar, User
from src.schemas.marc_schemas import Marc_Bibliographic, Exemplar_Schema
from pydantic import BaseModel
from typing import Dict, List, Optional
from copy import deepcopy
from datetime import date

from src.db.init_db import initializeDatabase

initializeDatabase()


item = Item()








