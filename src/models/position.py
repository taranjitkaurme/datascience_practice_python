from src.database.database import db



class Position(db.Model):
    """
    Represents a position in a company.

    Attributes:
        position_id (int): The unique identifier for the position.
        title (str): The title of the position.

    """
    __tablename__ = "position"

    position_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    #user_company_mapping = db.relationship('UserCompanyMapping', backref='position', lazy=True)

    # Other methods as needed
