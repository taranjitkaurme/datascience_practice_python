from flask_restful import Resource, reqparse
from src.services.user_service import UserService
from src.utility.decorators import log_request


class UserResource(Resource):
    """
    Represents the RESTful API resource for managing user information.

    Endpoints:
        GET /api/user/<int:user_id>:
            Retrieves information about a specific user.
        POST /api/user:
            Creates a new user.
        PUT /api/user/<int:user_id>:
            Updates information about a specific user.
        DELETE /api/user/<int:user_id>:
            Deletes a specific user.

    Methods:
        get(self, user_id=None):
            Retrieves information about a specific user or a list of all users.

        post(self):
            Creates a new user based on the provided information.

        put(self, user_id):
            Updates information about a specific user.

        delete(self, user_id):
            Deletes a specific user.

    Request Parameters:
        user_id (int, optional): The unique identifier of the user (for GET, PUT, and DELETE operations).

    Request JSON Payload (for POST and PUT operations):
        {
            "url_link": "User URL Link",
            "name": "User Name"
        }

    Returns:
        dict: A JSON response containing the result of the corresponding operation.

    """

    @log_request
    def get(self, user_id=None):
        try:
            user = UserService.get_user(user_id)
            if user:
                return {"user": user}
            else:
                return {"message": "User not found"}, 404
        except Exception as e:
            return {"message": str(e)}, 500

    @log_request
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('url_link', type=str, required=True, help='url_link is required')
            parser.add_argument('name', type=str, required=True, help='name is required')
            args = parser.parse_args()

            response = UserService.create_user(url_link=args['url_link'], name=args['name'])

            return {"message": response}, 201
        except Exception as e:
            return {"message": str(e)}, 400

    @log_request
    def put(self, user_id):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('url_link', type=str)
            parser.add_argument('name', type=str)
            args = parser.parse_args()

            response = UserService.update_user(user_id, url_link=args['url_link'], name=args['name'])

            if response:
                return {"message": "User updated successfully"}
            else:
                return {"message": "User not found"}, 404
        except Exception as e:
            return {"message": str(e)}, 500

    @log_request
    def delete(self, user_id):
        try:
            response = UserService.delete_user(user_id)

            if response:
                return {"message": "User deleted successfully"}
            else:
                return {"message": "User not found"}, 404
        except Exception as e:
            return {"message": str(e)}, 500
