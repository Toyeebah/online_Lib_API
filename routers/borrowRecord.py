from fastapi import APIRouter,HTTPException
from schemas.borrowRecord import BorrowRecord,borrowRecords,BorrowCreate
from CRUD.borrowOperations import BorrowCRUD
from schemas.book import books


borrowRecord_router = APIRouter()



@borrowRecord_router.post("/borrow")
def borrow_book(borrow_data:BorrowCreate):
    return BorrowCRUD.borrow_book(borrow_data)



@borrowRecord_router.post("/return")
def return_book(user_id: int, book_id: int):
   return BorrowCRUD.borrow_book(user_id, book_id)


@borrowRecord_router.get("/user/{user_id}")
def get_user_borrow_records(user_id: int):
   return BorrowCRUD.get_user_borrow_records(user_id)

@borrowRecord_router.get("/")
def get_all_borrow_records():
   return BorrowCRUD.get_all_borrow_records()


