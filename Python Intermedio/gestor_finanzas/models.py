class Category:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"Category('{self.name}')"


class Movement:
    def __init__(self, title, amount, category, type):
        self.title = title
        self.amount = amount
        self.category = category
        self.type = type


class FinanceManager:
    def __init__(self):
        self.movements = []
        self.categories = []

    def category_exists(self, name):
        for category in self.categories:
            if category.name.strip().lower() == name.strip().lower():
                return True
        return False

    def add_category(self, name):
        name = name.strip()

        if not name:
            raise ValueError("Category name cannot be empty.")

        if self.category_exists(name):
            raise ValueError(f"Category '{name}' already exists.")

        new_category = Category(name)
        self.categories.append(new_category)
        return new_category

    def add_movement(self, title, amount, category, type):
        title = title.strip()

        if not title:
            raise ValueError("Movement title cannot be empty.")

        if not isinstance(amount, (int, float)):
            raise TypeError("Movement amount must be a number.")

        if amount <= 0:
            raise ValueError("Movement amount must be a positive number.")
        
        category = category.strip()
        if not category:
            raise ValueError("Movement category cannot be empty.")

        if not self.category_exists(category):
            raise ValueError(f"Category '{category}' does not exist.")

        type = type.strip().lower()

        if type not in ["income", "expense"]:
            raise ValueError("Movement type must be either 'income' or 'expense'.")

        new_movement = Movement(title, amount, category, type)
        self.movements.append(new_movement)

        return new_movement

    def get_movements(self):
        return self.movements

    def get_categories(self):
        return self.categories

    def get_balance(self):
        balance = 0

        for movement in self.movements:
            if movement.type == "income":
                balance += movement.amount
            elif movement.type == "expense":
                balance -= movement.amount

        return balance

    def calculate_income(self):
        income = 0

        for movement in self.movements:
            if movement.type == "income":
                income += movement.amount

        return income

    def calculate_expenses(self):
        expenses = 0

        for movement in self.movements:
            if movement.type == "expense":
                expenses += movement.amount

        return expenses