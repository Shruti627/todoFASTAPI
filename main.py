from fastapi import FastAPI
from pydantic import BaseModel

class LoginBody(BaseModel):
    email: str
    password: str

app = FastAPI()

@app.get("/hello")
def read_root():
    return {"msg": "Hello World"}

@app.post("/login")
def login(loginBody: LoginBody):
    print(loginBody.email)
    return {
        "msg": "Login successfully"
    }
