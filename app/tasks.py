from sqlalchemy.orm import Session
from app import models

def send_task_reminders(db: Session):
    from datetime import datetime, timedelta
    tasks = db.query(models.Task).filter(models.Task.due_date <= datetime.utcnow() + timedelta(hours=1), models.Task.completed == False).all()
    for task in tasks:
        print(f"Reminder: Task '{task.title}' is due soon!")