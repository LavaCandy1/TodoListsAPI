from fastapi import FastAPI , HTTPException , Depends, Request, Form, status
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional, Annotated
from sqlalchemy.orm import Session
from database import engine, LocalSession
from starlette.responses import RedirectResponse
import models

todoApp = FastAPI()

templates = Jinja2Templates(directory = "templates")

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

class TodoBase(BaseModel):
    todo_text : str
    completed : Optional[bool]=False


@todoApp.get("/todoHome")
async def put_name(req : Request,db:db_dependency):
    result = db.query(models.Todo).all()
    return templates.TemplateResponse("todoHome.html", {"request": req , "name" : "World!", "todoList" : result})


@todoApp.post("/add-todoHTML")
async def add_todo(db : db_dependency, todo_textHTML : str=Form(...)):
    todo = TodoBase(todo_text=todo_textHTML)
    db_todo = models.Todo(todo_text = todo.todo_text)
    db.add(db_todo)
    db.commit()
    return RedirectResponse(url="/todoHome",status_code=status.HTTP_303_SEE_OTHER)

@todoApp.delete("/delete-todo/{todo_id}")
async def del_todo(todo_id : int, db : db_dependency ):
    to_delete = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not to_delete:
        raise HTTPException(status_code=404, detail=f"Todo id {todo_id} not found")
    db.delete(to_delete)
    db.commit()
    db.refresh(to_delete)


@todoApp.get("/delete-todo/{todo_id}")
async def del_todo(todo_id : int, db : db_dependency ):
    to_delete = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not to_delete:
        raise HTTPException(status_code=404, detail=f"Todo id {todo_id} not found")
    db.delete(to_delete)
    db.commit()
    return RedirectResponse(url="/todoHome",status_code=status.HTTP_303_SEE_OTHER)


@todoApp.get("/toggle-completion/{todo_id}")
async def update_todo(todo_id : int, db : db_dependency):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()

    if db_todo.completed:
        db_todo.completed = False
    else:
        db_todo.completed = True

    db.commit()
    db.refresh(db_todo)
    return RedirectResponse(url="/todoHome",status_code=status.HTTP_303_SEE_OTHER)



# @todoApp.post("/add-todo")
# async def add_todo(todo : TodoBase, db : db_dependency):
#     db_todo = models.Todo(todo_text = todo.todo_text)
#     db.add(db_todo)
#     db.commit()


# @todoApp.get("/get-todo/{todo_id}")
# async def get_todo(todo_id : int, db:db_dependency):
#     result = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
#     if not result:
#         raise HTTPException(status_code=404, detail=f"Todo with id {todo_id} not found!")
#     return result
