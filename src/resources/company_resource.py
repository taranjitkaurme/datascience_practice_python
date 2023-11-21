from flask_restful import Resource, reqparse
from src.services.company_service import CompanyService

class CompanyResource(Resource):

    """
    Represents the RESTful API resource for managing company information.

    Endpoints:
        GET /api/company/<int:company_id>:
            Retrieves information about a specific company.
        POST /api/company:
            Creates a new company.
        PUT /api/company/<int:company_id>:
            Updates information about a specific company.
        DELETE /api/company/<int:company_id>:
            Deletes a specific company.

    Methods:
        get(self, company_id=None):
            Retrieves information about a specific company or a list of all companies.

        post(self):
            Creates a new company based on the provided information.

        put(self, company_id):
            Updates information about a specific company.

        delete(self, company_id):
            Deletes a specific company.

    Request Parameters:
        company_id (int, optional): The unique identifier of the company (for GET, PUT, and DELETE operations).

    Request JSON Payload (for POST and PUT operations):
        {
            "name": "Company Name"
        }

    Returns:
        dict: A JSON response containing the result of the corresponding operation.

    """

    def get(self, company_id=None):
        return CompanyService.get_company(company_id)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='name is required')
        args = parser.parse_args()
        return CompanyService.create_company(args['name'])

    def put(self, company_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='name is required')
        args = parser.parse_args()
        return CompanyService.update_company(company_id, args['name'])

    def delete(self, company_id):
        return CompanyService.delete_company(company_id)
