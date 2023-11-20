from flask_restful import Resource, reqparse
from src.models.user import User
from src.database.database import db
from src.services.user_service import UserService


class UserResource(Resource):
    def get(self, user_id=None):
        user = UserService.get_user(user_id)
        if user:
            return {"user": user.to_dict()}
        else:
            return {"message": "User not found"}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('url_link', type=str, required=True, help='url_link is required')
        parser.add_argument('name', type=str, required=True, help='name is required')

        args = parser.parse_args()

        response = UserService.create_user(url_link=args['url_link'], name=args['name'])

        return {"message": response}, 201

    def put(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument('url_link', type=str)
        parser.add_argument('name', type=str)

        args = parser.parse_args()

        response = UserService.update_user(user_id, url_link=args['url_link'], name=args['name'])

        if response:
            return {"message": "User updated successfully"}
        else:
            return {"message": "User not found"}, 404

    def delete(self, user_id):
        response = UserService.delete_user(user_id)

        if response:
            return {"message": "User deleted successfully"}
        else:
            return {"message": "User not found"}, 404
