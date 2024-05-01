from fastapi import Body, FastAPI, HTTPException
from src.classes.enums.todos import TO_DOS
from src.classes.todo.models import CreateTodoRequest

app = FastAPI()


@app.get("/")
def health_check():
    return {"status": "ok"}


@app.get("/todos")
def get_todos(order: str = "asc"):
    if order == "desc":
        return list(TO_DOS.values())[::-1]
    return list(TO_DOS.values())


@app.get("/todos/{todo_id}", status_code=200)
def get_todo(todo_id: int):
    res = TO_DOS.get(todo_id)
    if res:
        return res
    raise HTTPException(status_code=404, detail="There is No ToDo")


@app.post("/todos", status_code=201)
def create_todo_handler(request: CreateTodoRequest):
    res = TO_DOS[request.id] = request
    if res:
        return res
    raise HTTPException(status_code=404, detail="There is No ToDo")


@app.patch("/todos/{todo_id}", status_code=200)
def update_todo_handler(todo_id: int, todo_status: bool = Body(..., embed=True)):
    todo = TO_DOS.get(todo_id)
    if todo:
        todo["status"] = todo_status
        return todo
    raise HTTPException(status_code=404, detail="There is No ToDo")


@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo_handler(todo_id: int):
    deleted_todo = TO_DOS.pop(todo_id, None)
    if deleted_todo:
        return
    raise HTTPException(status_code=404, detail="There is No ToDo")
