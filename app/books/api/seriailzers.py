from flask_restful import fields

category_serializers = {
    "id": fields.Integer,
    "name": fields.String,
    # "image": fields.String,
    # "blogs": fields.List(fields.Nested(blogs_serializers)),  # list of blogs related to this category.
}

books_serializers = {
    "id": fields.Integer,
    "name": fields.String,
    "description": fields.String,
    "image": fields.String,
    "category_id": fields.Integer,
    "category": fields.Nested(category_serializers),
}
