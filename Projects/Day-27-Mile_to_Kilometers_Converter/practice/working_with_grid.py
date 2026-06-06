import tkinter

# Configure the window
window = tkinter.Tk()
window.title("Grid Practice")
window.minsize(width=500, height=300)

# Label
label = tkinter.Label(text="Label", font=("Arial", 24, "bold"))
label.grid(column=0, row=0)

# Buttons
button = tkinter.Button(text="Button")
button.grid(column=1, row=1)

new_button = tkinter.Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry
entry = tkinter.Entry(width=10)
entry.insert(0, "Entry")
entry.grid(column=3, row=3)

window.mainloop()
