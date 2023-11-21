import unittest
from flask import Flask
from flask_testing import TestCase
from src.database.database import db
from src.models.company import Company
from src.services.company_service import CompanyService

class TestCompanyService(TestCase):
    """
    Test cases for the CompanyService class.
    """

    def create_app(self):
        """
        Create a Flask app for testing.
        """
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(app)
        with app.app_context():
            db.create_all()
        return app

    def setUp(self):
        """
        Set up test resources before each test.
        """
        self.company_service = CompanyService()

    def tearDown(self):
        """
        Clean up test resources after each test.
        """
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_company(self):
        """
        Test the get_company method of CompanyService.
        """
        # Test getting a company that exists
        company_id = 1
        Company(name="Test Company").save()
        result = self.company_service.get_company(company_id)
        self.assertEqual(result, {"company_id": company_id, "name": "Test Company"})

        # Test getting a non-existing company
        non_existing_company_id = 2
        result = self.company_service.get_company(non_existing_company_id)
        self.assertEqual(result, {"message": "Company not found"})

    def test_create_company(self):
        """
        Test the create_company method of CompanyService.
        """
        # Test creating a company
        name = "New Company"
        result = self.company_service.create_company(name)
        self.assertEqual(result, {"message": "Company created successfully"})

        # Test creating a company with an existing name
        Company(name="Existing Company").save()
        result = self.company_service.create_company("Existing Company")
        self.assertEqual(result, {"message": "Company with the same name already exists"})

    def test_update_company(self):
        """
        Test the update_company method of CompanyService.
        """
        # Test updating an existing company
        company_id = 1
        Company(name="Old Company").save()
        result = self.company_service.update_company(company_id, "New Company")
        self.assertEqual(result, {"message": "Company updated successfully"})

        # Test updating a non-existing company
        non_existing_company_id = 2
        result = self.company_service.update_company(non_existing_company_id, "New Company")
        self.assertEqual(result, {"message": "Company not found"})

    def test_delete_company(self):
        """
        Test the delete_company method of CompanyService.
        """
        # Test deleting an existing company
        company_id = 1
        Company(name="ToDelete Company").save()
        result = self.company_service.delete_company(company_id)
        self.assertEqual(result, {"message": "Company deleted successfully"})

        # Test deleting a non-existing company
        non_existing_company_id = 2
        result = self.company_service.delete_company(non_existing_company_id)
        self.assertEqual(result, {"message": "Company not found"})

if __name__ == '__main__':
    unittest.main()
