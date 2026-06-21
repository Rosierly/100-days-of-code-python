import tkinter as tk
from tkinter import PhotoImage
import pandas
import random
import os

# ---------------------------- CONSTANTS & VARIABLES ------------------------------- #
DEBUG = True
DEFAULT_FILE = "../data/test.csv" if DEBUG else "../data/french_words.csv"
NEW_DATA_FILE = "../data/words_to_learn.csv"
BACKGROUND_COLOR = "#B1DDC6"
FONT = "Ariel"

current_card = {}
flip_timer = None

# ---------------------------- READ CSV DATA ------------------------------- #
# Try loading saved progress first, otherwise load the default word list
try:
    data = pandas.read_csv(NEW_DATA_FILE)
    if data.empty:
        raise ValueError("Empty file")  # force fallback

except (FileNotFoundError, ValueError):
    data = pandas.read_csv(DEFAULT_FILE)

words_to_learn = data.to_dict(orient="records")


# ---------------------------- FUNCTIONS ------------------------------- #
def flip_card():
    """Show the translation side of the current flashcard."""
    language_back, word_back = list(current_card.items())[1]

    canvas.itemconfig(card_title, text=language_back, fill="white")
    canvas.itemconfig(card_word, text=word_back, fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def next_card():
    """Display a new random flashcard and start the flip timer."""
    global current_card, flip_timer

    # Cancel the previous timer ONLY if it exists
    if flip_timer is not None:
        window.after_cancel(flip_timer)

    # Select a random word pair
    current_card = random.choice(words_to_learn)
    language_forth, word_forth = list(current_card.items())[0]

    # Show the front side of the card
    canvas.itemconfig(card_title, text=language_forth, fill="black")
    canvas.itemconfig(card_word, text=word_forth, fill="black")
    canvas.itemconfig(card_background, image=card_front_img)

    # Flip card after 3 seconds
    flip_timer = window.after(3000, func=flip_card)


def remove_card():
    """Remove the current card from the learning list."""
    global words_to_learn

    # Remove the known word
    if current_card in words_to_learn:
        words_to_learn.remove(current_card)

    # Handle completion state
    if not words_to_learn:
        canvas.itemconfig(card_title, text="         All done!\nRestart to start over.")
        canvas.itemconfig(card_word, text="Congratulations!")

        # Disable buttons when all words are learned
        known_button.config(state="disabled")
        unknown_button.config(state="disabled")

        # Stop any pending card flip
        if flip_timer is not None:
            window.after_cancel(flip_timer)

        # Delete saved progress file
        if os.path.exists(NEW_DATA_FILE):
            os.remove(NEW_DATA_FILE)

        return

    next_card()


def save_and_exit():
    """Save remaining words and close the application."""
    if words_to_learn:
        new_data = pandas.DataFrame(words_to_learn)
        new_data.to_csv("../data/words_to_learn.csv", index=False)
    window.destroy()


# ---------------------------- UI SETUP ------------------------------- #
# Window Setup
window = tk.Tk()
window.title("Flash Card App")
window.config(padx=50, pady=40, bg=BACKGROUND_COLOR)

# Images
card_back_img = PhotoImage(file="../assets/card_back.png")
card_front_img = PhotoImage(file="../assets/card_front.png")
check_img = PhotoImage(file="../assets/right.png")
cross_img = PhotoImage(file="../assets/wrong.png")

# Get Image Dimensions
card_width = card_back_img.width()
card_height = card_back_img.height()

# Canvas
canvas = tk.Canvas(width=card_width, height=card_height, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(card_width//2, card_height//2, image=card_front_img)
card_title = canvas.create_text(card_width//2, card_height//2 - 125, text="Press any button to start...", font=(FONT, 40, "italic"))
card_word = canvas.create_text(card_width//2, card_height//2, text="Hello!", font=(FONT, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2, pady=(10, 5))

# Buttons
known_button = tk.Button(
    image=check_img,
    bg=BACKGROUND_COLOR,
    activebackground=BACKGROUND_COLOR,
    highlightthickness=0,
    bd=0,
    command=remove_card
)
known_button.grid(row=1, column=0, pady=5)

unknown_button = tk.Button(
    image=cross_img,
    bg=BACKGROUND_COLOR,
    activebackground=BACKGROUND_COLOR,
    highlightthickness=0,
    bd=0,
    command=next_card
)
unknown_button.grid(row=1, column=1, pady=5)

# Save progress when the window is closed
window.protocol("WM_DELETE_WINDOW", save_and_exit)

window.mainloop()
