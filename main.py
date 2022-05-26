from fastapi import FastAPI
from pydantic import BaseModel


class Profile(BaseModel):
    name: str
    email: str


app = FastAPI()


@app.get("/")
def index():
    return f"Hello World!"


@app.get("/user/admin")
def admin():
    return f"welcome to admin page"


@app.post('/adduser')
def add_user(profile: Profile):
    return {"data":profile}
