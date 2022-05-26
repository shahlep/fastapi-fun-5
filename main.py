from fastapi import FastAPI, Form
from pydantic import BaseModel, Field
from uuid import UUID
from datetime import date, datetime, timedelta, time
import schemas as _schemas
import models as _models
import database as _database


class User(BaseModel):
    name: str = Field(example="test")
    email: str

    class Config:
        schema_extra = {"example": {"name": "test", "email": "test@example.com"}}


class Product(BaseModel):
    name: str
    price: int = Field(title="Price of the product", gt=2)


class Event(BaseModel):
    event_id: UUID
    start_date: date
    start_time: datetime
    end_time: datetime
    repeat_time: date
    execute_after: timedelta


_database.get_db()
_models.Base.metadata.create_all(bind=_database.engine)
app = FastAPI()


@app.get("/")
def index():
    return f"Hello World!"


@app.get("/user/admin")
def admin():
    return f"welcome to admin page"


@app.post("/purchase")
def purchase(user: User, product: Product):
    return {"user": user, "product": product}


@app.post("/event")
def event(event: Event):
    return event


@app.post("/login")
def login(username: str, password: str):
    return {"username": username, "password": password}


@app.post("/product")
def add(request: _schemas.Product):
    return request
