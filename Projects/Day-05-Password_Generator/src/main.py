import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def get_user_input(item: str) -> int:
    """Prompt user for a number of a given item and return it as an integer."""
    while True:
        user_input = input(f"How many {item} would you like in your password? ").strip()
        if user_input.isdigit():
            return int(user_input)
        print("Invalid input. Please try again.\n")


def get_characters(item_amount: int, required_list: list[str]) -> list[str]:
    """Return a list of random characters of length `item_amount` from `required_list`."""
    result = []
    for _ in range(item_amount):
        result.append(random.choice(required_list))
    return result


def generate_password():
    print("Welcome to the PyPassword Generator!\n")

    # Get user input for each character type
    letter_amount = get_user_input("letters")
    symbol_amount = get_user_input("symbols")
    number_amount = get_user_input("numbers")

    # Build password list
    password_list = []
    for amount, char_list in [(letter_amount, letters), (symbol_amount, symbols), (number_amount, numbers)]:
        password_list += get_characters(amount, char_list)

    # Shuffle the characters to randomize order
    random.shuffle(password_list)

    # Convert list of characters into a string password
    password = "".join(password_list)
    # Alternative method: convert `list`-> `str` using a loop (less efficient)
    alt_password = ""
    for char in password_list:
        alt_password += char

    print(f"\n{password}")


generate_password()
