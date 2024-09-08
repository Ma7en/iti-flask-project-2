from flask import Flask

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired, Length


# start class
class CategoriesForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(2, 100)])
    image = FileField("Image", validators=[])
    submit = SubmitField("Submit")
