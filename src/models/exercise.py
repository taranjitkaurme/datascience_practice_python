from src.models.activity import Activity

class Exercise(Activity):
    def __init__(self, exercise_id, name, duration_minutes):
        super().__init__(name, calories=0)  # Exercise calories are not specified in Exercise class
        self.exercise_id=exercise_id
        self.duration_minutes = duration_minutes

    def log_activity(self):
        # Override log_activity method in Exercise class
        activity_log = f"Logged {self.name} for {self.duration_minutes} minutes."
        return activity_log

    # CRUD operations for Exercise
    exercises = []  # In-memory storage, replace with a database in a real-world application

    @classmethod
    def create(cls, exercise):
        cls.exercises.append(exercise)

    @classmethod
    def read(cls, exercise_id):
        return next((item for item in cls.exercises if item.exercise_id == exercise_id), None)

    @classmethod
    def update(cls, exercise_id, new_data):
        item = cls.read(exercise_id)
        if item:
            for key, value in new_data.items():
                setattr(item, key, value)

    @classmethod
    def delete(cls, exercise_id):
        cls.exercises = [item for item in cls.exercises if item.exercise_id != exercise_id]
