from flask import Flask
from flask_migrate import Migrate

from flask_bootstrap import Bootstrap5
from flask_restful import Resource, Api

# con
from app.models import db
from app.config import config_options

# user
from app.user import login_manager

# API
# from app.blogs.api.views import BlogsList, BlogsResource
# from app.categories.api.views import CategoriesList, CategoriesResource


def create_app(config_name="prd"):
    app = Flask(__name__)

    # config
    current_config = config_options[config_name]
    app.config.from_object(current_config)
    app.config.SQLALCHEMY_DATABASE_URI = current_config.SQLALCHEMY_DATABASE_URI

    db.init_app(app)
    migrate = Migrate(app, db)
    login_manager.init_app(app)

    # packages
    bootstrap = Bootstrap5(app)
    api = Api(app)

    # Apps
    # -1 -> Blogs
    from app.blogs import blogs_blueprint

    app.register_blueprint(blogs_blueprint)

    # -2 -> Categories
    from app.categories import categories_blueprint

    app.register_blueprint(categories_blueprint)

    # -3 -> Users
    from app.user import users_blueprint

    app.register_blueprint(users_blueprint)

    # -4 -> Home
    from app.home import home_blueprint

    app.register_blueprint(home_blueprint)

    # # API
    # # -1 -> Blogs
    # api.add_resource(BlogsList, "/api/blogs")
    # api.add_resource(BlogsResource, "/api/blogs/<int:id>")

    # # -2 -> Categories
    # api.add_resource(CategoriesList, "/api/categories")
    # api.add_resource(CategoriesResource, "/api/categories/<int:id>")

    return app
