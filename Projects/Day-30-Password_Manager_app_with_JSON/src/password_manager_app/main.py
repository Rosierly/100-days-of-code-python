import tkinter as tk
from tkinter import messagebox  # messagebox is a module for dialogs, not a class
import string
import random
import pyperclip  # clipboard support
import json

# ---------------------------- CONSTANTS ------------------------------- #
BG_COLOR = "#1B2A41"  # deep navy background

PRIMARY_COLOR = "#D4483B"  # save password button (logo color → red)
PRIMARY_HOVER = "#B63A30"  # hover color for save button

SECONDARY_COLOR = "#4A6480"  # generate button (close to bg → deep navy)
ENTRY_BG = "#2D4059"  # bg color for entry fields

TEXT_COLOR = "#F5F5F5"  # white

# Base font
BASE_FONT = ("Segoe UI", 11)

# Derived fonts
BOLD_FONT = (BASE_FONT[0], BASE_FONT[1], "bold")  # same family & size, bold
BUTTON_FONT = (BASE_FONT[0], BASE_FONT[1] - 1)  # slightly smaller for buttons


# ---------------------------- HIDE PASSWORD ------------------------------- #
def toggle_password():
    """Toggle visibility of password entry field."""
    if password_entry.cget("show") == "":
        password_entry.config(show="*")
        eye_button.config(text="Show")
    else:
        password_entry.config(show="")
        eye_button.config(text="Hide")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def get_characters(item_amount, required_list):
    """Return a list of random characters of a specified length."""
    return [random.choice(required_list) for _ in range(item_amount)]


