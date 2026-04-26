from art import logo
import random

MIN_NUMBER = 1
MAX_NUMBER = 100
ATTEMPTS_BY_DIFFICULTY = {
    "easy": 10,
    "hard": 5
}

DEBUG = False


def set_difficulty() -> int:
    """Return attempts based on chosen difficulty."""
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
        if difficulty in ATTEMPTS_BY_DIFFICULTY:
            return ATTEMPTS_BY_DIFFICULTY[difficulty]
        print("Invalid input. Please try again.")


def display_attempts(attempts_left: int):
    """Display the number of remaining attempts."""
    print(f"\nYou have {attempts_left} attempts remaining to guess the number.")


def get_valid_guess() -> int:
    """Return a valid guess within the allowed range."""
    while True:
        user_input = input("Make a guess: ").strip()
        if user_input.isdigit():
            user_guess = int(user_input)
            if MIN_NUMBER <= user_guess <= MAX_NUMBER:
                return user_guess
        print(f"Please enter a number between {MIN_NUMBER} and {MAX_NUMBER}.")


def game():
    """Run one round of the number guessing game."""
    print(f"{logo}\nWelcome to the Number Guessing Game!\n"
          f"I'm thinking of a number between {MIN_NUMBER} and {MAX_NUMBER}.")
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    attempts_remaining = set_difficulty()

    if DEBUG:
        print(f"\n[DEBUG] The number is {number}.")

    while attempts_remaining:  # while attempts_remaining != 0:
        display_attempts(attempts_remaining)
        guess = get_valid_guess()

        # Win condition - Early exit on correct guess
        if guess == number:
            print(f"\nYou got it! The answer was {number}.")
            return

        # Update remaining attempts after a wrong guess
        attempts_remaining -= 1

        # Give feedback only if the game continues
        if attempts_remaining:
            print("Too low." if guess < number else "Too high.")

    # Reached when all attempts are used
    print(f"\nYou've run out of guesses. The answer was {number}.")


game()
