# Day 29 - Password Manager GUI App

A password manager that generates secure passwords, toggles visibility, copies generated passwords to the clipboard, and stores website login credentials.

<img width="auto" height="620" alt="day-29-project" src="https://github.com/user-attachments/assets/8a7469de-15fe-41be-8624-007a07120512" />

## Packages used:
- pyperclip → cross-platform clipboard module used to copy and paste text to the system clipboard programmatically

## Notes

### How to Display an Image without Canvas
###### You can display images in Tkinter using a Label, which is simpler than using a Canvas when you only need to show an image.
```python
# Label is best for static images (logos, icons, etc.)
# No need for Canvas unless you are combining images with text or precise positioning

import tkinter as tk

window = tk.Tk()
window.title("Password Manager")
window.config(bg="seashell")

logo_img = tk.PhotoImage(file="../assets/logo.png")
label = tk.Label(window, image=logo_img, bg="seashell")
label.pack()

# Keep a reference to the image to prevent it from disappearing (avoid garbage collection issues)
label.image = logo_img
# If there is no reference kept, Python may think the image is not needed anymore and delete it from memory.
# Instead, store the image in the label so Python keeps it in memory and Tkinter can display it.

window.mainloop()
```
***

### Columnspan & Rowspan (Grid Spanning)
###### Used to make a widget span multiple cells.
```python
widget.grid(column=1, row=2, columnspan=2)

# columnspan → widget stretches across multiple columns
# rowspan → widget stretches across multiple rows
```
***

### Sticky (Widget Alignment in Grid)
###### Controls how a widget expands inside its grid cell.
```python
widget.grid(row=0, column=1, sticky="EW")

#  Sticky Values:
# N → top
# S → bottom
# E → right
# W → left

# Common combinations:
# "E" → align right
# "W" → align left
# "EW" → stretch horizontally
# "NS" → stretch vertically
# "NSEW" → fill entire cell

# Note:
# Use sticky="EW" to make widgets stretch nicely
```
***

### Tkinter Entry Methods: `insert` and `delete`
###### `insert(index, text)` → Inserts text at a given position in the entry.
```python
entry = tk.Entry(window)  # creates a text input box and places it inside the main window
entry.insert(0, "Hello")  # inserts "Hello" at the start
```

###### `delete(start, end)` → Deletes characters from start to end. Use tk.END to delete to the end.
```python
entry.delete(0, tk.END)  # clears the entire entry
entry.delete(0, 5)  # deletes first 5 characters
```
***

### Using the `string` Module
###### Provides ready-made constants for letters, digits, and other character sets, making code simpler and more readable.
```python
import string

# Letters
letters = list(string.ascii_letters)  # a-z + A-Z
# string.ascii_letters → all lowercase and uppercase letters

# Lowercase letters
lowercase = list(string.ascii_lowercase)  # a-z

# Uppercase letters
uppercase = list(string.ascii_uppercase)  # A-Z

# Digits
numbers = list(string.digits) # 0-9
# string.digits → all numbers 0–9

# Symbols and punctuation
symbols = list(string.punctuation)

```
***

### References:
- *[Canvas Documentation](https://tkdocs.com/tutorial/canvas.html)*
- *[Effbot Archive - The Tkinter Canvas Widget](https://web.archive.org/web/20201108093851/effbot.org/tkinterbook/canvas.htm)*
- *[Python Writing to File Documentation](https://www.w3schools.com/python/python_file_write.asp)*
- *[Entry Widget Docs](https://tkdocs.com/tutorial/widgets.html#entry)*
- *[Python String join() Method Documentation](https://www.w3schools.com/python/ref_string_join.asp)*
***
