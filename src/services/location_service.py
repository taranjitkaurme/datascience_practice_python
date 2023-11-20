from src.models.location import Location
from src.database.database import db
class LocationService:
    @staticmethod
    def get_location(location_id=None):
        if location_id:
            location = Location.query.get(location_id)
            if not location:
                return {"message": "Location not found"}, 404
            return {
                "location_id": location.location_id,
                "city": location.city,
                "state": location.state
            }
        else:
            locations = Location.query.all()
            return [{
                "location_id": location.location_id,
                "city": location.city,
                "state": location.state
            } for location in locations]

    @staticmethod
    def create_location(city, state):
        new_location = Location(city=city, state=state)
        db.session.add(new_location)
        db.session.commit()
        return {"message": "Location created successfully"}, 201

    @staticmethod
    def update_location(location_id, city, state):
        location = Location.query.get(location_id)
        if location:
            location.city = city
            location.state = state
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
