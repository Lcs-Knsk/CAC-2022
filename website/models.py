from . import db
from flask_login import UserMixin


class db_coopersrock(db.Model):
    id = db.Column(db.String(1000), primary_key=True)
    date = db.Column(db.String(100))
    location = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    is_caution = db.Column(db.Boolean, unique=False, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class db_greenbrier(db.Model):
    id = db.Column(db.String(1000), primary_key=True)
    date = db.Column(db.String(100))
    location = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    is_caution = db.Column(db.Boolean, unique=False, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class db_cabwaylingo(db.Model):
    id = db.Column(db.String(1000), primary_key=True)
    date = db.Column(db.String(100))
    location = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    is_caution = db.Column(db.Boolean, unique=False, default=False)    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class db_calvinPrice(db.Model):
    id = db.Column(db.String(1000), primary_key=True)
    date = db.Column(db.String(100))
    location = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    is_caution = db.Column(db.Boolean, unique=False, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class db_campCreek(db.Model):
    id = db.Column(db.String(1000), primary_key=True)
    date = db.Column(db.String(100))
    location = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    is_caution = db.Column(db.Boolean, unique=False, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class db_kanawha(db.Model):
    id = db.Column(db.String(1000), primary_key=True)
    date = db.Column(db.String(100))
    location = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    is_caution = db.Column(db.Boolean, unique=False, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class db_kumbrabow(db.Model):
    id = db.Column(db.String(1000), primary_key=True)
    date = db.Column(db.String(100))
    location = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    is_caution = db.Column(db.Boolean, unique=False, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class db_panther(db.Model):
    id = db.Column(db.String(1000), primary_key=True)
    date = db.Column(db.String(100))
    location = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    is_caution = db.Column(db.Boolean, unique=False, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class db_seneca(db.Model):
    id = db.Column(db.String(1000), primary_key=True)
    date = db.Column(db.String(100))
    location = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    is_caution = db.Column(db.Boolean, unique=False, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    uploadsCR = db.relationship('db_coopersrock')
    uploadsGB = db.relationship('db_greenbrier')
    uploadsCWL = db.relationship('db_cabwaylingo')
    uploadsCP = db.relationship('db_calvinPrice')
    uploadsCC = db.relationship('db_campCreek')
    uploadsKNW = db.relationship('db_kanawha')
    uploadsKBB = db.relationship('db_kumbrabow')
    uploadsP = db.relationship('db_panther')
    uploadsS = db.relationship('db_seneca')
