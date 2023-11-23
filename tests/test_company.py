# tests/test_company.py
"""
Company Test Module

This module defines the CompanyTestCase class, which contains test cases for the Company resource.

"""

from tests.test_base import BaseTestCase
from src.models.company import Company
from src.database.database import db

class CompanyTestCase(BaseTestCase):
    """
    Company Test Case Class

    This class inherits from the BaseTestCase and contains test cases for the Company resource.

    """

    def test_create_company(self):
        """
        Test Creating a Company

        Ensure that a new company can be created and is stored in the test database.

        """
        response = self.client.post('/api/companies', json={'name': 'Test Company'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Company.query.count(), 1)
        company = Company.query.first()
        self.assertEqual(company.name, 'Test Company')

    def test_get_company(self):
        """
        Test Getting a Company

        Ensure that an existing company can be retrieved from the test database.

        """
        company = Company(name='Existing Company')
        db.session.add(company)
        db.session.commit()

        response = self.client.get(f'/api/companies/{company.company_id}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['name'], 'Existing Company')

    def test_update_company(self):
        """
        Test Updating a Company

        Ensure that an existing company's name can be updated in the test database.

        """
        company = Company(name='Old Company Name')
        db.session.add(company)
        db.session.commit()

        response = self.client.put(f'/api/companies/{company.company_id}', json={'name': 'New Company Name'})
        self.assertEqual(response.status_code, 200)
        updated_company = Company.query.get(company.company_id)
        self.assertEqual(updated_company.name, 'New Company Name')

    def test_delete_company(self):
        """
        Test Deleting a Company

        Ensure that an existing company can be deleted from the test database.

        """
        company = Company(name='Company to Delete')
        db.session.add(company)
        db.session.commit()

        response = self.client.delete(f'/api/companies/{company.company_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Company.query.count(), 0)

if __name__ == '__main__':
    unittest.main()
