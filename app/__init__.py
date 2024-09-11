from flask import Flask, render_template
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap5
from flask_restful import Resource, Api

# configuration database
from app.models import db
from app.config import config_options

# user
from app.user import login_manager

# API
# from app.books.api.views import BooksList, BooksResource
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
    # -1 -> Users
    from app.user import users_blueprint

    app.register_blueprint(users_blueprint)

    # -2 -> Home
    from app.home import home_blueprint

    app.register_blueprint(home_blueprint)

    # -3 -> Books
    from app.books import books_blueprint

    app.register_blueprint(books_blueprint)

    # -4 -> Categories
    from app.categories import categories_blueprint

    app.register_blueprint(categories_blueprint)

    # 404
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("error/404.html"), 404

    # # API
    # # -1 -> Books
    # api.add_resource(BooksList, "/api/books")
    # api.add_resource(BooksResource, "/api/books/<int:id>")

    # # -2 -> Categories
    # api.add_resource(CategoriesList, "/api/categories")
    # api.add_resource(CategoriesResource, "/api/categories/<int:id>")

    return app
