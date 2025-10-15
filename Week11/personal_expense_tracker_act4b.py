"""Create a simple personal expense tracker using OOP
which can add expenses and calculate total expenses.
Apply unit testing to ensure the correctness of the add and total methods"""
import unittest
import doctest

class ExpenseTracker:
    """Class to track personal expenses."""
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount):
        """Add an expense amount to the tracker."""
        if amount > 0:
            self.expenses.append(amount)
    def get_expenses(self):
        """Return the list of expenses."""
        return self.expenses

def add(a, b):
    """Add two numbers."""
    return a + b

def total_expenses(tracker):
    """Calculate total expenses from an ExpenseTracker instance."""
    return sum(tracker.expenses)

def test_add():
    """Test the add function with various cases."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-1, -1) == -2
    assert add(1.5, 2.5) == 4.0
    assert add(-1.5, 1.5) == 0.0

def test_total_expenses():
    """Test the total_expenses method of ExpenseTracker."""
    tracker = ExpenseTracker()
    tracker.add_expense(50)
    tracker.add_expense(100)
    assert total_expenses(tracker) == 150
    tracker.add_expense(-20)  # Invalid expense, should not affect total
    assert total_expenses(tracker) == 150
    tracker.add_expense(0)  # Zero expense, should not affect total
    assert total_expenses(tracker) == 150
    tracker.add_expense(25.5)
    assert total_expenses(tracker) == 175.5

class TestMathOperations(unittest.TestCase):
    """Unit test class for math operations."""
    def test_add(self):
        """Unit test for add function."""
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
        self.assertEqual(total_expenses(tracker), 150)
        tracker.add_expense(-20)  # Invalid expense, should not affect total
        self.assertEqual(total_expenses(tracker), 150)
        tracker.add_expense(0)  # Zero expense, should not affect total
        self.assertEqual(total_expenses(tracker), 150)
        tracker.add_expense(25.5)
        self.assertEqual(total_expenses(tracker), 175.5)

class DoctestMathOperations:
    """Doctest class for math operations."""
    def add(self, a, b):
        """Add two numbers.

        >>> add(2, 3)
        5
        >>> add(-1, 1)
        0
        >>> add(0, 0)
        0
        >>> add(-1, -1)
        -2
        >>> add(1.5, 2.5)
        4.0
        >>> add(-1.5, 1.5)
        0.0
        """
        return a + b
    def total_expenses(self, tracker):
        """Calculate total expenses from an ExpenseTracker instance.

        >>> tracker = ExpenseTracker()
        >>> tracker.add_expense(50)
        >>> tracker.add_expense(100)
        >>> total_expenses(tracker)
        150
        >>> tracker.add_expense(-20)  # Invalid expense, should not affect total
        >>> total_expenses(tracker)
        150
        >>> tracker.add_expense(0)  # Zero expense, should not affect total
        >>> total_expenses(tracker)
        150
        >>> tracker.add_expense(25.5)
        >>> total_expenses(tracker)
        175.5
        """
        return sum(tracker.expenses)

if __name__ == '__main__':
    test_add()
    test_total_expenses()
    unittest.main() # Run unit tests
    doctest.testmod() # Run doctests
