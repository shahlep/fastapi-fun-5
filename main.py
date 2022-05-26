from fastapi import FastAPI
from pydantic import BaseModel,Field


class User(BaseModel):
    name: str
    email: str


class Product(BaseModel):
    name: str
    price: int = Field(title="Price of the product",gt=2)


app = FastAPI()


@app.get("/")
def index():
    return f"Hello World!"


@app.get("/user/admin")
def admin():
    return f"welcome to admin page"


@app.post("/purchase")
def purchase(user:User, product:Product):
    return {'user': user,'product':product}
