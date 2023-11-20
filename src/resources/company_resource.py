from flask_restful import Resource, reqparse
from src.services.company_service import CompanyService

class CompanyResource(Resource):
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
