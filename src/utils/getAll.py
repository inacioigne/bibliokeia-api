from functools import wraps
from src.db.init_db import session

def get_all(Model):
    def inner(func):
        @wraps(func)
        async def wrapper(**kwargs):
            return await session.query(Model).all()
        return wrapper
    return inner



