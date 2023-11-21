from src.models.usercompanymapping import UserCompanyMapping
from src.database.database import db
class UserCompanyMappingService:

    """
    Service class for managing user company mapping-related operations.

    Methods:
        get_user_company_mapping(mapping_id):
            Retrieves information about a specific user company mapping or a list of all mappings.

        create_user_company_mapping(user_id, company_id, position_id, location_id, start_year, end_year, current_company):
            Creates a new user company mapping with the provided details.

        update_user_company_mapping(mapping_id, user_id, company_id, position_id, location_id, start_year, end_year, current_company):
            Updates information about a specific user company mapping.

        delete_user_company_mapping(mapping_id):
            Deletes a specific user company mapping.

    Parameters:
        mapping_id (int): The unique identifier of the user company mapping (for get, update, and delete operations).
        user_id (int): The user's unique identifier (for create and update operations).
        company_id (int): The company's unique identifier (for create and update operations).
        position_id (int): The position's unique identifier (for create and update operations).
        location_id (int): The location's unique identifier (for create and update operations).
        start_year (int): The start year of the mapping (for create and update operations).
        end_year (int): The end year of the mapping (for create and update operations).
        current_company (bool): Indicates whether the company is the current one (for create and update operations).

    Returns:
        dict: A dictionary containing the result of the corresponding operation.

    Example Usage:
        mapping_service = UserCompanyMappingService()
        mapping_info = mapping_service.get_user_company_mapping(mapping_id=1)
        new_mapping_result = mapping_service.create_user_company_mapping(user_id=1, company_id=1, start_year=2022, current_company=True)
        update_mapping_result = mapping_service.update_user_company_mapping(mapping_id=1, end_year=2023)
        delete_mapping_result = mapping_service.delete_user_company_mapping(mapping_id=1)

    """

    @staticmethod
    def get_user_company_mapping(mapping_id=None):
        if mapping_id:
            mapping = UserCompanyMapping.query.get(mapping_id)
            if not mapping:
                return {"message": "UserCompanyMapping not found"}, 404
            return {
                "mapping_id": mapping.mapping_id,
                "user_id": mapping.user_id,
                "company_id": mapping.company_id,
                "position_id": mapping.position_id,
                "location_id": mapping.location_id,
                "start_year": mapping.start_year,
                "end_year": mapping.end_year,
                "current_company": mapping.current_company
            }
        else:
            mappings = UserCompanyMapping.query.all()
            return [{
                "mapping_id": mapping.mapping_id,
                "user_id": mapping.user_id,
                "company_id": mapping.company_id,
                "position_id": mapping.position_id,
                "location_id": mapping.location_id,
                "start_year": mapping.start_year,
                "end_year": mapping.end_year,
                "current_company": mapping.current_company
            } for mapping in mappings]

    @staticmethod
    def create_user_company_mapping(user_id, company_id, position_id, location_id, start_year, end_year, current_company):
        new_mapping = UserCompanyMapping(
            user_id=user_id,
            company_id=company_id,
            position_id=position_id,
            location_id=location_id,
            start_year=start_year,
            end_year=end_year,
            current_company=current_company
        )
        db.session.add(new_mapping)
        db.session.commit()
        return {"message": "UserCompanyMapping created successfully"}, 201

    @staticmethod
    def update_user_company_mapping(mapping_id, user_id, company_id, position_id, location_id, start_year, end_year, current_company):
        mapping = UserCompanyMapping.query.get(mapping_id)
        if mapping:
            mapping.user_id = user_id
            mapping.company_id = company_id
            mapping.position_id = position_id
            mapping.location_id = location_id
            mapping.start_year = start_year
            mapping.end_year = end_year
            mapping.current_company = current_company
            db.session.commit()
            return {"message": "UserCompanyMapping updated successfully"}
        else:
            return {"message": "UserCompanyMapping not found"}, 404

    @staticmethod
    def delete_user_company_mapping(mapping_id):
        mapping = UserCompanyMapping.query.get(mapping_id)
        if mapping:
            db.session.delete(mapping)
            db.session.commit()
            return {"message": "UserCompanyMapping deleted successfully"}
        else:
            return {"message": "UserCompanyMapping not found"}, 404
