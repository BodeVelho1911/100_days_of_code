import art
import random as rd

# Global constants
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 6

# Functions
def difficulty_level():
    """Function that asks the user which level of difficulty it wants
     and return the number of guesses the user have"""
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_LEVEL_ATTEMPTS
    elif difficulty == "hard":
        return HARD_LEVEL_ATTEMPTS
    else:
        return 0

def play_game():
    """Run this to start the number guessing game, it returns if the user wants to play again or not"""
    # Welcome message
    print(art.logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

    # Initialization
    chosen_num = rd.randint(1, 100)
    attempts_left = difficulty_level()
    guessed_right = False
    while not guessed_right and attempts_left > 0:
        print(f"You have {attempts_left} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > chosen_num:
            print("Too high!")
            attempts_left -= 1
        elif guess < chosen_num:
            print("Too low!")
            attempts_left -= 1
        else:
            print("You guessed right!! Congrats 😁")
            guessed_right = True
    if attempts_left == 0:
        print("You have ran out of attempts! 😭")

play_game()
