from fastapi import FastAPI
from src.classes.enums.todos import TO_DOS

app = FastAPI()


@app.get("/")
def health_check():
    return {"status": "ok"}


@app.get("/todos")
def get_todos(order: str = "asc"):
    if order == "desc":
        return list(TO_DOS.values())[::-1]
    return list(TO_DOS.values())
