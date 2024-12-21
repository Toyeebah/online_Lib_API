from fastapi import FastAPI
from routers.user import user_router
from routers.book import book_router
from routers.borrowRecord import borrowRecord_router


app=FastAPI()

app.include_router(book_router, prefix="/books", tags=["Books"])
app.include_router(borrowRecord_router, prefix="/borrowRecords", tags=["BorrowRecords"])
app.include_router(user_router, prefix="/users", tags=["Users"])



