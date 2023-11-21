from src.models.location import Location
from src.database.database import db
class LocationService:

    """
    Service class for managing location-related operations.

    Methods:
        get_location(location_id=None):
            Retrieves information about a specific location or a list of all locations.

        create_location(city, state, country):
            Creates a new location with the provided city, state, and country.

        update_location(location_id, city, state, country):
            Updates information about a specific location.

        delete_location(location_id):
            Deletes a specific location.

    Parameters:
        location_id (int, optional): The unique identifier of the location (for get, update, and delete operations).
        city (str): The city of the location (for create and update operations).
        state (str): The state of the location (for create and update operations).
        country (str): The country of the location (for create and update operations).

    Returns:
        dict: A dictionary containing the result of the corresponding operation.

    Example Usage:
        location_service = LocationService()
        location_info = location_service.get_location(location_id=1)
        new_location_result = location_service.create_location(city="New City", state="New State", country="New Country")
        update_location_result = location_service.update_location(location_id=1, city="Updated City", state="Updated State", country="Updated Country")
        delete_location_result = location_service.delete_location(location_id=1)

    """

    @staticmethod
    def get_location(location_id=None):
        if location_id:
            location = Location.query.get(location_id)
            if not location:
                return {"message": "Location not found"}, 404
            return {
                "location_id": location.location_id,
                "city": location.city,
                "state": location.state,
                "country": location.country
            }
        else:
            locations = Location.query.all()
            return [{
                "location_id": location.location_id,
                "city": location.city,
                "state": location.state,
                "country": location.country
            } for location in locations]

    @staticmethod
    def create_location(city, state, country):
        new_location = Location(city=city, state=state, country=country)
        db.session.add(new_location)
        db.session.commit()
        return {"message": "Location created successfully"}, 201

    @staticmethod
    def update_location(location_id, city, state, country):
        location = Location.query.get(location_id)
        if location:
            location.city = city
            location.state = state
            location.country = country
            db.session.commit()
            return {"message": "Location updated successfully"}
        else:
            return {"message": "Location not found"}, 404

    @staticmethod
    def delete_location(location_id):
        location = Location.query.get(location_id)
        if location:
            db.session.delete(location)
            db.session.commit()
            return {"message": "Location deleted successfully"}
        else:
            return {"message": "Location not found"}, 404
