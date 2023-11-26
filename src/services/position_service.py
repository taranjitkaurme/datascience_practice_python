from src.models.position import Position
from src.database.database import db


class PositionService:

    @staticmethod
    def get_position(position_id):
        try:
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
        except Exception as e:
            # Log the exception or handle it accordingly
            return {"message": f"Error in get_position: {str(e)}"}, 500

    @staticmethod
    def create_position(title):
        try:
            new_position = Position(title=title)
            db.session.add(new_position)
            db.session.commit()
            return {"message": "Position created successfully"}, 201
        except Exception as e:
            # Log the exception or handle it accordingly
            return {"message": f"Error in create_position: {str(e)}"}, 500

    @staticmethod
    def update_position(position_id, title):
        try:
            position = Position.query.get(position_id)
            if position:
                position.title = title
                db.session.commit()
                return {"message": "Position updated successfully"}
            else:
                return {"message": "Position not found"}, 404
        except Exception as e:
            # Log the exception or handle it accordingly
            return {"message": f"Error in update_position: {str(e)}"}, 500

    @staticmethod
    def delete_position(position_id):
        try:
            position = Position.query.get(position_id)
            if position:
                db.session.delete(position)
                db.session.commit()
                return {"message": "Position deleted successfully"}
            else:
                return {"message": "Position not found"}, 404
        except Exception as e:
            # Log the exception or handle it accordingly
            return {"message": f"Error in delete_position: {str(e)}"}, 500
