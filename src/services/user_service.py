from src.models.user import User
from src.database.database import db


class UserService:

    @staticmethod
    def get_user(user_id):
        if user_id:
            user = User.query.get(user_id)
            if not user:
                return None
            return {"user_id": user.user_id, "url_link": user.url_link, "name": user.name}
        else:
            users = User.query.all()
            return [{"user_id": user.user_id, "url_link": user.url_link, "name": user.name} for user in users]

    @staticmethod
    def create_user(url_link, name):
        new_user = User(url_link=url_link, name=name)
        #new_user = User(url_link=args['url_link'], name=args['name'])
        db.session.add(new_user)
        db.session.commit()
        return "User created successfully"


    @staticmethod
    def update_user(user_id, url_link=None, name=None):
        user = User.query.get(user_id)
        if user:
            if url_link:
                user.url_link = url_link
            if name:
                user.name = name
            db.session.commit()
            return "User updated successfully"
        else:
            return None

    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return "User deleted successfully"
        else:
            return None


