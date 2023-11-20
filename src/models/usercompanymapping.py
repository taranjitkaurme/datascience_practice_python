from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserCompanyMapping(db.Model):
    __tablename__ = "user_company_mapping"

    mapping_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.company_id'), nullable=False)
    position_id = db.Column(db.Integer, db.ForeignKey('position.position_id'))
    start_year = db.Column(db.Integer)
    end_year = db.Column(db.Integer)
    current_company = db.Column(db.Boolean, default=False)
    position = db.relationship('Position', backref='user_company_mappings')
