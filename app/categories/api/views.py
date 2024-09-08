from flask_restful import Resource, Api, marshal_with
from app.models import db, Categories
from app.categories.api.seriailzers import categories_serializers
from app.categories.api.parsers import categories_parser


class CategoriesList(Resource):
    @marshal_with(categories_serializers)
    def get(self):
        categories = Categories.query.all()
        return categories, 200

    @marshal_with(categories_serializers)
    def post(self):
        categories_args = categories_parser.parse_args()
        category = Categories(**categories_args)  # dictionary
        db.session.add(category)
        db.session.commit()
        return "category", 201


class CategoriesResource(Resource):
    @marshal_with(categories_serializers)
    def get(self, id):
        category = db.get_or_404(Categories, id)
        return category, 200

    @marshal_with(categories_serializers)
    def put(self, id):
        category = db.get_or_404(Categories, id)
        categories_args = categories_parser.parse_args()

        category.name = categories_args["name"]
        category.image = categories_args["image"]
        db.session.add(category)
        db.session.commit()

        return category, 200

    def delete(self, id):
        category = db.get_or_404(Categories, id)
        db.session.delete(category)
        db.session.commit()
        return "deleted", 204
