import json

from models import Category, Movement


def save_categories(manager):
    categories_data = []

    for category in manager.get_categories():
        category_data = {
            "name": category.name
        }

        categories_data.append(category_data)

    with open("data/categories.json", "w") as file:
        json.dump(categories_data, file, indent=4)


def load_categories(manager):
    try:
        with open("data/categories.json", "r") as file:
            categories_data = json.load(file)

        for category_data in categories_data:
            category = Category(category_data["name"])
            manager.categories.append(category)

    except FileNotFoundError:
        pass


def save_movements(manager):
    movements_data = []

    for movement in manager.get_movements():
        movement_data = {
            "title": movement.title,
            "amount": movement.amount,
            "category": movement.category,
            "type": movement.type
        }

        movements_data.append(movement_data)

    with open("data/movements.json", "w") as file:
        json.dump(movements_data, file, indent=4)


def load_movements(manager):
    try:
        with open("data/movements.json", "r") as file:
            movements_data = json.load(file)

        for movement_data in movements_data:
            movement = Movement(
                movement_data["title"],
                movement_data["amount"],
                movement_data["category"],
                movement_data["type"]
            )

            manager.movements.append(movement)

    except FileNotFoundError:
        pass