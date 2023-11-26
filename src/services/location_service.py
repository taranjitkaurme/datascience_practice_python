from src.models.location import Location
from src.database.database import db


class LocationService:

    @staticmethod
    def get_location(location_id=None):
        try:
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
        except Exception as e:
            # Log the exception or handle it accordingly
            return {"message": f"Error in get_location: {str(e)}"}, 500

    @staticmethod
    def create_location(city, state, country):
        try:
            new_location = Location(city=city, state=state, country=country)
            db.session.add(new_location)
            db.session.commit()
            return {"message": "Location created successfully"}, 201
        except Exception as e:
            # Log the exception or handle it accordingly
            return {"message": f"Error in create_location: {str(e)}"}, 500

    @staticmethod
    def update_location(location_id, city, state, country):
        try:
            location = Location.query.get(location_id)
            if location:
                location.city = city
                location.state = state
                location.country = country
                db.session.commit()
                return {"message": "Location updated successfully"}
            else:
                return {"message": "Location not found"}, 404
        except Exception as e:
            # Log the exception or handle it accordingly
            return {"message": f"Error in update_location: {str(e)}"}, 500

    @staticmethod
    def delete_location(location_id):
        try:
            location = Location.query.get(location_id)
            if location:
                db.session.delete(location)
                db.session.commit()
                return {"message": "Location deleted successfully"}
            else:
                return {"message": "Location not found"}, 404
        except Exception as e:
            # Log the exception or handle it accordingly
            return {"message": f"Error in delete_location: {str(e)}"}, 500
