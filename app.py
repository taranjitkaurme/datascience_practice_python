from flask import Flask, jsonify, request
from src.models.user_profile import UserProfile,db
from src.models.food_item import FoodItem
from src.models.exercise import Exercise
from src.models.meal import Meal

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diet_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

# API endpoint for retrieving a user profile
@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user_profile(user_id):
    get_profile = UserProfile.query.get(user_id)
    if get_profile:
        return jsonify(get_profile.to_dict())
    else:
        return jsonify({'message': 'User profile not found'})


# API endpoint for creating a user profile
@app.route('/api/user', methods=['POST'])
def create_user_profile():
    data = request.get_json()
    new_user_profile = UserProfile(**data)
    db.session.add(new_user_profile)
    db.session.commit()
    return jsonify({'message': 'User profile created successfully'})


# API endpoint for updating a user profile
@app.route('/api/user/<int:user_id>', methods=['PUT'])
def update_user_profile(user_id):
    data = request.get_json()
    user_profile = UserProfile.query.get(user_id)
    if user_profile:
        for key, value in data.items():
            setattr(user_profile, key, value)
        db.session.commit()
        return jsonify({'message': 'User profile updated successfully'})
    else:
        return jsonify({'message': 'User profile not found'})


# API endpoint for deleting a user profile
@app.route('/api/user/<int:user_id>', methods=['DELETE'])
def delete_user_profile(user_id):
    user_profile = UserProfile.query.get(user_id)
    if user_profile:
        db.session.delete(user_profile)
        db.session.commit()
        return jsonify({'message': 'User profile deleted successfully'})
    else:
        return jsonify({'message': 'User profile not found'})


# Similar API endpoints for FoodItem, Exercise, and Meal CRUD operations...

if __name__ == '__main__':
    app.run(debug=True)
