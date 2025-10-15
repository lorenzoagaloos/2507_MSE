""" Unit tests for basic math operations. """
from unittest import TestCase, main
from doctest import testmod

def add(x, y):
    """ Add two numbers. """
    return x + y

def multiply(x, y):
    """ Multiply two numbers. """
    return x * y

def subtract(x, y):
    """ Subtract two numbers. """
    return x - y

def divide(x, y):
    """ Divide two numbers. """
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def remainder(x, y):
    """ Get the remainder of division. """
    return x % y


class TestMathOperations(TestCase):
    """ Test cases for math operations. """
    def test_add(self):
        """ Test addition. """
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
    def test_multiply(self):
        """ Test multiplication. """
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
    def test_subtract(self):
        """ Test subtraction. """
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 1), -1)
    def test_divide(self):
        """ Test division. """
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(5, 2), 2.5)
        with self.assertRaises(ValueError):
            divide(1, 0)
    def test_remainder(self):
        """ Test remainder. """
        self.assertEqual(remainder(5, 2), 1)
        self.assertEqual(remainder(4, 2), 0)

class DoctestMathOperations:
    """ Doctest for math operations. """
    def add(self, a, b):
        """ Add two numbers.

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
        return add(a, b)

    def multiply(self, a, b):
        """ Multiply two numbers.

        >>> multiply(2, 3)
        6
        >>> multiply(-1, 1)
        -1
        >>> multiply(0, 100)
        0
        >>> multiply(-2, -3)
        6
        """
        return multiply(a, b)

    def subtract(self, a, b):
        """ Subtract two numbers.

        >>> subtract(5, 3)
        2
        >>> subtract(0, 1)
        -1
        >>> subtract(-1, -1)
        0
        >>> subtract(2.5, 1.5)
        1.0
        """
        return subtract(a, b)

    def divide(self, a, b):
        """ Divide two numbers.

        >>> divide(6, 3)
        2.0
        >>> divide(5, 2)
        2.5
        >>> divide(-6, -3)
        2.0
        >>> divide(1, 0)
        Traceback (most recent call last):
            ...
        ValueError: Cannot divide by zero
        """
        return divide(a, b)

    def remainder(self, a, b):
        """ Get the remainder of division.

        >>> remainder(5, 2)
        1
        >>> remainder(4, 2)
        0
        >>> remainder(10, 3)
        1
        >>> remainder(-5, 2)
        1
        """
        return remainder(a, b)

if __name__ == '__main__':
    main() # Unittest main
    testmod() # Doctest main
