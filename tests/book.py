from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app, Book

client = TestClient(app)

mock_books = [
    Book(**{"id": 1, "title": "book 1", "author": "author 1", "description": "description 1"}),
    Book(**{"id": 2, "title": "book 2", "author": "author 2", "description": "description 2"}),
    Book(**{"id": 3, "title": "book 3", "author": "author 3", "description": "description 3"}),
]


@patch("main.books", mock_books)
def test_add_book():
    book_data = {
        "title": "Test Book",
        "author": "Test Author",
        "description": "a good book"
    }
    expected_book_response = book_data = {
        "id": len(mock_books) + 1,
        "title": "Test Book",
        "author": "Test Author",
        "description": "a good book"
    }
    response = client.post("/books", json=book_data)
    assert response.status_code == 201
    assert response.json() == expected_book_response


@patch("main.books", mock_books)
def test_get_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert len(mock_books) == 3


@patch("main.books", mock_books)
def test_get_book_by_id():
    response = client.get("/books/1")
    assert response.status_code == 200
    assert response.json()["title"] == "book 1"
    assert response.json()["author"] == "author 1"


@patch("main.books", mock_books)
def test_update_book():
    book_data = {
        "title": "Updated Test Book",
        "author": "Updated Test Author",
        "description": "an updated good book"
    }
    response = client.put("/books/1", json=book_data)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Test Book"
    assert response.json()["author"] == "Updated Test Author"
    assert response.json()["description"] == "an updated good book"


@patch("main.books", mock_books)
def test_delete_book():
    response = client.delete("/books/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Book deleted successfully"
    response = client.get("/books/1")
    assert response.status_code == 404
    assert response.json()["detail"] == "Book not found."


def test_delete_book_not_found():
    response = client.delete("/books/2")
    assert response.status_code == 404
    assert response.json()["detail"] == "Book not found."


def test_get_book_not_found():
    response = client.get("/books/2")
    assert response.status_code == 404
    assert response.json()["detail"] == "Book not found."
