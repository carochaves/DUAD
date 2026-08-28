import unittest

from models import FinanceManager

class TestFinanceManager(unittest.TestCase):

    def test_add_category(self):
        manager = FinanceManager()
        category = manager.add_category("Test Category")
        self.assertIn(category, manager.get_categories())

    def test_add_empty_category(self):
            manager = FinanceManager()
            with self.assertRaises(ValueError):
                manager.add_category("")

    def test_add_duplicate_category(self):
        manager = FinanceManager()
        manager.add_category("Test Category")
        with self.assertRaises(ValueError):
            manager.add_category("Test Category")

    def test_add_duplicate_category_case_insensitive(self):
        manager = FinanceManager()
        manager.add_category("Test Category")
        with self.assertRaises(ValueError):
            manager.add_category("test category")

    def test_add_movement(self):
        manager = FinanceManager()
        manager.add_category("Test Category")
        movement = manager.add_movement("Test Movement", 100, "Test Category", "income")
        self.assertIn(movement, manager.get_movements())

    def test_add_movement_with_nonexistent_category(self):
        manager = FinanceManager()
        with self.assertRaises(ValueError):
            manager.add_movement("Test Movement", 100, "Nonexistent Category", "income")

    def test_add_movement_with_invalid_amount(self):
        manager = FinanceManager()
        manager.add_category("Test Category")
        with self.assertRaises(TypeError):
            manager.add_movement("Test Movement", "invalid_amount", "Test Category", "income")

    def test_add_movement_with_negative_amount(self):
        manager = FinanceManager()
        manager.add_category("Test Category")
        with self.assertRaises(ValueError):
            manager.add_movement("Test Movement", -100, "Test Category", "income")

if __name__ == "__main__":
    unittest.main()
