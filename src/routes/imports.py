from fastapi import APIRouter
from src.schemas.requests_body import Request_Item, Request_Authority, Request_Subjects
from src.functions.import_marc import import_marc_item, import_marc_authority, import_marc_subjects

router = APIRouter()

@router.post('/import/items', tags=["Imports"], status_code=201)
async def import_items(request_item: Request_Item):
    response = import_marc_item(request_item)

    return response

@router.post('/import/authority', tags=["Imports"])
async def import_authority(request_authority: Request_Authority):
    response = import_marc_authority(request_authority)

    return response

@router.post('/import/subjects', tags=["Imports"], status_code=201)
async def import_subjects(request_subjects: Request_Subjects):
    response = import_marc_subjects(request_subjects)

    return response