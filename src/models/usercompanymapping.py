from src.database.database import db


class UserCompanyMapping(db.Model):
    __tablename__ = "user_company_mapping"

    mapping_id = db.Column(db.Integer, primary_key=True)

    # Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.company_id'), nullable=False)
    position_id = db.Column(db.Integer, db.ForeignKey('position.position_id'))
    location_id = db.Column(db.Integer, db.ForeignKey('location.location_id'))

    # Other Columns
    start_year = db.Column(db.Integer)
    end_year = db.Column(db.Integer)
    current_company = db.Column(db.Boolean, default=False)

    # Relationships
    user = db.relationship('User', backref='user_company_mappings')
    company = db.relationship('Company', backref='user_company_mappings')
    position = db.relationship('Position', backref='user_company_mappings')
    location = db.relationship('Location', backref='user_company_mappings')