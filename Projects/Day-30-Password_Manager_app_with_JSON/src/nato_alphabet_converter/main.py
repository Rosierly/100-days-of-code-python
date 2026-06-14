import pandas as pd

# Load NATO phonetic alphabet data from CSV
nato_data = pd.read_csv("./nato_phonetic_alphabet.csv")

# Convert DataFrame into a dictionary: letter → code
nato_alphabet = {row.letter: row.code for index, row in nato_data.iterrows()}


# TODO: Validate input so only alphabetic characters are accepted using exception handling.
def convert():
    """Convert a user-input word into NATO phonetic alphabet codes."""
    while True:
        user_input = input("Enter a word: ").strip().upper()

        try:
            output = [nato_alphabet[character] for character in user_input]
        except KeyError:
            print("Sorry, only letters in the alphabet please.\n")
        else:
            return output


result = convert()
print(result)

