
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("📚 Library Manager")

# --- Button Selection ---
action = st.radio("Choose an action:", ["Add Book", "Show All", "Search Books", "Sort Books", "Update Book", "Delete Book"], key="action_selector", horizontal=True)


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

# -------------------- SEARCH BOOKS --------------------
elif action == "Search Books":
    st.subheader("🔍 Search Books")
    
    # Search options
    search_option = st.radio("Search by:", ["Search with Sorting", "Simple Search"], horizontal=True)
    
    if search_option == "Search with Sorting":
        st.write("**Search with additional sorting options:**")
        search_title = st.text_input("Search by title (optional)")
        sort_order = st.selectbox("Sort by year:", ["None", "asc", "desc"])
        
        if st.button("Search"):
            params = {}
            if search_title:
                params["search_title"] = search_title
            if sort_order != "None":
                params["sort_by_year"] = sort_order
            
            res = requests.get(f"{API_URL}/books", params=params)
            if res.status_code == 200:
                books = res.json()
                if books:
                    st.success(f"Found {len(books)} book(s)")
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
                    st.info("No books found matching your search criteria.")
            else:
                st.error("❌ Failed to search books.")
    
    else:  # Simple Search
        st.write("**Simple search by title:**")
        search_title = st.text_input("Enter title to search")
        
        if st.button("Search"):
            if search_title:
                res = requests.get(f"{API_URL}/books/search/{search_title}")
                if res.status_code == 200:
                    books = res.json()
                    if books:
                        st.success(f"Found {len(books)} book(s) with similar title")
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
                        st.info("No books found with similar title.")
                else:
                    st.error("❌ Failed to search books.")
            else:
                st.warning("Please enter a title to search.")

# -------------------- SORT BOOKS --------------------
elif action == "Sort Books":
    st.subheader("📊 Sort Books by Year")
    
    sort_order = st.selectbox("Sort order:", ["asc", "desc"])
    
    if st.button("Sort Books"):
        res = requests.get(f"{API_URL}/books/sort/year/{sort_order}")
        if res.status_code == 200:
            books = res.json()
            if books:
                order_text = "ascending" if sort_order == "asc" else "descending"
                st.success(f"Books sorted by year in {order_text} order:")
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
            st.error("❌ Failed to sort books.")

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
