#Week 2 Activity 1 - Word Guessing Game (lorenzoagaloos-270729354)

#Tasks
# Create a program that randomly selects a five letter word.
# The user has to guess the word by entering letters one at a time.
# The program will inform the user if the letter is in the word and its position.
# If the letter is not in the word, it will inform the user as well.
# The game continues until the user guesses the word or runs out of attempts.
# The user is only given 10 attempts to guess the word.
# the program should also handle invalid inputs gracefully.
# The program should be able to run multiple times without restarting.
# To end the game, the user can type 'exit'
# Use local functions in the script

import random
def get_random_word():
    words = ["apple", "grape", "peach", "berry", "melon"]
    return random.choice(words)

def get_user_input():
    while True:
        user_input = input("Enter a letter (or type 'exit' to quit): ").strip().lower()
        if user_input == 'exit':
            return None
        elif len(user_input) == 1 and user_input.isalpha():
            return user_input
        else:
            print("Invalid input. Please enter a single letter.")
def play_game():
    word = get_random_word()
    attempts = 10
    guessed_letters = set()
    
    print("Welcome to the Yoobee College Word Guessing Game!")
    print("Try to guess a five-letter word for fruits. You have 10 attempts.")
    
    while attempts > 0:
        print(f"\nAttempts remaining: {attempts}")
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
        
        user_input = get_user_input()
        if user_input is None:
            print("Thanks for playing!")
            return
        
        if user_input in guessed_letters:
            print(f"You already guessed '{user_input}'. Try a different letter.")
            continue
        
        guessed_letters.add(user_input)
        
        if user_input in word:
            positions = [i for i, letter in enumerate(word) if letter == user_input]
            print(f"Good job! '{user_input}' is in the word at positions: {', '.join(map(str, positions))}.")
        else:
            print(f"Sorry, '{user_input}' is not in the word.")
        
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word: {word}")
            return
        
        attempts -= 1
    
    print(f"Game over! The word was: {word}")
def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break
if __name__ == "__main__":
    main()

# Week 2 Activity 1 - Word Guessing Game (lorenzoagaloos-270729354)

