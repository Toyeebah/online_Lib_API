from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app, User

client = TestClient(app)

mock_users = [
    User(**{"id": 1, "name": "John", "email": "John@yahoo.com", "description": "Johnny"}),
    User(**{"id": 2, "name": "Janet", "email": "Janet@yahoo.com", "description": "Jane"}),
    User(**{"id": 3, "name": "Joe", "email": "Joe@yahoo.com", "description": "Joey"}),
]


@patch("main.users", mock_users)
def test_add_user():
    user_data = {
        "name": "Test Name",
        "email": "Test@yahoo.com",
        "description": "a good person"
    }
    expected_user_response = user_data = {
        "id": len(mock_users) + 1,
        "name": "Test Nmae",
        "email": "Test@yahoo.com",
        "description": "a good person"
    }
    response = client.post("/users", json=user_data)
    assert response.status_code == 201
    assert response.json() == expected_user_response


@patch("main.users", mock_users)
def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert len(mock_users) == 3


@patch("main.users", mock_users)
def test_get_user_by_id():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["name"] == "John"
    assert response.json()["email"] == "john@yahoo.com"


@patch("main.users", mock_users)
def test_update_user():
    user_data = {
        "name": "Updated John",
        "email": "Updated John@yahoo.com",
        "description": "Updated good user"
    }
    response = client.put("/users/1", json=user_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Updated name"
    assert response.json()["email"] == "Updated email"
    assert response.json()["description"] == "Updated good user"


@patch("main.users", mock_users)
def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code == 200
    assert response.json()["message"] == "User deleted successfully"
    response = client.get("/users/1")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found."


def test_delete_user_not_found():
    response = client.delete("/users/2")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found."


def test_get_user_not_found():
    response = client.get("/users/2")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found."
