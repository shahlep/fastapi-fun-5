from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return f"Hello World!"


@app.get("/property/{id}")
def property(id: int):
    return f"property page based on given {id}"
