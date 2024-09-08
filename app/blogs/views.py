from flask import render_template, request, redirect, url_for, Blueprint
from werkzeug.utils import secure_filename
import os, datetime
from flask_login import login_required, current_user

# db
from app.models import Blogs, db, Categories

# blogs
from app.blogs import blogs_blueprint
from app.blogs.forms import BlogsForm


# =================================================================================================
# *** list blogs ***
@blogs_blueprint.route("/", endpoint="list")
def blogs_list():
    blogs = Blogs.query.all()
    return render_template("blogs/list.html", blogs=blogs)


# =================================================================================================
# *** creat blog ***
# @blogs_blueprint.route("create", endpoint="create", methods=["GET", "POST"])
# def blogs_create():
#     categories = Categories.query.all()
#     if request.method == "POST":

#         blog = Blogs(
#             name=request.form["name"],
#             description=request.form["description"],
#             image=request.form["image"],
#             category_id=request.form["category_id"],
#         )
#         db.session.add(blog)
#         db.session.commit()
#         return redirect(blog.show_url)
#     return render_template("blogs/create.html", categories=categories)


# @blogs_blueprint.route("create", endpoint="create", methods=["GET", "POST"])
# def blogs_create():
#     form = BlogsForm()
#     date = datetime.datetime.now()

#     if request.method == "POST":
#         if form.validate_on_submit():
#             image_name = None
#             if request.files.get("image"):
#                 image = form.image.data
#                 image_name = secure_filename(image.filename)
#                 con_name = f"{date.day}-{date.hour}-{date.minute}-{image_name}"
#                 image.save(
#                     os.path.join("static/assets/images/blogs/", con_name)
#                 )  # image_name

#             data = dict(request.form)
#             del data["csrf_token"]
#             del data["submit"]
#             # save only image name
#             data["image"] = con_name
#             blog = Blogs(**data)
#             db.session.add(blog)
#             db.session.commit()

#             return redirect(blog.show_url)
#     return render_template("blogs/forms/create.html", form=form)


@blogs_blueprint.route("create", endpoint="create", methods=["GET", "POST"])
@login_required
def blogs_create():
    # print("===================================")
    # print(request.form)
    # print("===================================")
    form = BlogsForm()
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
                    os.path.join("static/assets/images/blogs/", con_name)
                )  # image_name

            data = dict(request.form)
            # print("=============================")
            # print("data blogs")
            # print(
            #     data
            # )  # { 'name': 'vb', 'description': 'vb', 'category_id': '1', 'submit': 'Submit'}
            # print("=============================")
            # del data["csrf_token"]
            # del data["submit"]

            # data["image"] = con_name
            # blog = Blogs(**data)
            blog = Blogs(
                name=data["name"],
                description=data["description"],
                image=con_name,
                category_id=data["category_id"],
                user_id=current_user.id,  # current user id for testing purpose, replace with actual user id when implemented with login system.  # current_user.id,  # current user id for testing purpose, replace with actual user id when implemented with login system.  # current_user.id,  # current user id for testing purpose, replace with actual user id when implemented with login system.  # current_user.id,  # current user id for testing purpose, replace with actual user id when implemented with login system.  # current_user.id,  # current user id for testing purpose, replace with actual user id when implemented with login system.  # current_user.id,  # current user id for testing purpose, replace with actual user id when implemented with login
            )

            db.session.add(blog)
            db.session.commit()

            return redirect(blog.show_url)
    return render_template("blogs/forms/create.html", form=form)


# =================================================================================================
# *** update blogs ***
# @blogs_blueprint.route("<int:id>/update", endpoint="update", methods=["GET", "POST"])
# def blogs_update(id):
#     blog = db.get_or_404(Blogs, id)
#     if request.method == "POST":
#         # print("requested blog----------->\n", request.form)
#         # print("-==->", request.POST["name"])
#         # print("-==->", request.form["name"])
#         blogobj = blog
#         blogobj.name = request.form["name"]
#         blogobj.description = request.form["description"]
#         blogobj.image = request.form["image"]
#         db.session.add(blogobj)
#         db.session.commit()
#         return redirect(url_for("blogs.list"))
#     return render_template("blogs/update.html", blog=blog)


@blogs_blueprint.route("<int:id>/update", endpoint="update", methods=["GET", "POST"])
@login_required
def blogs_update(id):
    blog = db.get_or_404(Blogs, id)
    if blog is None:
        return redirect(url_for("blogs.list"))

    if blog.user_id != current_user.id:
        return redirect(url_for("blogs.list"))

    form = BlogsForm(obj=blog)
    date = datetime.datetime.now()
    default_image = "default_image.jpg"

    if request.method == "POST":
        if form.validate_on_submit():
            con_name = blog.image or default_image  # Keep existing image name

            if form.image.data:
                image = form.image.data
                image_name = secure_filename(image.filename)
                con_name = f"{date.day}-{date.hour}-{date.minute}-{image_name}"
                image.save(os.path.join("static/assets/images/blogs/", con_name))

            blog.name = form.name.data
            blog.description = form.description.data
            blog.image = con_name
            blog.category_id = form.category_id.data
            db.session.commit()

            return redirect(blog.show_url)

    return render_template("blogs/forms/update.html", form=form, blog=blog)


# =================================================================================================
# *** show details blog ***
@blogs_blueprint.route("<int:id>", endpoint="show")
def blog_show(id):
    blog = db.get_or_404(Blogs, id)
    return render_template("blogs/show.html", blog=blog)


# =================================================================================================
# *** delete blogs ***
@blogs_blueprint.route("<int:id>/delete", endpoint="delete", methods=["POST"])
@login_required
def blogs_delete(id):
    blog = db.get_or_404(Blogs, id)
    if blog is None:
        return redirect(url_for("blogs.list"))

    if blog.user_id != current_user.id:
        return redirect(url_for("blogs.list"))

    default_image = "default_image.jpg"

    if blog.image and blog.image != default_image:
        image_path = os.path.join("static/assets/images/blogs/", blog.image)
        if os.path.exists(image_path):
            os.remove(image_path)

    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for("blogs.list"))


# use -> url_for
# @blogs_blueprint.route("<int:id>/delete", endpoint="delete")
# def blogs_delete(id):
#     blog = db.get_or_404(Blogs, id)
#     db.session.delete(blog)
#     db.session.commit()
#     return redirect(url_for("blogs.list"))
