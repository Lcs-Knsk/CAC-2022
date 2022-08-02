from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

class db_coopersrock(db.Model):
    id = db.Column(db.String(1000), primary_key=True)
    date = db.Column(db.String(100))
    location = db.Column(db.String(100))
    description = db.Column(db.String(1000))


