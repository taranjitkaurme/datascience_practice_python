import pytest
from src.models.user import User
from src.services.user_service import UserService
from src.database.database import db

class TestUserService:
    """
    Test cases for the UserService class.
    """

    @pytest.fixture
    def app(self):
        """
        Fixture to set up the Flask app for testing.
        """
        # Set up your Flask app configuration for testing
        # ...

    def test_get_user(self, app):
        """
        Test the get_user method of UserService.
        """
        # Set up test data
        test_user = User(user_id=1, url_link='test_url', name='Test User')
        db.session.add(test_user)
        db.session.commit()

        # Test getting a user by user_id
        result = UserService.get_user(1)

        # Assertions
        assert result == {"user_id": 1, "url_link": 'test_url', "name": 'Test User'}

    def test_create_user(self, app):
        """
        Test the create_user method of UserService.
        """
        # Test creating a new user
        result = UserService.create_user(url_link='new_url', name='New User')

        # Assertions
        assert result == "User created successfully"

    def test_update_user(self, app):
        """
        Test the update_user method of UserService.
        """
        # Set up test data
        test_user = User(user_id=1, url_link='test_url', name='Test User')
        db.session.add(test_user)
        db.session.commit()

        # Test updating a user
        result = UserService.update_user(1, url_link='updated_url', name='Updated User')

        # Assertions
        assert result == "User updated successfully"

    def test_delete_user(self, app):
        """
        Test the delete_user method of UserService.
        """
        # Set up test data
        test_user = User(user_id=1, url_link='test_url', name='Test User')
        db.session.add(test_user)
        db.session.commit()

        # Test deleting a user
        result = UserService.delete_user(1)

        # Assertions
        assert result == "User deleted successfully"
