# TODO: Create a letter using starting_letter.txt for each name in invited_names.txt
#  Replace the [name] placeholder with the actual name.
#  Save the letters in the folder "ReadyToSend".

# Hints:
# - readlines(): https://www.w3schools.com/python/ref_file_readlines.asp
# - replace(): https://www.w3schools.com/python/ref_string_replace.asp
# - strip(): https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as template_file:
    template = template_file.read()

for name in names:
    recipient_name = name.strip()  # strip() method removes `\n` automatically

    personalized_letter = template.replace("[name]", recipient_name)

    with open(f"./Output/ReadyToSend/letter_for_{recipient_name}.txt",mode="w") as letter_to_send:
        letter_to_send.write(personalized_letter)
