from db.run_sql import run_sql

from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository

# Save
def save(author):
    sql = """
    INSERT INTO author (name, title)
    VALUES (%s, %s) RETURNING *
    """
    values = [author.name, author.title]
    results = run_sql(sql, values)
    # THis code block injects the author id at the front of list
    id = results[0]["id"]
    author.id = id
    return author


# Select all


# Select id


# Delete all


# Delete (id)
def delete_all():
    sql = "DELETE  FROM author"
    run_sql(sql)


# Update
