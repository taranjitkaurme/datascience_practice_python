from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from src.models.location import Location, db
from src.models.user import User, db


#from src.models.company import Company, UserCompanyMapping, Position, Location,

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()


# API endpoint for retrieving a location
@app.route('/api/location/<int:location_id>', methods=['GET'])
def get_location(location_id):
    get_location = Location.query.get(location_id)
    if get_location:
        location_data = {
            'location_id': get_location.location_id,
            'city': get_location.city,
            'state': get_location.state,
            'country': get_location.country,
            # Add other location-related fields as needed
        }
        return jsonify(location_data)
    else:
        return jsonify({'message': 'Location not found'})

# API endpoint for creating a location
@app.route('/api/location', methods=['POST'])
def create_location():
    data = request.get_json()
    new_location = Location(**data)
    db.session.add(new_location)
    db.session.commit()
    return jsonify({'message': 'Location created successfully'})

# API endpoint for updating a location
@app.route('/api/location/<int:location_id>', methods=['PUT'])
def update_location(location_id):
    data = request.get_json()
    location = Location.query.get(location_id)
    if location:
        for key, value in data.items():
            setattr(location, key, value)
        db.session.commit()
        return jsonify({'message': 'Location updated successfully'})
    else:
        return jsonify({'message': 'Location not found'})

# API endpoint for deleting a location
@app.route('/api/location/<int:location_id>', methods=['DELETE'])
def delete_location(location_id):
    location = Location.query.get(location_id)
    if location:
        db.session.delete(location)
        db.session.commit()
        return jsonify({'message': 'Location deleted successfully'})
    else:
        return jsonify({'message': 'Location not found'})


# API endpoint for retrieving a user profile

@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user_profile(user_id):
    get_user = User.query.get(user_id)
    if get_user:
        user_data = {
            'user_id': get_user.user_id,
            'url_link': get_user.url_link,
            'name': get_user.name,
            #'location_id': get_user.location_id,
            # Add other user-related fields as needed
        }
        return jsonify(user_data)
    else:
        return jsonify({'message': 'User not found'})

# API endpoint for creating a user profile


@app.route('/api/user', methods=['POST'])
def create_user_profile():
    data = request.get_json()
    new_user = User(**data)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'})

# API endpoint for updating a user profile


@app.route('/api/user/<int:user_id>', methods=['PUT'])
def update_user_profile(user_id):
    data = request.get_json()
    user = User.query.get(user_id)
    if user:
        for key, value in data.items():
            setattr(user, key, value)
        db.session.commit()
        return jsonify({'message': 'User profile updated successfully'})
    else:
        return jsonify({'message': 'User not found'})

# API endpoint for deleting a user profile


@app.route('/api/user/<int:user_id>', methods=['DELETE'])
def delete_user_profile(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'})
    else:
        return jsonify({'message': 'User not found'})

# Similar API endpoints for Company, UserCompanyMapping, Position, and Location CRUD operations...


if __name__ == '__main__':
    app.run(debug=True)
