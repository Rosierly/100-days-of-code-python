from art import rock, paper, scissors
import random

choices = [rock, paper, scissors]


def check_input(prompt_text: str, valid_answers: list) -> int:
    """Prompts the user until a valid input is received, then returns it as an integer."""
    while True:
        user_input = input(prompt_text).strip()
        if user_input in valid_answers:
            return int(user_input)
        print("Invalid Input.\n")


def determine_winner(player_choice: int, computer_choice: int) -> str:
    """Determines and returns the result of the game."""
    if ((player_choice == 0 and computer_choice == 2) or
            (player_choice == 1 and computer_choice == 0) or
            (player_choice == 2 and computer_choice == 1)):
        return "You win."
    elif player_choice == computer_choice:
        return "It's a draw."
    else:
        return "You lost."


def game():
    """Main game loop."""
    # User's choice
    player_index = check_input("\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ",
                               ["0", "1", "2"])
    print(choices[player_index])

    # Computer's choice
    computer_index = random.randint(0, len(choices) - 1)
    print(f"Computer chose:\n{choices[computer_index]}")

    # Winner
    result = determine_winner(player_index, computer_index)
    print(result)

    # Play again
    keep_playing = input("Do you want to play again? Type 'Y' for yes or 'N' for no: ").upper()
    if keep_playing == "Y":
        game()  # recursion
    else:
        print("\nGoodbye!")


game()
