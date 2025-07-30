
# 📚 Library Manager App

A full-stack book management app built using **FastAPI** for the backend and **Streamlit** for the frontend — all in a single file.

---

## 🚀 Features

- 📖 Add, View, Update, and Delete books
- 🔍 Search books by similar title (using query parameters or path parameters)
- 📊 Sort books by year published (ascending/descending)
- 🌐 RESTful API with FastAPI
- 💻 Interactive UI with Streamlit
- ⚡ Fast and lightweight

---

## 🧰 Tech Stack

- **FastAPI** – High-performance web framework
- **Streamlit** – Rapid frontend development
- **Pydantic** – Data validation
- **Uvicorn** – ASGI server for FastAPI

---

## 🔧 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/library-manager.git
cd library-manager
```

### 2️⃣ Create and Activate Virtual Environment (Recommended)

```bash
python -m venv .env
# For Windows:
.env\Scripts\activate
# For macOS/Linux:
source .env/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

<details>
<summary>If you don't have <code>requirements.txt</code>, use this:</summary>

```txt
fastapi
uvicorn
pydantic
streamlit
requests
```

✅ Make sure both work together (FastAPI runs in background and Streamlit calls it using `requests`).

---

## 🧪 Example Usage

- **Add Book** – Enter book details like `title`, `author`, `year_published`, and `genre`
- **View All** – See the entire list of books
- **Search Books** – Search by title with optional sorting
- **Sort Books** – Sort books by year published
- **Update Book** – Provide ID and new data to update
- **Delete Book** – Enter the ID of the book to remove it

---

## 📬 API Endpoints (FastAPI)

| Method | Endpoint                    | Description                    |
|--------|----------------------------|--------------------------------|
| GET    | `/`                        | Health check                   |
| GET    | `/books`                   | Get all books                  |
| GET    | `/books?search_title=...`  | Search books by title          |
| GET    | `/books?sort_by_year=asc`  | Sort books by year (ascending) |
| GET    | `/books?sort_by_year=desc` | Sort books by year (descending)|
| GET    | `/books/search/{title}`    | Search books by title (path)   |
| GET    | `/books/sort/year/{order}` | Sort books by year (path)      |
| POST   | `/books`                   | Add a new book                 |
| PUT    | `/books/{id}`              | Update a book                  |
| DELETE | `/books/{id}`              | Delete a book                  |

---

## 🔍 Search Features

### Query Parameter Search
- Use `GET /books?search_title=harry` to find books with "harry" in the title
- Combine with sorting: `GET /books?search_title=harry&sort_by_year=desc`

### Path Parameter Search
- Use `GET /books/search/harry` to find books with "harry" in the title
- Use `GET /books/sort/year/asc` to sort all books by year (ascending)
- Use `GET /books/sort/year/desc` to sort all books by year (descending)

---

## 📊 Sorting Options

- **Ascending (asc)**: Books sorted from oldest to newest
- **Descending (desc)**: Books sorted from newest to oldest
- Works with search functionality for combined filtering and sorting

---
