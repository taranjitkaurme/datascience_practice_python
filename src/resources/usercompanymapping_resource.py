from flask_restful import Resource, reqparse
from src.services.usercompanymapping_service import UserCompanyMappingService
from src.utility.decorators import log_request
class UserCompanyMappingResource(Resource):

    """
Represents the RESTful API resource for managing user-company mapping information.

Endpoints:
    GET /api/user_company_mapping/<int:mapping_id>:
        Retrieves information about a specific user-company mapping.
    POST /api/user_company_mapping:
        Creates a new user-company mapping.
    PUT /api/user_company_mapping/<int:mapping_id>:
        Updates information about a specific user-company mapping.
    DELETE /api/user_company_mapping/<int:mapping_id>:
        Deletes a specific user-company mapping.

Methods:
    get(self, mapping_id=None):
        Retrieves information about a specific user-company mapping or a list of all mappings.

    post(self):
        Creates a new user-company mapping based on the provided information.

    put(self, mapping_id):
        Updates information about a specific user-company mapping.

    delete(self, mapping_id):
        Deletes a specific user-company mapping.

Request Parameters:
    mapping_id (int, optional): The unique identifier of the user-company mapping (for GET, PUT, and DELETE operations).

Request JSON Payload (for POST and PUT operations):
    {
        "user_id": 1,
        "company_id": 1,
        "position_id": 1,
        "location_id": 1,
        "start_year": 2022,
        "end_year": 2023,
        "current_company": false
    }

Returns:
    dict: A JSON response containing the result of the corresponding operation.

"""
    @log_request
    def get(self, mapping_id=None):

        return UserCompanyMappingService.get_user_company_mapping(mapping_id)

    @log_request
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

    @log_request
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

    @log_request
    def delete(self, mapping_id):
        return UserCompanyMappingService.delete_user_company_mapping(mapping_id)
