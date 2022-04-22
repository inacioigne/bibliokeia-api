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



item = session.query(Item).filter_by(id = 1).first()


