from flask_restful import Resource, reqparse
from src.services.position_service import PositionService

class PositionResource(Resource):
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
