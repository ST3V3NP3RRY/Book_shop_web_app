import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

# THIS WORKS :)
author1 = Author("J R R Tolkien", "Mr")
author_repository.save(author1)

book1 = Book("The Lord of The Rings", "Fantasy", 678887, author1)

book_repository.save(book1)


# pdb.set_trace()
