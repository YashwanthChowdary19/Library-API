from fastapi import FastAPI, HTTPException
from typing import List
from model import Book, BookOut, Genre

app = FastAPI()

# In-memory "database"
books_db: List[BookOut] = []
book_id_counter = 1

@app.get("/", tags=["Health Check"])
def root():
    return {"message": "Library API is up"}

@app.post("/books", response_model=BookOut, tags=["Books"])
def add_book(book: Book):
    global book_id_counter
    book_out = BookOut(id=book_id_counter, **book.dict())
    books_db.append(book_out)
    book_id_counter += 1
    return book_out

@app.get("/books", response_model=List[BookOut], tags=["Books"])
def get_books():
    return books_db

@app.get("/books/{book_id}", response_model=BookOut, tags=["Books"])
def get_book(book_id: int):
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.put("/books/{book_id}", response_model=BookOut, tags=["Books"])
def update_book(book_id: int, updated_book: Book):
    for index, book in enumerate(books_db):
        if book.id == book_id:
            new_book = BookOut(id=book_id, **updated_book.dict())
            books_db[index] = new_book
            return new_book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}", tags=["Books"])
def delete_book(book_id: int):
    for index, book in enumerate(books_db):
        if book.id == book_id:
            books_db.pop(index)
            return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")
