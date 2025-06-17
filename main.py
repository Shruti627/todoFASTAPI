from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles

tasks = []

class LoginBody(BaseModel):
    email: str
    password: str

class Task(BaseModel):
    title: str
    description: str

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def index():
    return FileResponse("static/index.html")

@app.get("/hello", response_class=HTMLResponse)
def read_root():
    return "<h1>Hello</h1>"

@app.post("/login")
def login(loginBody: LoginBody):
    print(loginBody.email)
    return {
        "msg": "Login successfully"
    }

@app.get("/tasks", response_model=list[Task])
def get_tasks():
    return tasks

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    tasks.append(task)
    return task
