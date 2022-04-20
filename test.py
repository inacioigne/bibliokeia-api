import json
from src.db.init_db import session
from src.db.models import Item, Exemplar, User
from src.schemas.request.cataloguing.item import Marc_Bibliographic, Field_Marc
from copy import deepcopy
from datetime import datetime
from sqlalchemy import delete

ex = session.query(Exemplar).filter_by(id = 22).first()
session.delete(ex)
session.commit()

# stmt = (
#     delete(Exemplar).
#     where(Exemplar.id == 5)
# )