from flask_restful import reqparse

books_parser = reqparse.RequestParser()

books_parser.add_argument("name", type=str, required=True, help="Name is required")
books_parser.add_argument(
    "description", type=str, required=True, help="Description is required"
)
books_parser.add_argument("image", type=str, required=True, help="Image is required")
books_parser.add_argument(
    "category_id", type=int, required=True, help="Category ID is required"
)
