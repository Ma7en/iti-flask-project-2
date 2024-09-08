from flask import render_template, request, redirect, url_for, Blueprint
from werkzeug.utils import secure_filename
import os, datetime
from flask_login import login_required, current_user

# db
from app.models import Categories, db

# apps
from app.categories import categories_blueprint
from app.categories.forms import CategoriesForm


# =================================================================================================
# *** list categories ***
@categories_blueprint.route("/", endpoint="list")
def categories_list():
    categories = Categories.query.all()
    return render_template("categories/list.html", categories=categories)


# =================================================================================================
# *** create category ***
# @categories_blueprint.route("create", endpoint="create", methods=["GET", "POST"])
# def categories_create():
#     if request.method == "POST":
#         category = Categories(
#             name=request.form["name"],
#             image=request.form["image"],
#         )
#         db.session.add(category)
#         db.session.commit()
#         return redirect(category.show_url)
#     return render_template("categories/forms/create.html")


@categories_blueprint.route("create", endpoint="create", methods=["GET", "POST"])
@login_required
def categories_create():
    form = CategoriesForm()
    date = datetime.datetime.now()
    default_image = "default_image.jpg"

    if request.method == "POST":
        if form.validate_on_submit():
            con_name = default_image

            if request.files.get("image"):
                image = form.image.data
                image_name = secure_filename(image.filename)
                con_name = f"{date.day}-{date.hour}-{date.minute}-{image_name}"
                image.save(
                    os.path.join("static/assets/images/categories/", con_name)
                )  # image_name

                # data = dict(request.form)
                # del data["csrf_token"]
                # del data["submit"]

                # data["image"] = con_name
                # category = Categories(**data)

            # print("=============================")
            # print("current user")
            # print(current_user)
            # print("=============================")

            category = Categories(
                name=form.name.data,
                image=con_name,
                user_id=current_user.id,
            )

            db.session.add(category)
            db.session.commit()

            return redirect(category.show_url)
    return render_template("categories/forms/create.html", form=form)


# =================================================================================================
# *** update category ***
# @categories_blueprint.route(
#     "<int:id>/update", endpoint="update", methods=["GET", "POST"]
# )
# def categories_update(id):
#     category = db.get_or_404(Categories, id)
#     if request.method == "POST":
#         categoryobj = category
#         categoryobj.name = request.form["name"]
#         categoryobj.image = request.form["image"]
#         db.session.add(categoryobj)
#         db.session.commit()
#         return redirect(url_for("categories.list"))

#     return render_template("categories/forms/update.html", category=category)


@categories_blueprint.route(
    "<int:id>/update", endpoint="update", methods=["GET", "POST"]
)
@login_required
def categories_update(id):
    category = db.get_or_404(Categories, id)
    if category is None:
        return redirect(url_for("categories.list"))

    if category.user_id != current_user.id:
        return redirect(url_for("categories.list"))

    form = CategoriesForm(obj=category)
    date = datetime.datetime.now()
    default_image = "default_image.jpg"

    if request.method == "POST":
        if form.validate_on_submit():
            con_name = category.image or default_image

            if form.image.data:
                image = form.image.data
                image_name = secure_filename(image.filename)
                con_name = f"{date.day}-{date.hour}-{date.minute}-{image_name}"
                image.save(os.path.join("static/assets/images/categories/", con_name))

            category.name = form.name.data
            category.image = con_name  # Save new image name
            db.session.commit()

            return redirect(category.show_url)

    return render_template("categories/forms/update.html", form=form, category=category)


# =================================================================================================
# *** show details category ***
@categories_blueprint.route("<int:id>", endpoint="show")
def category_show(id):
    category = db.get_or_404(Categories, id)
    return render_template("categories/show.html", category=category)


# =================================================================================================
# *** delete category ***
@categories_blueprint.route("<int:id>/delete", endpoint="delete", methods=["POST"])
@login_required
def categories_delete(id):
    category = db.get_or_404(Categories, id)
    if category is None:
        return redirect(url_for("categories.list"))

    if category.user_id != current_user.id:
        return redirect(url_for("categories.list"))

    default_image = "default_image.jpg"

    if category.image and category.image != default_image:
        image_path = os.path.join("static/assets/images/categories/", category.image)
        if os.path.exists(image_path):
            os.remove(image_path)

    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories.list"))
