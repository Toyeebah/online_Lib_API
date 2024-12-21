from fastapi import APIRouter
from CRUD.book import BookCrud
from schemas.book import BookCreate, BookResponse

book_router = APIRouter()

@book_router.post("/", response_model=BookResponse)
def create_book(book_data: BookCreate):
    return BookCrud.create_book(book_data)

@book_router.get("/", response_model=BookResponse)
def get_book():
    return BookCrud.get_book()


@book_router.get("/{book_id}", response_model=BookResponse)
def get_book_by_id(book_id: int):
    return BookCrud.get_book_by_id(book_id)



@book_router.put("/{book_id}", response_model=BookResponse)
def update_book(book_id: int, new_data: BookCreate):
    return BookCrud.update_book(book_id, new_data)



@book_router.delete("/{book_id}")
def delete_book(book_id: int):
    return BookCrud.delete_book(book_id)


@book_router.patch("/{book_id}/mark-unavailable")
def mark_book_unavailable(book_id: int):
    return BookCrud.mark_book_unavailable(book_id)
