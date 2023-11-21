from src.models.position import Position
from src.database.database import db

class PositionService:

    """
    Service class for managing position-related operations.

    Methods:
        get_position(position_id):
            Retrieves information about a specific position or a list of all positions.

        create_position(title):
            Creates a new position with the provided title.

        update_position(position_id, title):
            Updates information about a specific position.

        delete_position(position_id):
            Deletes a specific position.

    Parameters:
        position_id (int): The unique identifier of the position (for get, update, and delete operations).
        title (str): The title of the position (for create and update operations).

    Returns:
        dict: A dictionary containing the result of the corresponding operation.

    Example Usage:
        position_service = PositionService()
        position_info = position_service.get_position(position_id=1)
        new_position_result = position_service.create_position(title="New Position")
        update_position_result = position_service.update_position(position_id=1, title="Updated Position")
        delete_position_result = position_service.delete_position(position_id=1)

    """

    @staticmethod
    def get_position(position_id):
        if position_id:
            position = Position.query.get(position_id)
            if not position:
                return {"message": "Position not found"}, 404
            return {
                "position_id": position.position_id,
                "title": position.title
            }
        else:
            positions = Position.query.all()
            return [{
                "position_id": position.position_id,
                "title": position.title
            } for position in positions]

    @staticmethod
    def create_position(title):
        new_position = Position(title=title)
        db.session.add(new_position)
        db.session.commit()
        return {"message": "Position created successfully"}, 201

    @staticmethod
    def update_position(position_id, title):
        position = Position.query.get(position_id)
        if position:
            position.title = title
            db.session.commit()
            return {"message": "Position updated successfully"}
        else:
            return {"message": "Position not found"}, 404

    @staticmethod
    def delete_position(position_id):
        position = Position.query.get(position_id)
        if position:
            db.session.delete(position)
            db.session.commit()
            return {"message": "Position deleted successfully"}
        else:
            return {"message": "Position not found"}, 404
