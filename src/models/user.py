# user.py
from src.database.database import db



class User(db.Model):
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    url_link = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(255))
    #location_id = db.Column(db.Integer, db.ForeignKey('location.location_id'))

    # location = db.relationship('Location', backref='user', lazy=True)
    # user_company_mappings = db.relationship('UserCompanyMapping', backref='user', lazy=True)
