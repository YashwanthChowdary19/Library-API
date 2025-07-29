
import streamlit as st
import requests

API_URL = "add your api url"

st.title("📚 Library Manager")

# --- Button Selection ---
action = st.radio("Choose an action:", ["Add Book", "Show All", "Update Book", "Delete Book"], key="action_selector")


# -------------------- ADD BOOK --------------------
if action == "Add Book":
    st.subheader("➕ Add a New Book")
    with st.form("add_book_form"):
        title = st.text_input("Title")
        author = st.text_input("Author")
        year = st.number_input("Year Published", min_value=1501, max_value=2025, step=1)
        genre = st.selectbox("Genre", ["Fiction", "Non-Fiction", "Sci-Fi", "Biography"])
        submitted = st.form_submit_button("Add Book")

        if submitted:
            payload = {
                "title": title,
                "author": author,
                "year_published": int(year),
                "genre": genre
            }
            res = requests.post(f"{API_URL}/books", json=payload)
            if res.status_code == 200:
                st.success("✅ Book added successfully!")
            else:
                st.error(f"❌ Error: {res.json()['detail']}")

# -------------------- SHOW ALL BOOKS --------------------
elif action == "Show All":
    st.subheader("📖 All Books")
    res = requests.get(f"{API_URL}/books")
    if res.status_code == 200:
        books = res.json()
        if books:
            for book in books:
                st.markdown(f"""
                    🔖 **ID**: {book['id']}  
                    📘 **Title**: {book['title']}  
                    ✍️ **Author**: {book['author']}  
                    🗓️ **Year**: {book['year_published']}  
                    🏷️ **Genre**: `{book['genre']}`  
                    ---
                """)
        else:
            st.info("No books found.")
    else:
        st.error("❌ Failed to fetch books.")

# -------------------- UPDATE BOOK --------------------
elif action == "Update Book":
    st.subheader("🔄 Update a Book")
    with st.form("update_book_form"):
        book_id = st.number_input("Enter Book ID", min_value=1, step=1)
        new_title = st.text_input("New Title")
        new_author = st.text_input("New Author")
        new_year = st.number_input("New Year Published", min_value=1501, max_value=2025, step=1)
        new_genre = st.selectbox("New Genre", ["Fiction", "Non-Fiction", "Sci-Fi", "Biography"])
        submit_update = st.form_submit_button("Update Book")

        if submit_update:
            payload = {
                "title": new_title,
                "author": new_author,
                "year_published": int(new_year),
                "genre": new_genre
            }
            res = requests.put(f"{API_URL}/books/{book_id}", json=payload)
            if res.status_code == 200:
                st.success("✅ Book updated successfully!")
            else:
                st.error(f"❌ Error: {res.json()['detail']}")

# -------------------- DELETE BOOK --------------------
elif action == "Delete Book":
    st.subheader("🗑️ Delete a Book")
    book_id = st.number_input("Enter Book ID to Delete", min_value=1, step=1)
    if st.button("Delete"):
        res = requests.delete(f"{API_URL}/books/{book_id}")
        if res.status_code == 200:
            st.success("✅ Book deleted successfully!")
        else:
            st.error(f"❌ Error: {res.json()['detail']}")
