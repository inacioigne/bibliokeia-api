from fastapi import APIRouter, HTTPException
from src.db.init_db import session
from src.db.models import Item

router = APIRouter()


@router.get('/item/{item_id}', tags=["Items"])
async def get_item(item_id: int):
    item = session.query(Item).filter_by(id = item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return {'title' : item.title}