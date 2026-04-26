from art import logo, vs
from game_data import data
import random
import os
import sys

DEBUG = False


def clear_screen() -> None:
    """Clear the console screen."""
    if sys.stdout.isatty():  # If running in a real terminal
        os.system('cls' if os.name == 'nt' else 'clear')
    else:  # Fallback for PyCharm console
        print("\n" * 40)


def get_entry(exclude=None) -> dict:
    """Return a random entry, excluding a specific one if provided."""
    while True:
        entry = random.choice(data)
        if entry != exclude:
            return entry


def format_entry(entry: dict) -> str:
    """Format an entry for display."""
    return f"{entry['name']}, a {entry['description']}, from {entry['country']}."


def display_round(entry_a: dict, entry_b: dict, current_score: int) -> None:
    """Display the current comparison between two entries."""
    clear_screen()
    print(logo)

    if current_score:
        print(f"You're right! Current score: {current_score}.")

    print(
          f"Compare A: {format_entry(entry_a)}\n"
          f"{vs}\n"
          f"Against B: {format_entry(entry_b)}"
    )


def get_answer() -> str:
    """Prompt the user until a valid choice ('a' or 'b') is entered and return it."""
    while True:
        user_input = input("\nWho has more followers? Type 'A' or 'B': ").strip().lower()
        if user_input in ("a", "b"):
            return user_input
        print("Invalid input. Please try again.")


def is_correct(user_answer: str, entry_a: dict, entry_b: dict) -> bool:
    """Return True if the user's answer matches the entry with more followers."""
    followers_a = entry_a["follower_count"]
    followers_b = entry_b["follower_count"]
    winner = "a" if followers_a > followers_b else "b"
    return winner == user_answer


def game() -> None:
    """Main game function for the Higher Lower Game."""
    account_a = get_entry()
    score = 0

    while True:
        account_b = get_entry(exclude=account_a)  # Select a new entry different from the current one
        display_round(account_a, account_b, score)

        if DEBUG:
            print(f"\n[DEBUG] A: {account_a['follower_count']} | B: {account_b['follower_count']}")

        answer = get_answer()

        # End the game if the guess is incorrect
        if not is_correct(answer, account_a, account_b):
            clear_screen()
            print(f"{logo}Sorry, that's wrong. Final score: {score}.")
            break

        # Correct guess: update score and carry forward the winning entry
        score += 1
        if answer == "b":
            account_a = account_b


game()
