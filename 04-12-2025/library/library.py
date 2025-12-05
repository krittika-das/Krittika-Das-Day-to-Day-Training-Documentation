import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="s112hu7&*",
    database="library_db"
)
cursor = conn.cursor(dictionary=True)


def search_books(keyword):
    query = """
    SELECT * FROM books
    WHERE title LIKE %s OR author LIKE %s;
    """
    cursor.execute(query, (f"%{keyword}%", f"%{keyword}%"))
    results = cursor.fetchall()
    for book in results:
        print(f"{book['book_id']}: {book['title']} by {book['author']} ({book['published_year']}) - Available: {book['available']}")


def borrow_book(member_id, book_id):
    # Check availability
    cursor.execute("SELECT available FROM books WHERE book_id=%s", (book_id,))
    book = cursor.fetchone()
    if book and book['available']:
        cursor.execute("INSERT INTO borrow_records (member_id, book_id) VALUES (%s, %s)", (member_id, book_id))
        cursor.execute("UPDATE books SET available=FALSE WHERE book_id=%s", (book_id,))
        conn.commit()
        print("Book borrowed successfully!")
    else:
        print("Book is not available.")


def return_book(record_id):
    cursor.execute("SELECT book_id FROM borrow_records WHERE record_id=%s AND return_date IS NULL", (record_id,))
    record = cursor.fetchone()
    if record:
        book_id = record['book_id']
        cursor.execute("UPDATE borrow_records SET return_date=CURRENT_DATE WHERE record_id=%s", (record_id,))
        cursor.execute("UPDATE books SET available=TRUE WHERE book_id=%s", (book_id,))
        conn.commit()
        print("Book returned successfully!")
    else:
        print("Invalid record or book already returned.")

if __name__ == "__main__":
    print("Searching for 'George':")
    search_books("George")

    print("Borrowing book_id=3 by member_id=1:")
    borrow_book(1, 3)

    print("Returning record_id=1:")
    return_book(1)

cursor.close()
conn.close()