def generate_password():
    """Generate a random password, display it in the entry, and copy it to the clipboard."""
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = list("!#$%&()*+")

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # Build password list
    password_list = []
    for amount, char_list in [(nr_letters, letters), (nr_symbols, symbols), (nr_numbers, numbers)]:
        password_list += get_characters(amount, char_list)

    # Shuffle and convert to string
    random.shuffle(password_list)
    password = "".join(password_list)

    # Display in entry and copy to clipboard
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Validate inputs, confirm save, and store password entry."""
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
                website: {
                    "email": email,
                    "password": password
                }
    }

    # Check for empty fields
    if not website or not email or not password:
        messagebox.showwarning(title="Error", message="Please don't leave any fields empty!")
        return

    # Mask password in confirmation if hidden
    display_password = password if password_entry.cget("show") != "*" else "*" * len(password)

    # Confirmation dialog
    is_ok = messagebox.askokcancel(
        title="Confirm Save",
        message=f"WEBSITE: {website}\nEMAIL: {email}\nPASSWORD: {display_password}\n\nDo you want to save this entry?"
    )

    # Save to file
    if is_ok:
        # Load existing JSON data if it exists, otherwise start with empty dictionary
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)  # read old data
        except FileNotFoundError:
            data = {}

        # Update data with new entries
        data.update(new_data)

        # Save updated data back to JSON file
        with open("data.json", mode="w") as data_file:
            json.dump(data, data_file, indent=4)  # save updated data

        messagebox.showinfo(title="Success", message="Your entry was saved successfully!")

        # Reset fields
        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        website_entry.focus()


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    """Retrieve saved login details for a website and copy the password to clipboard."""
    # Get website name entered by the user
    website = website_entry.get()

    # Load saved password data from JSON file
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No details found for this website.")
    else:
        if website in data:
            # Extract stored email and password
            website_data = data[website]
            email = website_data.get("email")
            password = website_data.get("password")

            # Copy password to clipboard
            pyperclip.copy(password)

            # Show credentials to the user
            messagebox.showinfo(
                title=website,
                message=f"Email: {email}\nPassword: {password}\n\n**Password copied to clipboard.**"
            )
        else:
            messagebox.showwarning(title="Error", message=f"No details found for this website.")


# ---------------------------- UI SETUP ------------------------------- #
# Window Setup
window = tk.Tk()
window.title("Password Manager")
window.config(padx=60, pady=60, bg=BG_COLOR)

# Image - Logo
logo_img = tk.PhotoImage(file="../../assets/logo.png")
img_width = logo_img.width()
img_height = logo_img.height()

# Canvas
canvas = tk.Canvas(width=img_width, height=img_height, bg=BG_COLOR, highlightthickness=0)
canvas.create_image(img_width // 2, img_height // 2, image=logo_img)
canvas.grid(row=0, column=0, columnspan=4, pady=10)

# Labels
website_label = tk.Label(text="Website:", bg=BG_COLOR, fg=TEXT_COLOR, font=BOLD_FONT)
website_label.grid(row=1, column=0, padx=10, pady=8, sticky="e")

email_label = tk.Label(text="Email/Username:", bg=BG_COLOR, fg=TEXT_COLOR, font=BOLD_FONT)
email_label.grid(row=2, column=0, padx=10, pady=8, sticky="e")

password_label = tk.Label(text="Password:", bg=BG_COLOR, fg=TEXT_COLOR, font=BOLD_FONT)
password_label.grid(row=3, column=0, padx=10, pady=8, sticky="e")

# Entries
website_entry = tk.Entry(width=35, bg=ENTRY_BG, fg="white", font=BASE_FONT, insertbackground="white", relief="flat")
website_entry.grid(row=1, column=1, sticky="EW")
website_entry.focus()

email_entry = tk.Entry(width=35, bg=ENTRY_BG, fg="white", font=BASE_FONT, insertbackground="white", relief="flat")
email_entry.grid(row=2, column=1, columnspan=3, sticky="EW")
email_entry.insert(0, "myemail@gmail.com")

password_entry = tk.Entry(
    width=26,
    bg=ENTRY_BG,
    fg="white",
    font=BASE_FONT,
    insertbackground="white",  # controls the color of the blinking text cursor (caret) inside an Entry widget
    relief="flat",
    show="*")  # hides the actual text you type in an Entry widget and replaces it with a symbol
password_entry.grid(row=3, column=1, sticky="EW")

# Buttons
search_button = tk.Button(
    width=17,
    text="Search",
    command=find_password,
    bg=SECONDARY_COLOR,
    fg=TEXT_COLOR,
    font=BUTTON_FONT,
    activebackground=ENTRY_BG,
    activeforeground=TEXT_COLOR,
    relief="flat",
    cursor="hand2",
    borderwidth=0,
    pady=0
)
search_button.grid(row=1, column=2, columnspan=2, padx=4, sticky="EW")

eye_button = tk.Button(
    width=6,
    text="Show",
    command=toggle_password,
    bg=SECONDARY_COLOR,
    fg=TEXT_COLOR,
    font=BUTTON_FONT,
    activebackground=ENTRY_BG,
    activeforeground=TEXT_COLOR,
    relief="flat",
    cursor="hand2",
    borderwidth=0,
    pady=0

)
eye_button.grid(row=3, column=2, padx=4, sticky="EW")

generate_password_button = tk.Button(
    width=10,
    text="Generate",
    command=generate_password,
    bg=SECONDARY_COLOR,
    fg=TEXT_COLOR,
    font=BUTTON_FONT,
    activebackground=ENTRY_BG,
    activeforeground=TEXT_COLOR,
    relief="flat",
    cursor="hand2",  # the cursor becomes a pointing hand (like when hovering over a link on a webpage)
    borderwidth=0,
    pady=0
)
generate_password_button.grid(row=3, column=3, sticky="EW")

save_button = tk.Button(
    text="Save Password",
    command=save,
    bg=PRIMARY_COLOR,
    fg=TEXT_COLOR,
    font=BASE_FONT,
    activebackground=PRIMARY_HOVER,
    activeforeground=TEXT_COLOR,
    relief="flat",
    cursor="hand2",
    borderwidth=0,
    pady=0,  # a button's height is usually controlled more by padding than by the height parameter
)
save_button.grid(row=4, column=1, columnspan=4, sticky="EW", pady=15)

window.mainloop()
