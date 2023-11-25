from src.services.usercompanymapping_service import UserCompanyMappingService

def test_get_user_company_mapping(app):
    # Test retrieving a specific user company mapping
    with app.app_context():
        result = UserCompanyMappingService.get_user_company_mapping(mapping_id=1)
        assert result["message"] == "UserCompanyMapping not found"

        # Test retrieving all user company mappings
        all_mappings = UserCompanyMappingService.get_user_company_mapping()
        assert isinstance(all_mappings, list)

def test_create_user_company_mapping(app):
    # Test creating a new user company mapping
    with app.app_context():
        result = UserCompanyMappingService.create_user_company_mapping(
            user_id=1,
            company_id=1,
            position_id=1,
            location_id=1,
            start_year=2022,
            end_year=2023,
            current_company=True
        )
        assert result["message"] == "UserCompanyMapping created successfully"

def test_update_user_company_mapping(app):
    # Test updating an existing user company mapping
    with app.app_context():
        result = UserCompanyMappingService.update_user_company_mapping(
            mapping_id=1,
            user_id=1,
            company_id=1,
            position_id=1,
            location_id=1,
            start_year=2022,
            end_year=2023,
            current_company=False
        )
        assert result["message"] == "UserCompanyMapping updated successfully"

def test_delete_user_company_mapping(app):
    with app.app_context():
        # Test deleting an existing user company mapping
        result = UserCompanyMappingService.delete_user_company_mapping(mapping_id=1)
        assert result["message"] == "UserCompanyMapping deleted successfully"

        # Test deleting a non-existent user company mapping
        result = UserCompanyMappingService.delete_user_company_mapping(mapping_id=999)
        assert result["message"] == "UserCompanyMapping not found"
