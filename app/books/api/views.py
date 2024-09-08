from flask_restful import Resource, Api, marshal_with
from app.models import db, Blogs
from app.blogs.api.seriailzers import blogs_serializers
from app.blogs.api.parsers import blogs_parser


class BlogsList(Resource):
    @marshal_with(blogs_serializers)
    def get(self):
        blogs = Blogs.query.all()
        return blogs, 200

    @marshal_with(blogs_serializers)
    def post(self):
        blogs_args = blogs_parser.parse_args()
        blog = Blogs(**blogs_args)  # dictionary
        db.session.add(blog)
        db.session.commit()
        return "blogs", 201


class BlogsResource(Resource):
    @marshal_with(blogs_serializers)
    def get(self, id):
        blog = db.get_or_404(Blogs, id)
        return blog, 200

    @marshal_with(blogs_serializers)
    def put(self, id):
        blog = db.get_or_404(Blogs, id)
        blogs_args = blogs_parser.parse_args()
        blog.name = blogs_args["name"]
        blog.description = blogs_args["description"]
        blog.image = blogs_args["image"]
        blog.category_id = blogs_args["category_id"]
        db.session.add(blog)
        db.session.commit()

        return blog, 200

        # for key, value in blogs_args.items():
        #     setattr(blog, key, value)
        # db.session.commit()
        # return blog, 200

    def delete(self, id):
        blog = db.get_or_404(Blogs, id)
        db.session.delete(blog)
        db.session.commit()
        return "deleted", 204
