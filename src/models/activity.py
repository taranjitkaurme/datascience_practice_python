# activity.py

class Activity:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def log_activity(self, data):
        # Placeholder method for activity logging
        activity_log = f"Logged {self.name} for {data.get('duration_minutes', 0)} minutes."
        return activity_log

    # Other methods as needed
