from flask_restful import fields

categories_serializers = {
    "id": fields.Integer,
    "name": fields.String,
    "image": fields.String,
}
