from pydantic import BaseModel


class CreateTodoRequest(BaseModel):
    id: int
    task: str
    status: bool
