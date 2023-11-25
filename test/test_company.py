from src.services.company_service import CompanyService

def test_create_company(app):
    # Test create_company
    with app.app_context():
        new_company_result = CompanyService.create_company(name="Test Company")
        print(new_company_result)
        assert "message" in new_company_result[0]
        assert new_company_result[0]["message"] == "Company created successfully"

def test_get_company(app):  # Pass the session fixture
    with app.app_context():
        # Test get_company with existing company
        company_info = CompanyService.get_company(company_id=1)
        print(company_info)
        assert "company_id" in company_info
        assert "name" in company_info

        # Test get_company with non-existing company
        non_existing_company_info = CompanyService.get_company(company_id=100)
        assert "message" in non_existing_company_info[0]
        assert non_existing_company_info[0]["message"] == "Company not found"

def test_update_company(app):
    # Test update_company with existing company
    with app.app_context():
        update_existing_result = CompanyService.update_company(company_id=1, name="Updated Company Name")
        assert "message" in update_existing_result
        assert update_existing_result["message"] == "Company updated successfully"

        # Test update_company with non-existing company
        update_non_existing_result = CompanyService.update_company(company_id=100, name="Updated Company Name")
        assert "message" in update_non_existing_result[0]
        assert update_non_existing_result[0]["message"] == "Company not found"


def test_delete_company(app):
    # Test delete_company with existing company
    with app.app_context():
        delete_existing_result = CompanyService.delete_company(company_id=1)
        assert "message" in delete_existing_result
        assert delete_existing_result["message"] == "Company deleted successfully"

        # Test delete_company with non-existing company
        delete_non_existing_result = CompanyService.delete_company(company_id=100)
        assert "message" in delete_non_existing_result[0]
        assert delete_non_existing_result[0]["message"] == "Company not found"
