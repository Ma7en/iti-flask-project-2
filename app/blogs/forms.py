from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, SelectField, FileField
from wtforms.validators import DataRequired, Length
from app.models import Categories


# start class
class BlogsForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(2, 50)])
    description = StringField(
        "Description", validators=[DataRequired(), Length(2, 5000)]
    )
    image = FileField("Image", validators=[])
    category_id = SelectField("Categories", validators=[DataRequired()], choices=[])
    submit = SubmitField("Submit")

    def __init__(self, *args, **kwargs):
        super(BlogsForm, self).__init__(*args, **kwargs)
        self.category_id.choices = [(c.id, c.name) for c in Categories.query.all()]
