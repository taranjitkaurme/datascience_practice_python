from src.database.database import db
class Company(db.Model):
    __tablename__ = "company"

    company_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    #user_company_mapping = db.relationship('UserCompanyMapping', backref='company', lazy=True)
