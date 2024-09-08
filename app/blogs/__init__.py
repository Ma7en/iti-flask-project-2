from flask import Blueprint

blogs_blueprint = Blueprint("blogs", __name__, url_prefix="/blogs")

from app.blogs import views
