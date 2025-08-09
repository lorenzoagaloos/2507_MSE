#Week 2 Activity 2 - Incorporate the use of at least one class into the Word Guessing Game (lorenzoagaloos-270729354)

#Tasks
# Incorporate the use of at least one class into the Word Guessing Game.
# Use the dateformatter class to format and display the date and time when the game starts and ends.

import random
import string
from datetime import datetime

class DateFormatter:
    def __init__(self, current_time=None):
        self.current_time = datetime.now()

    def format_time(self, fmt="%A, %d-%B-%Y %H:%M:%S"):
        return self.current_time.strftime(fmt)


# Function to get a random five-letter word from a predefined list
def get_random_word():
    words = ["apple", "grape", "peach", "berry", "melon", "mango", "lemon", "guava"]
    return random.choice(words)

# Function to get user input and validate it
def get_user_input():
    while True:
        user_input = input("Enter a letter (or type 'exit' to quit): ").strip().lower()
        if user_input == 'exit':
            return None
        elif len(user_input) == 1 and user_input.isalpha():
            return user_input
        else:
            print("Invalid input. Please enter a single letter.")

# Function to play the word guessing game
def play_game():
    secret = get_random_word() # Get a random five-letter word
    attempts = 10
    guessed_letters = set() # Set to keep track of guessed letters

    # Create an instance of DateFormatter to format the start time
    df = DateFormatter()
    print("\nGame started at:", df.format_time(fmt="%A, %d-%B-%Y %I:%M:%p"))


    print("\nWelcome to the Yoobee College Word Guessing Game!")
    print("Try to guess a FIVE-LETTER word for a FRUIT. You have 10 attempts.")

    # Local function to display the current progress of the guessed word
    def display_progress():
            display = ""
            for letter in secret:
                display += letter + " " if letter in guessed_letters else "_ " # Show guessed letters or underscores
            print("\nWord:", display.strip()) 
    
    while attempts > 0:
        print(f"\nAttempts remaining: {attempts}")
        display_progress() 
        print("\nGuessed letters:", " ".join(sorted(guessed_letters))) #
        
        user_input = get_user_input()
        if user_input is None:
            print("Thanks for playing!")
            return
        
        if user_input in guessed_letters:
            print(f"You already guessed '{user_input}'. Try a different letter.")
            continue
        
        guessed_letters.add(user_input) 
        
        if user_input in secret:
            print(f"\nGood job! '{user_input}' is in the word.")

        else:
            print(f"\nSorry, '{user_input}' is not in the word.")
        
        if all(letter in guessed_letters for letter in secret):
            display_progress()
            print(f"\nCONGRATULATIONS! You've guessed the word: {secret}")
            return
        
        attempts -= 1
    
    print(f"\nGame over! You have no more attempts left. The word was: {secret}")

# Main function to run the game loop
def main():
    while True:
        play_game()
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("\nThanks for playing! Goodbye!")

            # Create an instance of DateFormatter to format the end time
            df = DateFormatter()
            print("\nGame ended at:", df.format_time(fmt="%A, %d-%B-%Y %I:%M:%p\n"))

            break
if __name__ == "__main__":
    main()

# Week 2 Activity 1 - Word Guessing Game (lorenzoagaloos-270729354)