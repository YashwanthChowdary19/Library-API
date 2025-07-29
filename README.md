
# 📚 Library Manager App

A full-stack book management app built using **FastAPI** for the backend and **Streamlit** for the frontend — all in a single file.

---

## 🚀 Features

- 📖 Add, View, Update, and Delete books
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

- **Add Book** – Enter book details like `id`, `title`, `author`, and `pages`
- **View All** – See the entire list of books
- **Update Book** – Provide ID and new data to update
- **Delete Book** – Enter the ID of the book to remove it

---

## 📬 API Endpoints (FastAPI)

| Method | Endpoint         | Description         |
|--------|------------------|---------------------|
| GET    | `/`              | Health check        |
| GET    | `/books`         | Get all books       |
| POST   | `/books`         | Add a new book      |
| PUT    | `/books/{id}`    | Update a book       |
| DELETE | `/books/{id}`    | Delete a book       |

---
