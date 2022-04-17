from fastapi import APIRouter, Depends, HTTPException
from src.schemas.request.cataloguing.exemplar import Exemplares
from src.db.init_db import session
from src.db.models import Item, User, Exemplar
from src.auth.login import get_usuario_logado

router = APIRouter()

@router.get('/{item_id}', response_model= Exemplares)
async def get_exemplares(item_id: int):
    item = session.query(Item).filter_by(id = item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    exs = []
    for e in item.exemplares:
        exs.append({
            "number" : e.number,
            "callnumber" : e.callnumber,
            "edition" : e.edition,
            "year" : e.year,
            "volume" : e.volume,
            "library" : e.library,
            "shelf" : e.shelf,
            "status" : e.status,
            "collection" : e.collection,
            "created_at": e.created_at
        })

    return Exemplares(exemplares=exs)


@router.post('/{item_id}')
async def create_exemplar(
    item_id: int, 
    request: Exemplares,
    auth: User = Depends(get_usuario_logado)):

    item = session.query(Item).filter_by(id = item_id).first()
    exs = request.exemplares
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

    return item.exemplares