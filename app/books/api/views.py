from flask_restful import Resource, Api, marshal_with

# configuration database
from app.models import db, Books

# api
from app.books.api.seriailzers import books_serializers
from app.books.api.parsers import books_parser


class BooksList(Resource):
    @marshal_with(books_serializers)
    def get(self):
        books = Books.query.all()
        return books, 200

    @marshal_with(books_serializers)
    def post(self):
        books_args = books_parser.parse_args()
        book = Books(**books_args)  # dictionary
        db.session.add(book)
        db.session.commit()
        return "books", 201


class BooksResource(Resource):
    @marshal_with(books_serializers)
    def get(self, id):
        book = db.get_or_404(Books, id)
        return book, 200

    @marshal_with(books_serializers)
    def put(self, id):
        book = db.get_or_404(Books, id)
        books_args = books_parser.parse_args()

        book.name = books_args["name"]
        book.description = books_args["description"]
        book.image = books_args["image"]
        book.category_id = books_args["category_id"]

        db.session.add(book)
        db.session.commit()

        return book, 200

    def delete(self, id):
        book = db.get_or_404(Books, id)
        db.session.delete(book)
        db.session.commit()
        return "deleted", 204
