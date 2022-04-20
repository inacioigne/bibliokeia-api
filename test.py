import json

from requests import request
from src.db.init_db import session, engine
from src.db.models import Item, Exemplar, User
from src.schemas.request.cataloguing.item import Marc_Bibliographic, Field_Marc
from src.schemas.request.cataloguing.exemplar import Request_Exemplares, Exe_Schema
from copy import deepcopy
from datetime import datetime
from sqlalchemy import delete
from sqlalchemy import inspect
from sqlalchemy import update






item = session.query(Item).filter_by(id = 15).first()


body = {
  "library": "Biblioteca do INPA",
  "shelf": "D345c",
  "callnumber": "856.2 D345c",
  "collection": "Obras Gerais",
  "volume": "v. 5",
  "ex": "ex. 10",
  "number": "22-0015",
  "status": "EMPRESTADO"
}

request = Exe_Schema(**body)

stmt = (
    update(Exemplar).
    where(Exemplar.id == 33).
    values(**request.dict())
)

session.execute(stmt)
session.commit()



