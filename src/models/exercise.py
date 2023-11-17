from models.activity import Activity

class Exercise(Activity):
    def __init__(self, name, duration_minutes):
        super().__init__(name, calories=0)  # Exercise calories are not specified in Exercise class
        self.duration_minutes = duration_minutes

    def log_activity(self):
        # Override log_activity method in Exercise class
        activity_log = f"Logged {self.name} for {self.duration_minutes} minutes."
        return activity_log

    # Other methods as needed
