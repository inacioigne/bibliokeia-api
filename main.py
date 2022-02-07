import re
from fastapi import FastAPI, Response
from src.db.init_db import initializeDatabase
#from src.db.models import Item
from src.schemas.requests_body import Test_Item
from src.routes import cataloguing, imports, items, checkup
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

initializeDatabase()

app = FastAPI(
    title="BiblioKeia",
    description="Backend API for BiblioKeia",
    contact={
        "name": "Inácio Oliveira",
        "url": "https://github.com/inacioigne",
        "email": "dp@x-force.example.com",
    }
)

origins = [
    "http://localhost:3000",
    'http://127.0.0.1:3000'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET', 'PUT', 'POST'],
    allow_headers=["*"],
)

app.include_router(cataloguing.router)
app.include_router(imports.router)
app.include_router(items.router)
app.include_router(checkup.router)

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

@app.get("/test_items/{item_id}", response_model=Test_Item)
async def read_item(item_id: str):
    data = """<?xml version="1.0"?>
    <shampoo>
    <Header>
        Apply shampoo here.
    </Header>
    <Body>
        You'll have to use soap here.
    </Body>
    </shampoo>
    """
    return Response(content=data, media_type="application/xml")

@app.put("/test_items/{item_id}", response_model=Test_Item)
async def update_item(item_id: str, item: Test_Item):
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded
    