from src.services.user_service import UserService


def test_create_user(app):
    """
        Test the create_user method of UserService.
        """
    # Test creating a new user
    with app.app_context():
        result = UserService.create_user(url='new_url', name='New User')

        # Assertions
        assert result[0]["message"] == "User created successfully"


def test_get_user(app):
    """
    Test the get_user method of UserService.
    """
    with app.app_context():
        # Test getting a user by user_id
        result = UserService.get_user(1)

        # Assertions
        assert result == {"user_id": 1, "url": 'new_url', "name": 'New User'}


def test_update_user(app):
    """
        Test the update_user method of UserService.
        """
    with app.app_context():
        # Test updating a user
        result = UserService.update_user(1, url='updated_url', name='Updated User')
        print(result)
        # Assertions
        assert result["message"] == "User updated successfully"


def test_delete_user(app):
    """
        Test the delete_user method of UserService.
        """

    with app.app_context():
        # Test deleting a user
        result = UserService.delete_user(1)

        # Assertions
        assert result["message"] == "User deleted successfully"
