from src.models.usercompanymapping import UserCompanyMapping
from src.database.database import db
class UserCompanyMappingService:
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
