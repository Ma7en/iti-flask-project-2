from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, EmailField, PasswordField, FileField
from wtforms.validators import DataRequired, Length


# =============================================================================
# *** Register Form ***
class RegisterForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired(), Length(2, 100)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(2, 100)])
    username = StringField("UserName", validators=[DataRequired(), Length(2, 200)])
    email = EmailField("Email", validators=[DataRequired(), Length(2, 300)])
    password = PasswordField("Password", validators=[DataRequired()])
    image = FileField("Image", validators=[])
    submit = SubmitField("Register")
