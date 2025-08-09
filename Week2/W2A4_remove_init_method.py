#Week 2 Activity 4 - Update the activity 3 code by removing the _init method (lorenzoagaloos-270729354)

#Tasks
# update the code from activity 3 by removing the __init__ method
# Use a class variable to store the string.
# The three methods should still perform the same tasks as before.

class stringManipulator:

    def find_character(self, char):
        return self.text.find(char)
    
    def get_length(self):
        return len(self.text)
    
    def to_uppercase(self):
        return self.text.upper()
    
def main():
    stringManipulator.text = "software engineering"  # Class variable to store the string
    word = stringManipulator()

    # Method 1: Find the character 'r'
    char_index = word.find_character('r')
    print(f"Character 'r' found at index: {char_index}")  # Output: 8

    # Method 2: Get the length of the word
    length = word.get_length()
    print(f"Length of the word: {length}")  # Output: 14

    # Method 3: Convert to uppercase
    upper_text = word.to_uppercase()
    print(f"Uppercase version: {upper_text}")  # Output: YOOBEE COLLEGE

if __name__ == "__main__":
    main()
    
  
