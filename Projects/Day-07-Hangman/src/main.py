import random
from art import logo, stages
from words import words_dictionary

DEBUG = False


def get_difficulty_level() -> str:
    """Prompt the user for a difficulty level and return a valid option. """
    while True:
        user_input = input('\nChoose one level of difficulty.\nType "Easy", "Normal" or "Hard": ').strip().lower()
        try:
            words_dictionary[user_input]
        except KeyError:
            print("That's not a valid input. Please try again.")
        else:
            return user_input


def get_guess(guessed_letters: list[str]) -> str:
    """Prompt the user for a single valid alphabetical character and return it."""
    while True:
        user_input = input("\nGuess a letter: ").strip().lower()
        if not user_input.isalpha():
            print("Be careful. Only alphabetical letters are allowed.")
        elif len(user_input) > 1:
            print("Please enter one character at a time.")
        elif user_input in guessed_letters:
            print("You've already guessed that letter. Don't worry, you won't lose a life.")
        else:
            return user_input


def generate_slots(chosen_word: str) -> list[str]:
    """Generate a list of underscores representing each letter in the chosen word."""
    empty_slots = []
    for _ in chosen_word:
        empty_slots += "_"
    return empty_slots


def display_lives_left(lives: int):
    """Display the current hangman stage and remaining lives."""
    print(stages[lives])
    print(f"{'*' * 30} {lives}/{len(stages) - 1} LIVES LEFT {'*' * 30}")


def display_word(letter_slots: list[str]):
    """Display the current state of the guessed word."""
    print(f"Word to guess: {' '.join(letter_slots)}\n")


def hangman():
    print(f"{logo}\nWelcome to the Hangman Game!\nGood luck!")

    difficulty = get_difficulty_level()
    remaining_lives = len(stages) - 1
    word = random.choice(words_dictionary[difficulty])
    revealed_letters = generate_slots(word)
    used_letters = []

    if DEBUG:
        print(f"\n[DEBUG] Word is: {word}")

    # Main game loop
    while True:

        # Get player's guess and check if it exists in the word
        guess = get_guess(used_letters)
        if guess not in word:
            print(f"\n'{guess}' is not in the word.")
            remaining_lives -= 1
        else:
            # Update correct positions using enumerate
            for index_num, letter in enumerate(word):
                if letter == guess:
                    revealed_letters[index_num] = guess
            # Alternative way using index (less efficient)
            for index_num in range(len(word)):
                if word[index_num] == guess:
                    revealed_letters[index_num] = guess
            # Store guessed letters to prevent repeated guesses
            used_letters.append(guess)

        # Display current game state
        display_word(revealed_letters)
        display_lives_left(remaining_lives)

        # Check if the game is over (win or lose)
        if remaining_lives == 0 or "_" not in revealed_letters:
            if remaining_lives == 0:
                message = "YOU LOSE!"
            else:
                message = "CONGRATULATIONS. YOU WIN!"
            print(f"\n{message} The word was: {word}")
            break


hangman()
