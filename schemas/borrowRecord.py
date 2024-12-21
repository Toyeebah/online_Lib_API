from pydantic import BaseModel,UUID4,EmailStr
from datetime import date,time
from typing import Optional





class BorrowRecord(BaseModel):
    id: UUID4
    user_id: str
    book_id: str
    borrow_date: date
    return_date:date

class BorrowCreate(BaseModel):
    user_id:int
    book_id:int


class BorrowResponse(BorrowCreate):
    id:UUID4
    borrow_date: str
    return_date:Optional[str]





borrowRecords: dict[int:BorrowRecord]= {}