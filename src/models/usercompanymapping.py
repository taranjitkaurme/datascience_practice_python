from src.database.database import db


class UserCompanyMapping(db.Model):
    """
    Represents the mapping between a user, a company, a position, and a location.

    Attributes:
        mapping_id (int): The unique identifier for the mapping.
        user_id (int): The user's unique identifier.
        company_id (int): The company's unique identifier.
        position_id (int): The position's unique identifier.
        location_id (int): The location's unique identifier.
        start_year (int): The starting year of the user's association with the company.
        end_year (int): The ending year of the user's association with the company.
        current_company (bool): Indicates if the user is currently associated with the company.

    Relationships:
        user (User): The user associated with the mapping.
        company (Company): The company associated with the mapping.
        position (Position): The position associated with the mapping.
        location (Location): The location associated with the mapping.
    """

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