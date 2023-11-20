from flask import Flask
from flask_restful import Api
from src.resources.user_resource import UserResource
from src.resources.location_resource import LocationResource
from src.models.user import User
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
api.add_resource(LocationResource, '/api/locations', '/api/locations/<int:location_id>')

if __name__ == "__main__":
    app.run(debug=True)
