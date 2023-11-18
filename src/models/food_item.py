# food_item.py

class FoodItem:
    def __init__(self, food_id, name, calories, carbs, protein, fats):
        self.food_id = food_id
        self.name = name
        self.calories = calories
        self.carbs = carbs
        self.protein = protein
        self.fats = fats

    def to_dict(self):
        return {
            'food_id': self.food_id,
            'name': self.name,
            'calories': self.calories,
            'carbs': self.carbs,
            'protein': self.protein,
            'fats': self.fats
        }

    # CRUD operations for FoodItem
    food_items = []  # In-memory storage, replace with a database in a real-world application

    @classmethod
    def create(cls, food_item):
        cls.food_items.append(food_item)

    @classmethod
    def read(cls, food_id):
        return next((item for item in cls.food_items if item.food_id == food_id), None)

    @classmethod
    def update(cls, food_id, new_data):
        item = cls.read(food_id)
        if item:
            for key, value in new_data.items():
                setattr(item, key, value)

    @classmethod
    def delete(cls, food_id):
        cls.food_items = [item for item in cls.food_items if item.food_id != food_id]