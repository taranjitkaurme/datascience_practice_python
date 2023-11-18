from src.models.activity import Activity
from src.models.food_item import FoodItem


class Meal(Activity):
    def __init__(self, meal_id, name, calories, carbs, protein, fats):
        super().__init__(name, calories)
        self.meal_id = meal_id
        self.carbs = carbs
        self.protein = protein
        self.fats = fats


# CRUD operations for Meal

    meals = []  # In-memory storage, replace with a database in a real-world application

    @classmethod
    def create(cls, meal):
        cls.meals.append(meal)

    @classmethod
    def read(cls, meal_id):
        return next((item for item in cls.meals if item.meal_id == meal_id), None)

    @classmethod
    def update(cls, meal_id, new_data):
        item = cls.read(meal_id)
        if item:
            for key, value in new_data.items():
                setattr(item, key, value)

    @classmethod
    def delete(cls, meal_id):
        cls.meals = [item for item in cls.meals if item.meal_id != meal_id]

    def log_activity(self, food_item_data):
        # Placeholder method for meal logging
        food_item = FoodItem(**food_item_data)
        meal_log = f"Logged {self.name} with {food_item.name}."
        return meal_log

    # Other methods as needed
