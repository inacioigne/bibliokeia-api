from fastapi import APIRouter, Depends
from src.auth.login import get_usuario_logado
from src.schemas.requests_body import Model_Item, Model_Item_Edit
from src.schemas.marc_schemas import Marc_Bibliographic, TagMarc, TagsMarc, Exemplar_Schema, Exe
from src.functions.cataloguing import create_item, edit_item
#from src.functions.marcxml_to_json import xml_to_json
from src.db.init_db import session
from src.db.models import Item, Exemplar, User
from fastapi import HTTPException, Response, Depends, status
from fastapi.encoders import jsonable_encoder
from copy import deepcopy
import json
from datetime import date


router = APIRouter()

#Get item title 
@router.get('/cataloguing/item/{item_id}', tags=["Cataloguing"])
async def get_item(item_id: int):
    item = session.query(Item).filter_by(id = item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return {'title': item.title}



#Get metadata in json marc
@router.get('/cataloguing/item/{item_id}/json', tags=["Cataloguing"])
async def get_item_json(item_id: int):
    item = session.query(Item).filter_by(id = item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
  
    return jsonable_encoder(item.marc)

#Exemplar
@router.get('/cataloguing/item/{item_id}/exemplares', tags=["Cataloguing"])
async def get_exemplares(item_id: int):
    item = session.query(Item).filter_by(id = item_id).first()
    exs  = list()
    for ex in item.exemplares:
        d = ex.__dict__
        d.pop('_sa_instance_state')
        exs.append(d)
    return exs

@router.post('/cataloguing/item/{item_id}/exemplar', tags=["Cataloguing"])
async def create_exemplar(item_id: int, exemplar: Exe):

    item = session.query(Item).filter_by(id = item_id).first()
    exs = exemplar.exemplares
    for ex in exs:
        print(ex)
        e = Exemplar(
            number = ex.number,
            callnumber = ex.callnumber,
            volume = ex.volume,
            library = ex.library,
            shelf = ex.shelf,
            status = ex.status,
            collection = ex.collection
            )
        item.exemplares.append(e)
    session.add(item)
    session.commit()

    return {'msg': 'Exemplar created successefully'}

@router.get('/cataloguing/exemplar', tags=["Cataloguing"])
async def get_exemplar():

    ex = session.query(Exemplar).order_by(Exemplar.id.desc()).first()
    
    lastEx = str(ex).split("-")
    lastYear = lastEx[0]
    lastNumber = int(lastEx[1])
    currentYear = str(date.today().year)[2:]
    if lastYear == currentYear:
        number = str(lastNumber+1)
        fill = (4 - len(number))* '0'
        return {'exemplar': currentYear+"-"+fill+str(lastNumber+1)}
    else:
        return {'exemplar': currentYear+"-0001"}

#Create a item
@router.post('/cataloguing/create', tags=["Cataloguing"], status_code=201)
async def cataloguing(item_request: Marc_Bibliographic, 
usuario_logado: User = Depends(get_usuario_logado)):
    response = create_item(item_request)

    return response

    
@router.patch('/cataloguing/item/{item_id}/patch', tags=["Cataloguing"])
async def patch_item( item_id: int, tagMarc: TagMarc):
    tagMarc = tagMarc.json()
    tagMarc = json.loads(tagMarc)

    item = session.query(Item).filter_by(id = item_id).first()
    marc = deepcopy(item.marc)
    marc.get('datafield')[tagMarc.get('tag')] = tagMarc.get('subfield')

    item.marc = marc

    session.commit()

    return {'msg': 'Item updated successefully',
    'id': item.id}

@router.put('/cataloguing/update', tags=["Cataloguing"])
async def put_item( tagsMarc: TagsMarc):

    tagsMarc = tagsMarc.json()
    tagsMarc = json.loads(tagsMarc)
    item = session.query(Item).filter_by(id = tagsMarc['id']).first()
    item.marc = tagsMarc.get('marc')

    return {'msg': 'Item updated successefully',
    'id': item.id}
