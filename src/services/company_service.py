from src.models.company import Company
from src.database.database import db
class CompanyService:

    """
    Service class for managing company-related operations.

    Methods:
        get_company(company_id=None):
            Retrieves information about a specific company or a list of all companies.

        create_company(name):
            Creates a new company with the provided name.

        update_company(company_id, name):
            Updates information about a specific company.

        delete_company(company_id):
            Deletes a specific company.

    Parameters:
        company_id (int, optional): The unique identifier of the company (for get, update, and delete operations).
        name (str): The name of the company (for create and update operations).

    Returns:
        dict: A dictionary containing the result of the corresponding operation.

    Example Usage:
        company_service = CompanyService()
        company_info = company_service.get_company(company_id=1)
        new_company_result = company_service.create_company(name="New Company")
        update_company_result = company_service.update_company(company_id=1, name="Updated Company")
        delete_company_result = company_service.delete_company(company_id=1)

    """

    @staticmethod
    def get_company(company_id=None):
        if company_id:
            company = Company.query.get(company_id)
            if not company:
                return {"message": "Company not found"}, 404
            return {"company_id": company.company_id, "name": company.name}
        else:
            companies = Company.query.all()
            return [{"company_id": company.company_id, "name": company.name} for company in companies]

    @staticmethod
    def create_company(name):
        new_company = Company(name=name)
        db.session.add(new_company)
        db.session.commit()
        return {"message": "Company created successfully"}, 201

    @staticmethod
    def update_company(company_id, name):
        company = Company.query.get(company_id)
        if company:
            company.name = name
            db.session.commit()
            return {"message": "Company updated successfully"}
        else:
            return {"message": "Company not found"}, 404

    @staticmethod
    def delete_company(company_id):
        company = Company.query.get(company_id)
        if company:
            db.session.delete(company)
            db.session.commit()
            return {"message": "Company deleted successfully"}
        else:
            return {"message": "Company not found"}, 404
