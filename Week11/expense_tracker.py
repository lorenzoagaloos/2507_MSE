"""
Develop a program using OOP to create a simple Personal Expense Tracker.
The system should allow user input to add a new expense with a description and an amount. 
Then compute and display the total amount of all recorder expenses.
"""
import unittest

def add(a, b):
    """Add two numbers."""
    return a + b

class ExpenseTracker:
    """Class to track personal expenses."""
    def __init__(self):
        self.expenses = []

    def add_description(self, description):
        """Add a description for the expense."""
        self.expenses.append(description)

    def add_expense(self, amount):
        """Add an expense amount."""
        if amount > 0:
            self.expenses.append(amount)

    def total_expenses(self):
        """Calculate total expenses."""
        return sum(amount for amount in self.expenses if isinstance(amount, (int, float)))

class TestMathOperations(unittest.TestCase):
    """Unit test class for math operations."""
    def test_add(self):
        """Test the add function with various cases."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(1.5, 2.5), 4.0)
        self.assertEqual(add(-1.5, 1.5), 0.0)
    def test_total_expenses(self):
        """Unit test for total_expenses method."""
        tracker = ExpenseTracker()
        tracker.add_expense(50)
        tracker.add_expense(100)
        self.assertEqual(tracker.total_expenses(), 150)
        tracker.add_expense(-20)  # Invalid expense, should not affect total
        self.assertEqual(tracker.total_expenses(), 150)
        tracker.add_expense(0)  # Zero expense, should not affect total
        self.assertEqual(tracker.total_expenses(), 150)
        tracker.add_expense(25.5)
        self.assertEqual(tracker.total_expenses(), 175.5)


if __name__ == "__main__":
    tracker = ExpenseTracker()
    """User input loop to add expenses."""
    while True:
        description = input("Enter expense description (or 'q' to quit): ")
        if description.lower() == 'q':
            break
        try:
            amount = float(input("Enter expense amount: "))
            if amount <= 0:
                print("Amount must be positive. Try again.")
                continue
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue
        tracker.add_description(description)
        tracker.add_expense(amount)
        print(f"Added: {description} - ${amount:.2f}")
    print("\nAll recorded expenses:")
    for item in tracker.expenses:
        if isinstance(item, str):
            print(f"Description: {item}")
        else:
            print(f"Amount: ${item:.2f}")
    print(f"Total expenses: ${tracker.total_expenses():.2f}")

    unittest.main()
