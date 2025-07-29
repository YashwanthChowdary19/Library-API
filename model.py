from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class Genre(str, Enum):
    fiction = "Fiction"
    nonfiction = "Non-Fiction"
    sci_fi = "Sci-Fi"
    biography = "Biography"

class Book(BaseModel):
    title: str = Field(..., min_length=2)
    author: str
    year_published: Optional[int] = Field(None, gt=1500, lt=2026)
    genre: Genre

class BookOut(Book):
    id: int

