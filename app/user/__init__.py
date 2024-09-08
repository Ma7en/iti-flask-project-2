from flask import Blueprint
import flask_login

# configuration database user
from app.models import User

# login
login_manager = flask_login.LoginManager()
login_manager.login_view = "user.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


users_blueprint = Blueprint("user", __name__, url_prefix="/user")

from app.user import views
