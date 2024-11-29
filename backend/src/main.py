from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TodoItem(BaseModel):
    id: int
    task: str
    completed: bool

todo_list = [
    TodoItem(id=1, task="shopping", completed=False), 
    TodoItem(id=2, task="cleaning", completed=False), 
    TodoItem(id=3, task="cooking", completed=False), TodoItem(id=4, task="coding", completed=False)
]

@app.get("/todos")
def get_todos():
    return todo_list

