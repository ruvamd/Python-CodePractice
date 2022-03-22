from platform import python_branch
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

pc={
    1:{
        'cpu':'intel',
        'ram':'asus',
        'ssd':'samsung'
            }
    }

@app.get('/get-item/{item_id}/{name}')
def get_item(item_id:int,name:str):
    return pc[item_id]

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}

# @app.get('/about')
# def about():
#     return{'data':'about'}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}