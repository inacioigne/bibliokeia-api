from fastapi import APIRouter, HTTPException
import xml.etree.ElementTree as et
from src.db.init_db import session
from src.db.models import Item

router = APIRouter()


@router.get('/check/autorities/{item_id}', tags=["Check-up"])
async def check_autorities(item_id: int):
    item = session.query(Item).filter_by(id = item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    if len(item.authorship) == 0:
        root = et.fromstring(item.marc_record)
        author = root.find(".//*[@tag='100']/*/[@code='a']").text
        return {'msg' : 'Author: '+author+'Não está associado a este item'}