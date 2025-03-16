from fastapi import FastAPI, Depends, BackgroundTasks
from app import models, database, auth, crud, schemas, tasks
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.post("/register/")
def register_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return auth.register_user(db, user)

@app.post("/login/")
def login_user(user: schemas.UserLogin, db: Session = Depends(database.get_db)):
    return auth.login_user(db, user)

@app.post("/tasks/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(auth.get_current_user)):
    return crud.create_task(db, task, current_user.id)

@app.get("/tasks/", response_model=list[schemas.Task])
def get_tasks(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(auth.get_current_user)):
    return crud.get_tasks(db, current_user.id)

@app.put("/tasks/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(auth.get_current_user)):
    return crud.update_task(db, task_id, task, current_user.id)

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(auth.get_current_user)):
    return crud.delete_task(db, task_id, current_user.id)

@app.post("/background-tasks/")
def send_reminder(background_tasks: BackgroundTasks, db: Session = Depends(database.get_db)):
    background_tasks.add_task(tasks.send_task_reminders, db)
    return {"message": "Background task started for sending reminders."}