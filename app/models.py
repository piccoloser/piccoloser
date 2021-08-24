from app import db, login_manager

from datetime import datetime

from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String, nullable = False)
    last_name = db.Column(db.String, nullable = False)
    email = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)

    posts = db.relationship("Post", backref = "author", lazy = True)
    
    def __repr__(self):
        return f'{ self.first_name } { self.last_name } <{ self.email }>'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable = False)
    date = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    content = db.Column(db.Text, nullable = False)
    draft = db.Column(db.Boolean, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)

    def __repr__(self):
        return f'{ self.title }, posted { self.date }'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)