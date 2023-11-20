from src.models.user import User
from src.database.database import db


class UserService:

    def get_user(user_id=None):
        if user_id:
            user = User.query.get(user_id)
            if not user:
                return {"message": "User not found"}, 404
            return {"id": user.id, "username": user.username, "email": user.email}
        else:
            users = User.query.all()
            return [{"id": user.id, "username": user.username, "email": user.email} for user in users]

    def post(user):


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
