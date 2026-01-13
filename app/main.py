from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

fake_users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/users")
def get_users():
    return fake_users

@app.post("/users")
def create_user(user: User):
    fake_users.append(user.dict())
    return user
