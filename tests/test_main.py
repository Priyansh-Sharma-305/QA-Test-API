from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_user():
    new_user = {
        "id": 3,
        "name": "Charlie",
        "email": "charlie@example.com"
    }
    response = client.post("/users", json=new_user)
    assert response.status_code == 200
    assert response.json()["name"] == "Charlie"

def test_create_user_invalid_payload():
    bad_user = {"name": "NoID"}
    response = client.post("/users", json=bad_user)
    assert response.status_code == 422
