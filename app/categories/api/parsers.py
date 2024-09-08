from flask_restful import reqparse

categories_parser = reqparse.RequestParser()

categories_parser.add_argument("name", type=str, required=True, help="Name is required")
categories_parser.add_argument(
    "image", type=str, required=True, help="Image is required"
)
