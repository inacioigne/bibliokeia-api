import json
from src.db.init_db import session
from src.db.models import Item, Exemplar, User
from src.schemas.request.cataloguing.item import Marc_Bibliographic, Field_Marc
from copy import deepcopy
from datetime import datetime

marc = {
  "leader": "00861cam a22002777  4500",
  "controlfields": {
    "003": "BR-RjBN",
    "005": "19970609210000.0",
    "008": "900209n00001989brj           000 0 por u"
  },
  "datafields": {
    "082": {
      "indicators": {
        "Ind1": "0",
        "Ind2": "4"
      },
      "subfields": {
        "a": "851"
      }
    },
    "100": {
      "indicators": {
        "Ind1": "0",
        "Ind2": "#"
      },
      "subfields": {
        "a": "Dante Alighieri,", 
        "d": "1265-1321"
      }
    }, 
    "245": {
      "indicators": {
        "Ind1": "1",
        "Ind2": "2"
      },
      "subfields": {
        "a": "A divina comedia", 
        "b": "em forma de narrativa",
        "c": "Dante ; traducao de Cordelia Dias d'Aguiar ; introducao, notas e revisao do texto Assis Brasil. -"
      }
    }
  }
}

#r = Marc_Bibliographic(**marc)