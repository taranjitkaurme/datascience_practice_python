# user.py
from flask_sqlalchemy import SQLAlchemy
from .location import Location

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    url_link = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(255))

    location_id = db.Column(db.Integer, db.ForeignKey('location.user_id'))
    location = db.relationship('Location', backref='users', lazy=True)

    user_company_mappings = db.relationship('UserCompanyMapping', backref='user', lazy=True)
