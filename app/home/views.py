from flask import render_template, request, redirect, url_for, Blueprint
from werkzeug.utils import secure_filename
import os, datetime

# flask login
from flask_login import login_required, current_user

# db
from app.models import db, Books, Categories

# app home
from app.home import home_blueprint


# =================================================================================================
# *** Home ***
@home_blueprint.route("/", endpoint="home")
def home():
    books = Books.query.all()
    categories = Categories.query.all()
    return render_template("home/home.html", books=books, categories=categories)


# =================================================================================================
# *** About Me ***
@home_blueprint.route("/aboutme", endpoint="about_me")
def aboutme():
    return render_template("home/about-me.html")


# =================================================================================================
# *** Contact ***
@home_blueprint.route("/contact", endpoint="contact")
def contact():
    return render_template("home/contact.html")
