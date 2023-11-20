from src.database.database import db
class Position(db.Model):
    __tablename__ = "position"

    position_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    #user_company_mapping = db.relationship('UserCompanyMapping', backref='position', lazy=True)

    # Other methods as needed
