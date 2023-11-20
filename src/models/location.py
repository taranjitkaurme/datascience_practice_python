from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Location(db.Model):
    __tablename__ = "location"

    location_id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    country = db.Column(db.String(255))
    # Add other location-related fields as needed

    # Other methods as needed
