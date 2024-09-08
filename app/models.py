from flask_sqlalchemy import SQLAlchemy
from flask import url_for
from flask_login import UserMixin

# db
db = SQLAlchemy()


# =================================================================================================
# *** Users ***
class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(250), nullable=False)
    username = db.Column(db.String(250), unique=True, nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    image = db.Column(db.String(250), nullable=True)
    books = db.relationship("Books", backref="created_books", lazy=True)
    categories = db.relationship("Categories", backref="user_category", lazy=True)

    def __str__(self):
        return f"{self.username}"

    @property
    def image_url(self):
        return url_for("static", filename=f"assets/images/user/{self.image}")


# =================================================================================================
# *** Categories ***
class Categories(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    image = db.Column(db.String(250), nullable=True)
    books = db.relationship("Books", backref="category_ref", lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)

    def __str__(self):
        return f"{self.name}"

    @property
    def image_url(self):
        return url_for("static", filename=f"assets/images/categories/{self.image}")

    @property
    def show_url(self):
        return url_for("categories.show", id=self.id)

    @property
    def update_url(self):
        return url_for("categories.update", id=self.id)

    @property
    def delete_url(self):
        return url_for("categories.delete", id=self.id)


# =================================================================================================
# *** Books ***
class Books(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    description = db.Column(db.String(5000), nullable=True)
    image = db.Column(db.String(250), nullable=True)
    pages = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=True)

    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    category = db.relationship("Categories", backref=db.backref("books_ref", lazy=True))
    user = db.relationship("User", backref="created_books")

    # published_date = db.Column(db.Date, nullable=True)
    # author = db.Column(db.String(50), nullable=True)
    # rating = db.Column(db.Float, nullable=True)
    # isbn = db.Column(db.String(50), nullable=True)
    # pages = db.Column(db.Integer, nullable=True)
    # language = db.Column(db.String(50), nullable=True)
    # genre = db.Column(db.String(50), nullable=True)
    # status = db.Column(db.String(50), nullable=True)
    # available = db.Column(db.Boolean, nullable=True)
    # quantity = db.Column(db.Integer, nullable=True)
    # price = db.Column(db.Float, nullable=True)
    # stock = db.Column(db.Integer, nullable=True)
    # sold = db.Column(db.Integer, nullable=True)
    # discount = db.Column(db.Float, nullable=True)
    # views = db.Column(db.Integer, nullable=True)
    # created_at = db.Column(db.DateTime, nullable=True)
    # updated_at = db.Column(db.DateTime, nullable=True)
    # user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    # category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=True)

    def __str__(self):
        return f"{self.name}"

    @property
    def image_url(self):
        return url_for("static", filename=f"assets/images/books/{self.image}")

    @property
    def show_url(self):
        return url_for("books.show", id=self.id)

    @property
    def update_url(self):
        return url_for("books.update", id=self.id)

    @property
    def delete_url(self):
        return url_for("books.delete", id=self.id)
