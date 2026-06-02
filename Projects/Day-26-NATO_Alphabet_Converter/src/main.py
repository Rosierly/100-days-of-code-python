import pandas as pd

# Load NATO phonetic alphabet data from CSV
nato_data = pd.read_csv("./nato_phonetic_alphabet.csv")

# Convert DataFrame into a dictionary: letter → code
nato_alphabet = {row.letter: row.code for index, row in nato_data.iterrows()}


def get_word():
    """Get a valid alphabetic word from the user and return it in uppercase."""
    while True:
        user_input = input("Enter a word: ").strip().upper()
        if user_input.isalpha():
            return user_input
        print("Invalid input. Please use only letters.")


# Get valid user input
word = get_word()

# Convert each letter into NATO phonetic code
output = [nato_alphabet.get(letter) for letter in word]
print(output)

