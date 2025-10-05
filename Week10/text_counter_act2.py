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

# Function to count digits and special characters
def count_digits_and_specials(data):
    """Count and return the number of digits and special characters in the data"""
    if isinstance(data, str):
        text = data
    elif isinstance(data, list):
        text = ''.join(data)
    else:
        raise ValueError("Input must be a string or a list of strings.")

    digit_count = sum(1 for char in text if char.isdigit())
    special_count = sum(1 for char in text if not char.isalnum() and not char.isspace())

    return digit_count, special_count


# Example usage:
if __name__ == "__main__":
    # Test cases
    WORDS1 = "The Quick Brown Fox @ the *!#) r1v3r!"
    WORDS2 = ["Jumped", " ", "over", " ", "the", " ", "Lazy"," ", "1020"," ","DOG", "!"]

    # Create instances of TextCounter
    Count1 = TextCounter(WORDS1)
    Count2 = TextCounter(WORDS2)

    # Print results
    print(f"Text 1 Length: {Count1.total_length()}, Uppercase Count: {Count1.count_u_case()}")
    print(f"Text 2 Length: {Count2.total_length()}, Uppercase Count: {Count2.count_u_case()}")

    # Count digits and special characters
    digits1, specials1 = count_digits_and_specials(WORDS1)
    digits2, specials2 = count_digits_and_specials(WORDS2)
    print(f"Text 1 Digits: {digits1}, Special Characters: {specials1}")
    print(f"Text 2 Digits: {digits2}, Special Characters: {specials2}")
