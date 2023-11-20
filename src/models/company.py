# company.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Company(db.Model):
    __tablename__ = "company"

    company_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    user_company_mappings = db.relationship('UserCompanyMapping', backref='company', lazy=True)
