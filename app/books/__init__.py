from flask import Blueprint

books_blueprint = Blueprint("books", __name__, url_prefix="/books")

from app.books import views
