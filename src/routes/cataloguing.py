from fastapi import APIRouter
from src.schemas.requests_body import Model_Item, Model_Item_Edit
from src.schemas.marc_schemas import Marc_Bibliographic
from src.functions.cataloguing import create_item, edit_item
from src.functions.marcxml_to_json import xml_to_json
from src.db.init_db import session
from src.db.models import Item
from fastapi import HTTPException, Response
from fastapi.encoders import jsonable_encoder


router = APIRouter()

#Get item title 
@router.get('/cataloguing/item/{item_id}', tags=["Cataloguing"])
async def get_item(item_id: int):
    item = session.query(Item).filter_by(id = item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return {'title': item.title}

#Return a marcxml item
@router.get('/cataloguing/item/{item_id}/marcxml', tags=["Cataloguing"])
async def get_item(item_id: int):
    item = session.query(Item).filter_by(id = item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return Response(content=item.marc_record, media_type="application/xml")

#Get metadata in json marc
@router.get('/cataloguing/item/{item_id}/json', tags=["Cataloguing"])
async def get_item_json(item_id: int):
    item = session.query(Item).filter_by(id = item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
  
    return jsonable_encoder(item.marc)

#Create a item
@router.post('/cataloguing/create', tags=["Cataloguing"], status_code=201)
async def cataloguing(item_request: Marc_Bibliographic):
    response = create_item(item_request)

    return response



@router.put('/cataloguing/edit/{item_id}', tags=["Cataloguing"])
async def cataloguing_edit(item_id: int, item_edit: Model_Item_Edit):
    response = edit_item(item_id, item_edit)

    return response
