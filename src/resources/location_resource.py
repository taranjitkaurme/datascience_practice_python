from flask_restful import Resource, reqparse
from src.models.user import User
from src.database.database import db


class LocationResource(Resource):

    def get(self, user_id=None):
        if user_id:
            user = User.query.get(user_id)
            if not user:
                return {"message": "User not found"}, 404
            return {"id": user.id, "username": user.username, "email": user.email}
        else:
            users = User.query.all()
            return [{"id": user.id, "username": user.username, "email": user.email} for user in users]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('url_link', type=str, required=True, help='url_link is required')
        parser.add_argument('name', type=str, required=True, help='name is required')

        args = parser.parse_args()

        new_user = User(url_link=args['url_link'], name=args['name'])
        db.session.add(new_user)
        db.session.commit()

        return {"message": "User created successfully"}, 201

    def put(self, user_id):
        # Update user logic here
        pass

    def delete(self, user_id):
        # Delete user logic here
        pass
