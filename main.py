from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return f"Hello World!"


@app.get('/user/admin')
def admin():
    return f'welcome to admin page'


@app.get('/user/{username}')
def user(username: str):
    return f'this page is for user {username}'
