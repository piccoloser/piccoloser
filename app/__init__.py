from flask import Flask

from flask_bcrypt import Bcrypt

from flask_login import LoginManager

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, static_folder="./static")
app.config["SECRET_KEY"] = "1894634d971c90919080fe90c85882da"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

bc = Bcrypt(app)
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"


from app import routes