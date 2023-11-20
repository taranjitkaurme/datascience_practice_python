from src.models.company import Company
from src.database.database import db
class CompanyService:
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
