# tests/test_position_service.py
"""
Test cases for PositionService.
"""

from src.models.position import Position
from src.services.position_service import PositionService
from src.database.database import db

def test_get_position(app):
    """
    Test the get_position method of PositionService.
    """
    # Add test data to the database
    with app.app_context():
        position = Position(title="Software Engineer")
        db.session.add(position)
        db.session.commit()

        # Call the get_position method
        result = PositionService.get_position(position.position_id)

        # Assert the result
        assert result == {"position_id": position.position_id, "title": position.title}

def test_create_position(app):
    """
    Test the create_position method of PositionService.
    """
    # Call the create_position method
    with app.app_context():
        result = PositionService.create_position(title="Data Scientist")

        # Assert the result
        assert result == {"message": "Position created successfully"}

def test_update_position(app):
    """
    Test the update_position method of PositionService.
    """
    # Add test data to the database
    with app.app_context():
        position = Position(title="Software Engineer")

        db.session.add(position)
        db.session.commit()

        # Call the update_position method
        result = PositionService.update_position(position_id=position.position_id, title="Senior Software Engineer")

        # Assert the result
        assert result == {"message": "Position updated successfully"}

def test_delete_position(app):
    """
    Test the delete_position method of PositionService.
    """
    with app.app_context():
        # Add test data to the database
        position = Position(title="Software Engineer")
        db.session.add(position)
        db.session.commit()

        # Call the delete_position method
        result = PositionService.delete_position(position.position_id)

        # Assert the result
        assert result == {"message": "Position deleted successfully"}
