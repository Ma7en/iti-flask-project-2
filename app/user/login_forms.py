from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, EmailField, PasswordField, FileField
from wtforms.validators import DataRequired, Length


# =============================================================================
# *** Loging Form ***
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
