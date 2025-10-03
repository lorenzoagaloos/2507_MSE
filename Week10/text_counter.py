"""
This module provides functions for performing various mathematical operations,
including counting letters and upper cases.
"""

# This function counts the total length and uppercase characters in a string or list of strings.
class TextCounter:
    """Initialize with either a string or a list of strings"""
    def __init__(self, data):
        if isinstance(data, str):
            self.data = data
        elif isinstance(data, list):
            self.data = ''.join(data)
        else:
            raise ValueError("Input must be a string or a list of strings.")

    # Return the total length of the data
    def total_length(self):
        """Return the total length of the data"""
        return len(self.data)

    # Return the count of uppercase characters in the data
    def count_u_case(self):
        """Count and return the number of uppercase characters in the data"""
        return sum(1 for char in self.data if char.isupper())

# Example usage:
if __name__ == "__main__":
    # Test cases
    Words_1 = "The Quick Brown Fox!"
    Words_2 = ["Jumped", " ", "over", " ", "the", " ", "Lazy"," ", "DOG", "!"]

    # Create instances of TextCounter
    Count1 = TextCounter(Words_1)
    Count2 = TextCounter(Words_2)

    # Print results
    print(f"Text 1 Length: {Count1.total_length()}, Uppercase Count: {Count1.count_u_case()}")
    print(f"Text 2 Length: {Count2.total_length()}, Uppercase Count: {Count2.count_u_case()}")
