from flask_wtf import FlaskForm

from wtforms import BooleanField, PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    email = StringField("email", validators = [DataRequired(), Email()])
    password = PasswordField("password", validators = [DataRequired()])
    submit = SubmitField("log in")


class PostForm(FlaskForm):
    title = StringField("title", validators = [DataRequired()])
    content = TextAreaField("content", validators = [DataRequired()])
    draft = BooleanField("this post is a draft")
    submit = SubmitField("post")