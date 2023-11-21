from flask_restful import Resource, reqparse
from src.services.position_service import PositionService

class PositionResource(Resource):

    """
    Represents the RESTful API resource for managing position information.

    Endpoints:
        GET /api/position/<int:position_id>:
            Retrieves information about a specific position.
        POST /api/position:
            Creates a new position.
        PUT /api/position/<int:position_id>:
            Updates information about a specific position.
        DELETE /api/position/<int:position_id>:
            Deletes a specific position.

    Methods:
        get(self, position_id=None):
            Retrieves information about a specific position or a list of all positions.

        post(self):
            Creates a new position based on the provided information.

        put(self, position_id):
            Updates information about a specific position.

        delete(self, position_id):
            Deletes a specific position.

    Request Parameters:
        position_id (int, optional): The unique identifier of the position (for GET, PUT, and DELETE operations).

    Request JSON Payload (for POST and PUT operations):
        {
            "title": "Position Title"
        }

    Returns:
        dict: A JSON response containing the result of the corresponding operation.

    """

    def get(self, position_id=None):
        return PositionService.get_position(position_id)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True, help='title is required')

        args = parser.parse_args()

        return PositionService.create_position(title=args['title'])

    def put(self, position_id):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True, help='title is required')

        args = parser.parse_args()

        return PositionService.update_position(position_id=position_id, title=args['title'])

    def delete(self, position_id):
        return PositionService.delete_position(position_id)
