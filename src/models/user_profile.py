# user_profile.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserProfile(db.Model):
    __tablename__ = "user_profile"

    user_id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    weight = db.Column(db.Float)
    height = db.Column(db.Float)
    fitness_goals = db.Column(db.String(255))
    dietary_restrictions = db.Column(db.String(255))

    def __init__(self, user_id, age, weight, height, fitness_goals, dietary_restrictions):
        self.user_id = user_id
        self.age = age
        self.weight = weight
        self.height = height
        self.fitness_goals = fitness_goals
        self.dietary_restrictions = dietary_restrictions

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'age': self.age,
            'weight': self.weight,
            'height': self.height,
            'fitness_goals': self.fitness_goals,
            'dietary_restrictions': self.dietary_restrictions
        }

    # CRUD operations for UserProfile

    @classmethod
    def read(cls, user_id, user_profiles):
        print(user_profiles)
        return next((profile for profile in user_profiles if profile.user_id == user_id), None)

    @classmethod
    def create(cls, user_profile, user_profiles):
        user_profiles.append(user_profile)

    @classmethod
    def update(cls, user_id, new_data, user_profiles):
        profile = cls.read(user_id, user_profiles)
        if profile:
            for key, value in new_data.items():
                setattr(profile, key, value)

    @classmethod
    def delete(cls, user_id, user_profiles):
        user_profiles = [profile for profile in user_profiles if profile.user_id != user_id]

    def update_weight(self, new_weight):
        self.weight = new_weight

    def log_activity(self, activity_type, duration_minutes):
        # Placeholder method for activity logging
        activity_log = f"Logged {activity_type} for {duration_minutes} minutes."
        return activity_log

    def get_caloric_needs(self):
        # Placeholder method for calculating caloric needs based on user profile
        # You can implement a more sophisticated calculation based on user details
        caloric_needs = 2000  # Placeholder value
        return caloric_needs
