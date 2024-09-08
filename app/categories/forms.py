from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired, Length


# start class
class CategoriesForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(2, 100)])
    image = FileField("Image", validators=[])
    submit = SubmitField("Submit")
