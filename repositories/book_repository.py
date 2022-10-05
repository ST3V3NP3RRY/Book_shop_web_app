from db.run_sql import run_sql

from models.author import Author
from models.book import Book

# Save
def save(book):
    sql = """
    INSERT INTO books (title, genre, isbn, author_id)
    VALUES (%s, %s, %s, %s) RETURNING *
    """
    # breakpoint()
    values = [book.title, book.genre, book.isbn, book.author.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    book.id = id
    return book


# Select all


# Select id


# Delete all


# Delete (id)
def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)


# Update
