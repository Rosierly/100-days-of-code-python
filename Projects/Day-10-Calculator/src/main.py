from art import logo
import os
import sys


def reset_screen():
    """Clear the console screen and display the program logo."""
    if sys.stdout.isatty():  # If running in a real terminal
        os.system('cls' if os.name == 'nt' else 'clear')
    else:  # Fallback for PyCharm console
        print("\n" * 40)

    print(logo)


def get_number(prompt_text: str) -> float:
    """Get a valid number from the user and return it as a float."""
    while True:
        user_input = input(prompt_text)
        try:
            return float(user_input)
        except ValueError:
            print("That's not a valid number. Please try again.\n")


def get_operator(prompt_text: str, all_operations: dict) -> str:
    """Get a valid operator from the user and return it."""
    while True:
        operator = input(prompt_text)
        if operator in all_operations:
            return operator
        print("That's not a valid operator. Please try again.\n")


def addition(first_number: float, next_number: float) -> float:
    """Return the sum of two numbers."""
    return first_number + next_number


def subtraction(first_number: float, next_number: float) -> float:
    """Return the difference of two numbers."""
    return first_number - next_number


def multiplication(first_number: float, next_number: float) -> float:
    """Return the product of two numbers."""
    return first_number * next_number


def division(first_number: float, next_number: float) -> float | None:
    """Return the division of two numbers or None if invalid."""
    if next_number == 0:  # Handle division by zero
        print(f"\nCannot divide by zero. Your first number is {first_number}")
        return None
    return first_number / next_number


def calculator():
    """Run the calculator program."""
    operations = {
        "+": addition,
        "-": subtraction,
        "*": multiplication,
        "/": division
    }

    # Get the first number
    first_value = get_number("What's the first number?: ")

    while True:
        # Show available operations
        print("\n".join(operations.keys()))

        # Get operator and next number
        operator_symbol = get_operator("Pick an operation: ", operations)
        next_value = get_number("What's the next number?: ")

        # Perform calculation
        result = operations[operator_symbol](first_value, next_value)

        # Skip if invalid (from division by zero)
        if result is None:
            continue

        print(f"\n{first_value} {operator_symbol} {next_value} = {result}\n")

        while True:
            # Ask the user if they want to continue with this result or start fresh
            continue_calculation = input(f"\nType 'y' to continue calculating with {result} "
                                         f"or type 'n' to start a new calculation: ").strip().lower()
            if continue_calculation == "y":
                first_value = result  # Use previous result as first number
                break
            elif continue_calculation == "n":
                reset_screen()
                calculator()  # Restart the program
            else:
                print("That's not a valid input. Please try again.")


reset_screen()
calculator()
