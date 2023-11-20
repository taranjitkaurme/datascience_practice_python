from flask_restful import Resource, reqparse
from services.user_service import UserService
from services.location_service import LocationService

class UserLocationResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=int, required=True, help='User ID is required')
        parser.add_argument('location_id', type=int, required=True, help='Location ID is required')
        args = parser.parse_args()

        user = UserService.get_user(args['user_id'])
        if not user:
            return {"message": "User not found"}, 404

        location = LocationService.get_location(args['location_id'])
        if not location:
            return {"message": "Location not found"}, 404

        # Associate user with location logic here
        # This could involve updating the User model to include a location_id or creating a separate association table

        return {"message": "User associated with location successfully"}, 201
