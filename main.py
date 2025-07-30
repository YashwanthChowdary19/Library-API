from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
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
def get_books(
    search_title: Optional[str] = Query(None, description="Search books by similar title"),
    sort_by_year: Optional[str] = Query(None, description="Sort by year: 'asc' or 'desc'")
):
    filtered_books = books_db.copy()
    
    # Search by similar title
    if search_title:
        search_title_lower = search_title.lower()
        filtered_books = [
            book for book in filtered_books 
            if search_title_lower in book.title.lower()
        ]
    
    # Sort by year published
    if sort_by_year:
        if sort_by_year.lower() == "asc":
            filtered_books.sort(key=lambda x: x.year_published or 0)
        elif sort_by_year.lower() == "desc":
            filtered_books.sort(key=lambda x: x.year_published or 0, reverse=True)
    
    return filtered_books

@app.get("/books/search/{title}", response_model=List[BookOut], tags=["Books"])
def search_books_by_title(title: str):
    """Search books by similar title using path parameter"""
    title_lower = title.lower()
    matching_books = [
        book for book in books_db 
        if title_lower in book.title.lower()
    ]
    return matching_books

@app.get("/books/sort/year/{order}", response_model=List[BookOut], tags=["Books"])
def sort_books_by_year(order: str):
    """Sort books by year published: 'asc' or 'desc'"""
    if order.lower() not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Order must be 'asc' or 'desc'")
    
    sorted_books = books_db.copy()
    if order.lower() == "asc":
        sorted_books.sort(key=lambda x: x.year_published or 0)
    else:
        sorted_books.sort(key=lambda x: x.year_published or 0, reverse=True)
    
    return sorted_books

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
