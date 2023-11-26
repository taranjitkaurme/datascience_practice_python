from flask import Flask
from flask_restful import Api
from src.resources.user_resource import UserResource
from src.resources.location_resource import LocationResource
from src.resources.company_resource import CompanyResource
from src.resources.usercompanymapping_resource import UserCompanyMappingResource
from src.resources.position_resource import PositionResource
from src.database.database import db


app = Flask(__name__)
api = Api(app)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:\Users\Neurabytes-taranjit\IdeaProjects\datascience_practice_python\data\data.db' # Change this based on your database type and configuration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database setup
db.init_app(app)

# Create the tables (this creates all tables defined in your models)
with app.app_context():
    db.create_all()

# API resources
api.add_resource(UserResource, '/api/users', '/api/users/<int:user_id>')
api.add_resource(LocationResource, '/api/location', '/api/location/<int:location_id>')
api.add_resource(CompanyResource, '/api/company', '/api/company/<int:company_id>')
api.add_resource(PositionResource, '/api/position', '/api/position/<int:position_id>')
api.add_resource(UserCompanyMappingResource, '/api/usercompanymapping', '/api/usercompanymapping/<int:mapping_id>')


if __name__ == "__main__":
    app.run(debug=True)
