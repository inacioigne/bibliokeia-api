from fastapi import APIRouter, Depends, HTTPException
from src.db.init_db import session
from src.auth.login import get_usuario_logado
from src.schemas.request.cataloguing.item import Marc_Bibliographic, Field_Marc
from src.db.models import Item, User
from copy import deepcopy
from datetime import datetime

router = APIRouter()

#Create a item
@router.post('/create', status_code=201)
async def create_item(
    request: Marc_Bibliographic, 
    auth: User = Depends(get_usuario_logado)):
    
    log =  {'creator': {'id': auth.id, 'name': auth.name }}
    #Get title
    if  '245' in request.datafields.keys():
        title = request.datafields.get("245").get('subfields').get('a')
    else: 
        raise HTTPException(status_code=404, detail="Title not found")
    
    item = Item(title = title, marc = request.dict(), logs = log)   

    session.add(item)
    session.commit()

    return {'item_id': item.id, 'marc': item.marc}

#Get item marc
@router.get('/{item_id}', response_model= Marc_Bibliographic)
async def get_item(item_id: int ):
    item = session.query(Item).filter_by(id = item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return Marc_Bibliographic(**item.marc)

#Update (Patch) item
@router.patch('/{item_id}', response_model= Marc_Bibliographic)
async def patch_item(
    item_id: int, 
    request: Field_Marc, 
    auth: User = Depends(get_usuario_logado)):

    item = session.query(Item).filter_by(id = item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    
    #Update Logs
    logs = deepcopy(item.logs)
    if 'updates' in logs.keys():
        logs.get('updates').append({
            'user': {'id': auth.id, 'name': auth.name },
            "date": datetime.now().strftime("%d/%m/%Y %H:%M")})
    else:
        logs['updates'] = [{
            'user': {'id': auth.id, 'name': auth.name },
            "date": datetime.now().strftime("%d/%m/%Y %H:%M")}]
    item.logs = logs

    marc = deepcopy(item.marc)
    marc.get('datafields').get(request.tag)['subfields'] = request.subfields
    #handle time
    t = datetime.now()
    time = t.strftime('%Y%m%d%H%M%S')+'.'+t.strftime('%f')[0]  
    marc.get('controlfields')['005'] = time

    item.marc = marc
    session.add(item)
    session.commit()

    return Marc_Bibliographic(**item.marc)






