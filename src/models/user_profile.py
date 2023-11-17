# user_profile.py

class UserProfile:
    def __init__(self, age, weight, height, fitness_goals, dietary_restrictions):
        self.age = age
        self.weight = weight
        self.height = height
        self.fitness_goals = fitness_goals
        self.dietary_restrictions = dietary_restrictions

    def to_dict(self):
        return {
            'age': self.age,
            'weight': self.weight,
            'height': self.height,
            'fitness_goals': self.fitness_goals,
            'dietary_restrictions': self.dietary_restrictions
        }

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
