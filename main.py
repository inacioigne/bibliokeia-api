import re
from fastapi import FastAPI, Response
#from routes import old_cataloguing
from src.db.init_db import initializeDatabase
#from src.db.models import Item
#from src.schemas.requests_body import Test_Item
from src.routes import imports, items, checkup, users
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from src.routes.cataloging import item, exemplar

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
    'http://127.0.0.1:3000',
    "http://172.21.215.224:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET', 'PUT', 'POST', 'PATCH', 'DELETE'],
    allow_headers=["*"],
)

app.include_router(imports.router)
app.include_router(items.router)
app.include_router(checkup.router)
app.include_router(users.router, prefix='/usuarios', tags=['Usuarios'])
app.include_router(item.router, prefix='/cataloging/item', tags=['Cataloging Item'] )
app.include_router(exemplar.router, prefix='/cataloging/exemplar', tags=["Cataloguing Exemplar"] )
