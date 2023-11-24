import pytest
from src.services.usercompanymapping_service import UserCompanyMappingService
from src.database.database import db

@pytest.fixture
def user_company_mapping_service():
    return UserCompanyMappingService()

def test_get_user_company_mapping(user_company_mapping_service):
    # Test retrieving a specific user company mapping
    result = user_company_mapping_service.get_user_company_mapping(mapping_id=1)
    assert result["message"] == "UserCompanyMapping not found"

    # Test retrieving all user company mappings
    all_mappings = user_company_mapping_service.get_user_company_mapping()
    assert isinstance(all_mappings, list)

def test_create_user_company_mapping(user_company_mapping_service):
    # Test creating a new user company mapping
    result = user_company_mapping_service.create_user_company_mapping(
        user_id=1,
        company_id=1,
        position_id=1,
        location_id=1,
        start_year=2022,
        end_year=2023,
        current_company=True
    )
    assert result["message"] == "UserCompanyMapping created successfully"

def test_update_user_company_mapping(user_company_mapping_service):
    # Test updating an existing user company mapping
    result = user_company_mapping_service.update_user_company_mapping(
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

def test_delete_user_company_mapping(user_company_mapping_service):
    # Test deleting an existing user company mapping
    result = user_company_mapping_service.delete_user_company_mapping(mapping_id=1)
    assert result["message"] == "UserCompanyMapping deleted successfully"

    # Test deleting a non-existent user company mapping
    result = user_company_mapping_service.delete_user_company_mapping(mapping_id=999)
    assert result["message"] == "UserCompanyMapping not found"
