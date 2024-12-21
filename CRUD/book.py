from fastapi import HTTPException
from schemas.book import BookCreate,books

class BookCrud:

    @staticmethod
    def create_book(book_data: BookCreate):
        book_id = len(books) + 1
        book = {"id": book_id, **book_data.dict()}
        books[book_id] = book
        return book

    @staticmethod
    def get_book_by_id(book_id: int):
        book = books.get(book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found.")
        return book

    @staticmethod
    def get_book():
        book = books.get()
        if not book:
            raise HTTPException(status_code=404, detail="Book not found.")
        return book



    @staticmethod
    def update_book(book_id: int, new_data: BookCreate):
        book = books.get(book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found.")
        books[book_id] = {"id": book_id, **new_data.dict()}
        return books[book_id]

    @staticmethod
    def delete_book(book_id: int):
        if book_id not in books:
            raise HTTPException(status_code=404, detail="Book not found.")
        del books[book_id]
        return {"detail": f"Book {book_id} deleted."}

    @staticmethod
    def mark_book_unavailable(book_id: int):
        book = books.get(book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found.")
        book["is_available"] = False
        return {"detail": f"Book {book_id} marked as unavailable."}


book_crud = BookCrud()