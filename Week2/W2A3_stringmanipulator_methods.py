#Week 2 Activity 3 - Write a code incorporating the use of three methods (lorenzoagaloos-270729354)

#Tasks
# Write a project to look for a character in an string, get the length of the string, and convert the string to uppercase.
# Create a class with three methods to perform these tasks.
# Method 1 - find the character from a specified word
# Method 2 - get the lenght of the word
# Method 3 - convert lower to upper case

class stringManipulator:

    def __init__(self, text):
        self.text = text

    def find_character(self, char):
        return self.text.find(char)
    
    def get_length(self):
        return len(self.text)
    
    def to_uppercase(self):
        return self.text.upper()
    
def main():
    word = stringManipulator("yoobee college")

    # Method 1: Find the character 'c'
    char_index = word.find_character('c')
    print(f"Character 'c' found at index: {char_index}")  # Output: 8

    # Method 2: Get the length of the word
    length = word.get_length()
    print(f"Length of the word: {length}")  # Output: 14

    # Method 3: Convert to uppercase
    upper_text = word.to_uppercase()
    print(f"Uppercase version: {upper_text}")  # Output: YOOBEE COLLEGE
if __name__ == "__main__":
    main()

