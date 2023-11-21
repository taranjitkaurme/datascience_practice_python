from src.database.database import db

class Location(db.Model):

    """
    Represents a location.

    Attributes:
        location_id (int): The unique identifier for the location.
        city (str): The city of the location.
        state (str): The state of the location.
        country (str): The country of the location.
    """

    __tablename__ = "location"

    location_id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    country = db.Column(db.String(255))
    # Add other location-related fields as needed

    # Other methods as needed
