# user.py
from src.database.database import db




class User(db.Model):
    """
       Represents a user in the system.

       Attributes:
           user_id (int): The unique identifier for the user.
           url (str): The unique URL link associated with the user.
           name (str): The name of the user.
    """

    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(255))
    # location_id = db.Column(db.Integer, db.ForeignKey('location.location_id'))

    # location = db.relationship('Location', backref='user', lazy=True)
    # user_company_mappings = db.relationship('UserCompanyMapping', backref='user', lazy=True)
