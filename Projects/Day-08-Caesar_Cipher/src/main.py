from art import logo
import string

alphabet = list(string.ascii_lowercase)


def get_valid_inputs() -> tuple[str, str, int]:
    """Prompt the user for a valid direction, message, and shift value, and return them."""
    error_message = "That's not a valid input. Please try again.\n"

    # Get direction input (encode or decode)
    while True:
        direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").strip().lower()
        if direction in ["encode", "decode"]:
            break
        print(error_message)

    # Get message to transform
    text = input("Type your message:\n")

    # Get shift number
    while True:
        shift_value = input("Type the shift number:\n").strip()
        if shift_value.isdigit():
            break
        print(error_message)

    return direction, text, int(shift_value)


def transform_text(direction: str, text: str, shift_value: int) -> str:
    """Return the text encoded or decoded using the given shift value."""
    transformed_text = ""

    # Reverse the shift_value for decoding
    if direction == "decode":
        shift_value *= -1

    # Shift each character in the message
    for char in text:
        if char in alphabet:
            original_index = alphabet.index(char)
            shifted_index = (original_index + shift_value) % len(alphabet)  # Limit shift_index to alphabet size
            shifted_char = alphabet[shifted_index]
            transformed_text += shifted_char
        else:
            transformed_text += char  # Leave characters that aren't in the alphabet unchanged

    return transformed_text


def caesar_cipher():
    """Run the Caesar cipher program."""
    while True:
        cipher_direction, message, shift_amount = get_valid_inputs()
        output = transform_text(cipher_direction, message, shift_amount)
        print(f"Here's the {cipher_direction}d result: {output}")

        # Ask the user if they want to run the program again
        run_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").strip().lower()
        if run_again not in ("yes", "y"):
            print("Goodbye!")
            break


print(logo)
caesar_cipher()
