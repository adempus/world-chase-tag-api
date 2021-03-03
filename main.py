from typing import Optional
from fastapi import FastAPI
from wct_api.database import db


app = FastAPI()


def get_connection():
    return db.get_connection()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}



