from src.models.user import User
from src.database.database import db


class UserService:

    @staticmethod
    def get_user(user_id):
        try:
            if user_id:
                user = User.query.get(user_id)
                if not user:
                    return {"message": "User not found"}, 404
                return {"user_id": user.user_id, "url": user.url, "name": user.name}
            else:
                users = User.query.all()
                return [{"user_id": user.user_id, "url": user.url, "name": user.name} for user in users]
        except Exception as e:
            # Log the exception or handle it accordingly
            return {"message": f"Error in get_user: {str(e)}"}, 500

    @staticmethod
    def create_user(url, name):
        try:
            new_user = User(url=url, name=name)
            db.session.add(new_user)
            db.session.commit()
            return {"message": "User created successfully"}, 201
        except Exception as e:
            # Log the exception or handle it accordingly
            return {"message": f"Error in create_user: {str(e)}"}, 500

    @staticmethod
    def update_user(user_id, url=None, name=None):
        try:
            user = User.query.get(user_id)
            if user:
                if url:
                    user.url = url
                if name:
                    user.name = name
                db.session.commit()
                return {"message": "User updated successfully"}
            else:
                return {"message": "User not found"}, 404
        except Exception as e:
            # Log the exception or handle it accordingly
            return {"message": f"Error in update_user: {str(e)}"}, 500

    @staticmethod
    def delete_user(user_id):
        try:
            user = User.query.get(user_id)
            if user:
                db.session.delete(user)
                db.session.commit()
                return {"message": "User deleted successfully"}
            else:
                return {"message": "User not found"}, 404
        except Exception as e:
            # Log the exception or handle it accordingly
            return {"message": f"Error in delete_user: {str(e)}"}, 500
