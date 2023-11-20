from flask_restful import Resource, reqparse
from src.services.location_service import LocationService

class LocationResource(Resource):
    def get(self, location_id=None):
        return LocationService.get_location(location_id)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('city', type=str, required=True, help='city is required')
        parser.add_argument('state', type=str, required=True, help='state is required')

        args = parser.parse_args()

        return LocationService.create_location(city=args['city'], state=args['state'])

    def put(self, location_id):
        parser = reqparse.RequestParser()
        parser.add_argument('city', type=str, required=True, help='city is required')
        parser.add_argument('state', type=str, required=True, help='state is required')

        args = parser.parse_args()

        return LocationService.update_location(location_id=location_id, city=args['city'], state=args['state'])

    def delete(self, location_id):
        return LocationService.delete_location(location_id)
