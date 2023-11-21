from src.models.user import User
from src.database.database import db


class UserService:

    """
    Service class for managing user-related operations.

    Methods:
        get_user(user_id):
            Retrieves information about a specific user or a list of all users.

        create_user(url_link, name):
            Creates a new user with the provided URL link and name.

        update_user(user_id, url_link=None, name=None):
            Updates information about a specific user, including the URL link and/or name.

        delete_user(user_id):
            Deletes a specific user.

    Parameters:
        user_id (int): The unique identifier of the user (for get, update, and delete operations).
        url_link (str): The URL link associated with the user (for create and update operations).
        name (str): The name of the user (for create and update operations).

    Returns:
        str: A string containing the result of the corresponding operation.

    Example Usage:
        user_service = UserService()
        user_info = user_service.get_user(user_id=1)
        new_user_result = user_service.create_user(url_link="user123", name="John Doe")
        update_user_result = user_service.update_user(user_id=1, name="Updated Name")
        delete_user_result = user_service.delete_user(user_id=1)

    """

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


