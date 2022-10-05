from flask import Flask, render_template
from flask import Blueprint

from models.book import Book
from models.author import Author

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

books_blueprint = Blueprint("Books", __name__)
