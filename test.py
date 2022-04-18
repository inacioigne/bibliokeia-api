import json
from src.db.init_db import session
from src.db.models import Item, Exemplar, User
from src.schemas.request.cataloguing.item import Marc_Bibliographic, Field_Marc
from copy import deepcopy
from datetime import datetime

ex = session.query(Exemplar).order_by(Exemplar.id.desc()).first()