from src.database.database import db
class Company(db.Model):

    """
    Represents a company.

    Attributes:
        company_id (int): The unique identifier for the company.
        name (str): The name of the company.

    """

    __tablename__ = "company"

    company_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    #user_company_mapping = db.relationship('UserCompanyMapping', backref='company', lazy=True)
