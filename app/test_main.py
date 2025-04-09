import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_create_user():
    response = client.post(
        "/users/", 
        json={"email": "testuser@example.com", "username": "testuser", "full_name": "Test User", "password": "password123"}
    )
    assert response.status_code == 201
    assert response.json() == {
        "email": "testuser@example.com", 
        "username": "testuser", 
        "full_name": "Test User", 
        "password": "password123"
    }

def test_get_users():
    # 유저 생성 후, 조회 테스트
    client.post(
        "/users/", 
        json={"email": "testuser@example.com", "username": "testuser", "full_name": "Test User", "password": "password123"}
    )
    response = client.get("/users")
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()[0]["username"] == "testuser"

