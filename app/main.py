from fastapi import FastAPI
from pydantic import BaseModel
from threading import Lock

app = FastAPI(title="K8s Task API")

tasks = []
lock = Lock()


class TaskRequest(BaseModel):
    task: str


@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "k8s-task-api"}


@app.get("/tasks")
def get_tasks():
    with lock:
        return {"tasks": tasks}


@app.post("/tasks")
def create_task(request: TaskRequest):
    with lock:
        tasks.append(request.task)

    return {"message": "task added", "task": request.task}