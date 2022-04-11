from fastapi import APIRouter, Depends
from src.auth.login import get_usuario_logado
from src.schemas.request.cataloguing.item import Marc_Bibliographic
from src.db.models import Item, User

router = APIRouter()

#Create a item
@router.post('/create', status_code=201)
async def create_item(
    request: Marc_Bibliographic, 
    auth: User = Depends(get_usuario_logado)
    ):
    item = Item()
    print('USUARIO: ', auth)


    return request

    # def create_item(item_request):
    # marcjson = item_request.json()
    # marcdict = json.loads(marcjson)
    
    # item = Item(
    #         title = marcdict.get('datafield').get('245').get('a').replace(':',''),
    #         marc = marcdict,
    #         )
    
    # session.add(item)
    # session.commit()
    
    # return {'msg': 'Item created successefully',
    # 'id': item.id}