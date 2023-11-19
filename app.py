from flask import Flask, jsonify, request
from src.models.user_profile import UserProfile
from src.models.food_item import FoodItem
from src.models.exercise import Exercise
from src.models.meal import Meal
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diet_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

# Sample data for initialization (replace with your own data or load from a database)
user_profile_data = {
    'user_id': 1,
    'age': 25,
    'weight': 70,
    'height': 175,
    'fitness_goals': 'Build muscle',
    'dietary_restrictions': ['Vegetarian']
}

food_item_data = {
    'food_id': 1,
    'name': 'Broccoli',
    'calories': 55,
    'carbs': 11,
    'protein': 3,
    'fats': 0.6
}

exercise_data = {
    'exercise_id': 1,
    'name': 'Running',
    'duration_minutes': 30
}

meal_data = {
    'meal_id': 1,
    'name': 'Salad',
    'calories': 200,
    'carbs': 15,
    'protein': 10,
    'fats': 12
}


# Initialize sample data
user_profiles = [UserProfile(**user_profile_data)]
food_items = [FoodItem(**food_item_data)]
exercises = [Exercise(**exercise_data)]
meals = [Meal(**meal_data)]


# API endpoint for retrieving a user profile
@app.route('/api/get_user_profile/<int:user_id>', methods=['GET'])
def get_user_profile(user_id):
    get_profile = UserProfile.read(user_id, user_profiles)
    if get_profile:
        return jsonify(get_profile.to_dict())  # Use to_dict method to jsonify the profile
    else:
        return jsonify({'message': 'User profile not found'})


# API endpoint for creating a user profile
@app.route('/api/create_user_profile', methods=['POST'])
def create_user_profile():
    data = request.get_json()
    new_user_profile = UserProfile(**data)
    UserProfile.create(user_profiles, new_user_profile)
    return jsonify({'message': 'User profile created successfully'})


# API endpoint for updating a user profile
@app.route('/api/update_user_profile/<int:user_id>', methods=['PUT'])
def update_user_profile(user_id):
    data = request.get_json()
    UserProfile.update(user_id, data, user_profiles)
    return jsonify({'message': 'User profile updated successfully'})


# API endpoint for deleting a user profile
@app.route('/api/delete_user_profile/<int:user_id>', methods=['DELETE'])
def delete_user_profile(user_id):
    UserProfile.delete(user_id, user_profiles)
    return jsonify({'message': 'User profile deleted successfully'})


# Similar API endpoints for FoodItem, Exercise, and Meal CRUD operations...

if __name__ == '__main__':
    app.run(debug=True)
