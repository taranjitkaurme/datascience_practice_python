from flask_restful import Resource, reqparse
from src.services.usercompanymapping_service import UserCompanyMappingService

class UserCompanyMappingResource(Resource):
    def get(self, mapping_id=None):
        return UserCompanyMappingService.get_user_company_mapping(mapping_id)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=int, required=True, help='user_id is required')
        parser.add_argument('company_id', type=int, required=True, help='company_id is required')
        parser.add_argument('location_id', type=int, required=True, help='company_id is required')
        parser.add_argument('position_id', type=int)
        parser.add_argument('start_year', type=int)
        parser.add_argument('end_year', type=int)
        parser.add_argument('current_company', type=bool, default=False)

        args = parser.parse_args()

        return UserCompanyMappingService.create_user_company_mapping(
            user_id=args['user_id'],
            company_id=args['company_id'],
            position_id=args['position_id'],
            location_id=args['location_id'],
            start_year=args['start_year'],
            end_year=args['end_year'],
            current_company=args['current_company']
        )

    def put(self, mapping_id):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=int, required=True, help='user_id is required')
        parser.add_argument('company_id', type=int, required=True, help='company_id is required')
        parser.add_argument('position_id', type=int)
        parser.add_argument('location_id', type=int)
        parser.add_argument('start_year', type=int)
        parser.add_argument('end_year', type=int)
        parser.add_argument('current_company', type=bool, default=False)

        args = parser.parse_args()

        return UserCompanyMappingService.update_user_company_mapping(
            mapping_id=mapping_id,
            user_id=args['user_id'],
            company_id=args['company_id'],
            position_id=args['position_id'],
            location_id=args['location_id'],
            start_year=args['start_year'],
            end_year=args['end_year'],
            current_company=args['current_company']
        )

    def delete(self, mapping_id):
        return UserCompanyMappingService.delete_user_company_mapping(mapping_id)
