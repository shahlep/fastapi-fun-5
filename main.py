from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return f"Hello World!"


@app.get("/user/admin")
def admin():
    return f"welcome to admin page"


# route with dynamic path params with type
@app.get("/user/{username}")
def user(username: str):
    return f"this page is for user {username}"


# route with query params with deafult value and type
@app.get("/product")
def product(id: int = 1, price: float = 10.0):
    return f"product with an id: {id} and price: {price}"


# route with dynamic path params and query
@app.get("/profile/{userid}/comments")
def profile(userid: int, commentid: int):
    return f"profile page with userid {userid} and corresponding comment {commentid}"
