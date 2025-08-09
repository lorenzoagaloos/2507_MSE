#Week 2 Activity 5 - Create a project that works with strings (lorenzoagaloos-270729354)

#Tasks
# Get user input to enter a sentence.
# Check if the sentence is empty.
# If it is empty, display a message to the user.
# Create a class that would count the number of words in the sentence
# Display the result to the user.

# This code defines a class `wordCounter` that counts the number of words in a user-provided sentence.
class wordCounter:

    def __init__(self, text): # Initialize the class with the text
        self.text = text

    def count_words(self): # Count the number of words in the text
        words = self.text.split() # Split the text into words
    
def main():
    user_input = input("\nPlease write a sentence: ") # Get user input for a sentence
    
    if not user_input.strip():
        print("\nThe sentence is empty. Please re-run the code and enter a valid sentence.\n") # Check if the input is empty
        return
    
    word_counter = wordCounter(user_input) # Create an instance of the wordCounter class
    words = word_counter.text.split() # # Split the input sentence into words
    word_count = len(words) # Count the number of words in the sentence
    
    print(f"\nThe number of words in the sentence is: {word_count}\n")

if __name__ == "__main__":
    main()
    
  
