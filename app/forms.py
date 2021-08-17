from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    email = StringField("email", validators = [DataRequired(), Email()])
    password = PasswordField("password", validators = [DataRequired()])
    submit = SubmitField("log in")
