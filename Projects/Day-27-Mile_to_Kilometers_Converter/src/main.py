import tkinter
from tkinter import messagebox


# ---------------------------- FUNCTIONS ---------------------------- #

def calculate():
    """Converts miles to kilometers and updates the label."""
    miles_input = entry.get()

    try:
        miles = float(miles_input)
    except ValueError:
        messagebox.showinfo(title="Error", message="That's not a valid number. Please try again.")
        entry.delete(0, tkinter.END)
        return  # exit function if input is invalid

    km = round(miles * 1.609344, 2)
    km_label.config(text=km)


# ---------------------------- UI SETUP ---------------------------- #

# Window Setup
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=30, pady=20)

# Centering Widgets
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

# Entry field (user input)
entry = tkinter.Entry(width=10)
entry.grid(column=1, row=0)
entry.focus()  # so the user can type immediately

# Labels
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

equality_label = tkinter.Label(text="is equal to")
equality_label.grid(column=0, row=1)

km_label = tkinter.Label(text="0.00")
km_label.grid(column=1, row=1)

km_text_label = tkinter.Label(text="Km")
km_text_label.grid(column=2, row=1)

# Button
calculate_button = tkinter.Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

# Bind Enter key to trigger calculate()
window.bind("<Return>", lambda event: calculate())

# Keep window open
window.mainloop()
