import json
from src.db.init_db import session
from src.db.models import Item, Exemplar, User
from src.schemas.request.cataloguing.item import Marc_Bibliographic, Field_Marc
from copy import deepcopy
from datetime import datetime

item = session.query(Item).filter_by(id = 14).first()

e = Exemplar(
            number = "52",
            callnumber = "597",
            library = "biblioteca",
            status = "Disponível",
            collection = "Obras Gerais"
            )

item.exemplares.append(e)

ex = {
  "exemplares": [
    {
      "number": "22-001",
      "callnumber": "597",
      "volume": "string",
      "library": "string",
      "shelf": "string",
      "status": "string",
      "collection": "string"
    }
  ]
}
