#Week 2 Activity 1 - Word Guessing Game (lorenzoagaloos-270729354)

#Tasks
# Create a program that randomly selects a five letter word.
# The user has to guess the word by entering letters one at a time.
# The program will inform the user if the letter is in the word and display it in the correct blank space.
# If the letter is not in the word, it will inform the user as well.
# The game continues until the user guesses the word or runs out of attempts.
# The user is only given 10 attempts to guess the word.
# the program should also handle invalid inputs
# The program should be able to run multiple times without restarting.
# To end the game, the user can type 'exit'
# Use local functions in the script

import random
import string

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
            print("\nThanks for playing! Goodbye!\n")
            break
if __name__ == "__main__":
    main()

# Week 2 Activity 1 - Word Guessing Game (lorenzoagaloos-270729354)