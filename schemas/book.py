from pydantic import BaseModel,UUID4,EmailStr
from typing import Optional

class BookBase(BaseModel):
    title: str
    author: str
    is_available : bool=True


class Book(BookBase):
    id:UUID4

class BookCreate(BookBase):
    pass

class BookPatch(BookBase):
    title: Optional[str]= None
    author: Optional[str]=None
    is_available :Optional [bool]=True 


class BookResponse(BookCreate):
    id:int

    
books: dict[int: Book]= {}
