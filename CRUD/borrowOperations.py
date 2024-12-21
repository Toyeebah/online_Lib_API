
from fastapi import HTTPException
from schemas.book import BookCreate, Book, BookPatch, books
from schemas.user import UserCreate, User, UserPatch, users
from schemas.borrowRecord import BorrowRecord, borrowRecords
from datetime import datetime



class BorrowCRUD():

    @staticmethod
    def borrow_book(user_id: int, book_id: int):
        
        user = users.get(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        if not user.get("is_active"):
            raise HTTPException(status_code=403, detail="User is inactive")

        
        book = books.get(book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        if not book.get("is_available"):
            raise HTTPException(status_code=400, detail="Book is not available")

        
        for record in borrowRecords.values():
            if record["user_id"] == user_id and record["book_id"] == book_id and record["return_date"] is None:
                raise HTTPException(status_code=400, detail="User has already borrowed this book")

    
        borrow_id = len(borrowRecords) + 1
        borrowRecords[borrow_id] = {
            "id": borrow_id,
            "user_id": user_id,
            "book_id": book_id,
            "borrow_date": datetime.now().strftime("%Y-%m-%d"),
            "return_date": None,
        }

       
        book["is_available"] = False

        return {"message": "Book successfully borrowed"}

    @staticmethod
    def return_book(user_id: int, book_id: int):
        
        for record in borrowRecords.values():
            if record["user_id"] == user_id and record["book_id"] == book_id and record["return_date"] is None:
                
                record["return_date"] = datetime.now().strftime("%Y-%m-%d")
                books[book_id]["is_available"] = True
                return {"message": "Book successfully returned"}

        
        raise HTTPException(status_code=404, detail="No active borrowing record found for this user and book")




    @staticmethod
    def get_user_borrow_records(user_id: int):
        
        records = [
            record
            for record in borrowRecords.values()
            if record["user_id"] == user_id
        ]

        if not records:
            raise HTTPException(status_code=404, detail="No borrowing records found for this user")

        return {"records": records}



    @staticmethod
    def get_all_borrow_records():
    
        if not borrowRecords:
            raise HTTPException(status_code=404, detail="No borrowing records found")

        return {"records": list(borrowRecords.values())}


 


borrowCRUD=BorrowCRUD()




