from flask import Flask

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, FileField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange

# app
from app.models import Categories


# =================================================================================================
# *** Books Form ***
class BooksForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(2, 50)])
    description = StringField(
        "Description", validators=[DataRequired(), Length(2, 5000)]
    )
    image = FileField("Image", validators=[])
    pages = IntegerField(
        "Number Of Pages", validators=[DataRequired(), NumberRange(min=1)]
    )
    category_id = SelectField("Categories", validators=[DataRequired()], choices=[])
    submit = SubmitField("Submit")

    def __init__(self, *args, **kwargs):
        super(BooksForm, self).__init__(*args, **kwargs)
        self.category_id.choices = [(c.id, c.name) for c in Categories.query.all()]
