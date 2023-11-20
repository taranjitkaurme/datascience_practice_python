# position.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Position(db.Model):
    __tablename__ = "position"

    position_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    user_company_mappings = db.relationship('UserCompanyMapping', backref='position', lazy=True)

    # Other methods as needed
