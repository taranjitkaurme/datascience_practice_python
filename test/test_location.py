
import pytest
from src.services.location_service import LocationService

@pytest.fixture
def location_service():
    return LocationService()

def test_get_location(location_service):
    # Test get_location with existing location
    location_info = location_service.get_location(location_id=1)
    assert "location_id" in location_info
    assert "city" in location_info
    assert "state" in location_info
    assert "country" in location_info

    # Test get_location with non-existing location
    non_existing_location_info = location_service.get_location(location_id=100)
    assert "message" in non_existing_location_info
    assert non_existing_location_info["message"] == "Location not found"

def test_create_location(location_service):
    # Test create_location
    new_location_result = location_service.create_location(city="Test City", state="Test State", country="Test Country")
    assert "message" in new_location_result
    assert new_location_result["message"] == "Location created successfully"

def test_update_location(location_service):
    # Test update_location with existing location
    update_existing_result = location_service.update_location(location_id=1, city="Updated City", state="Updated State", country="Updated Country")
    assert "message" in update_existing_result
    assert update_existing_result["message"] == "Location updated successfully"

    # Test update_location with non-existing location
    update_non_existing_result = location_service.update_location(location_id=100, city="Updated City", state="Updated State", country="Updated Country")
    assert "message" in update_non_existing_result
    assert update_non_existing_result["message"] == "Location not found"

def test_delete_location(location_service):
    # Test delete_location with existing location
    delete_existing_result = location_service.delete_location(location_id=1)
    assert "message" in delete_existing_result
    assert delete_existing_result["message"] == "Location deleted successfully"

    # Test delete_location with non-existing location
    delete_non_existing_result = location_service.delete_location(location_id=100)
    assert "message" in delete_non_existing_result
    assert delete_non_existing_result["message"] == "Location not found"
