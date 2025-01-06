import art
from game_data import data
import random as rd

# Choose 2 persons in the list and associate both to A and B
def choose_person():
    """Randomly choose a person from the database
     and returns a dictionary containing its data"""
    person = rd.choice(data)
    return person

# Compare the input from the user to the followers values
def compare(a, b, answer):
    """Compare the guess from the user against the number of followers of person 'a' and person 'b'."""
    if a["follower_count"] > b["follower_count"]:
        return answer == "a"
    else:
        return answer == "b"

# Create a loop to continuously ask the user until it fails, then the game ends
score = 0
person_A = choose_person()
is_guess_right = True
print(art.logo)
while is_guess_right:
    # Print the initial screen
    person_B = choose_person()
    if person_A == person_B:
        person_B = choose_person()
    print(f"Compare A: {person_A["name"]}, a {person_A["description"]}, from {person_A["country"]}")
    print(art.vs)
    print(f"Against B: {person_B["name"]}, a {person_B["description"]}, from {person_B["country"]}")

    # Ask the user which one has more followers
    user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    is_guess_right = compare(person_A, person_B, user_answer)
    print("\n" * 100)
    # If the user guessed right, add one to the score, then B becomes A and choose a new person to become B
    if is_guess_right:
        score += 1
        print(art.logo)
        print(f"You're right! Current score: {score}")
        person_A = person_B
    else:
        print(art.logo)
        print(f"Sorry, you're wrong 😭. Final score: {score}")

