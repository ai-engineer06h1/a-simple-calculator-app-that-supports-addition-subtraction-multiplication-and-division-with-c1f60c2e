from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import os

app = FastAPI()

# Example data model
class Item(BaseModel):
    id: int
    name: str

items_db = []

@app.post("/api/items", response_model=Item)
def create_item(item: Item):
    items_db.append(item)
    return item

@app.get("/api/items", response_model=List[Item])
def read_items():
    return items_db

@app.get("/api/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")