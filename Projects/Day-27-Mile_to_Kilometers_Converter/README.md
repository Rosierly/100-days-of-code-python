# Day 27 - Mile to Kilometers Converter
A simple Tkinter GUI application that converts miles to kilometers with real-time input validation and a clean, interactive interface.


## Notes

### Default Function Arguments
###### Default function arguments are values given in a function definition that are used when no argument is provided during the function call.
```python
def my_function(a, b=2, c=3, d=4):
    print(f"The values of (a, b, c, d) is : {a, b, c, d}.")
    
# Function Call Example:
my_function(6, d=9)  # d gets overridden

# Key Rules:
# Default values are set in the function definition (b=2, c=3, d=4).
# Required arguments must come first (a is required).
# Default arguments can be overridden when calling the function.
```
***

### `*args` in Python (Advanced Python Arguments: Unlimited Positional Arguments)
###### *args allows a function to accept any number of positional arguments, which are stored as a tuple inside the function.
```python
def test(*args):  # the asterisk (*) allows any name after it; default name by convention is args
    for n in args:
        print(n)

test(5, 6, 9)

# All values passed into the function are packed into a tuple called args.
# You can loop through or index them.
```

Accessing *args
```python
def add(*args):
    first_item = args[0]  # access first item by index
    # position matters because args is ordered

    total = 0
    for n in args:
        total += n
    return total

result = add(1, 2, 3, 6)
print(result)  # output: 12
```
***

### `**kwargs` in Python (Advanced Python Arguments: Keyword Arguments)
###### **kwargs allows a function to accept any number of keyword arguments, which are stored as a dictionary inside the function.
```python
def calculate(**kwargs):  # the double asterisk (**) allows any name after it; default name by convention is kwargs
    print(kwargs)
    print(type(kwargs))  # output: <class 'dict'>

    for key, value in kwargs.items():
        print(key)
        print(value)

    print(kwargs["add"])  # output: 3

calculate(add=3, multiply=5)

# kwargs becomes a dictionary, you can loop through it using .items()
# You can access values using keys (e.g., kwargs["add"])
```

Combining Normal Parameters with `**kwargs`
```python
def calculator(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculator(2, add=5, multiply=4)
```

Creating a Class with `**kwargs`
```python
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(model="GT-R")
print(my_car.make)  # output: None

# Note: Key Difference: [] vs .get()
# kw["make"] → gives KeyError if missing
# kw.get("make") → returns None if missing
```
***

### Tkinter
###### Tkinter is Python’s built-in library for creating Graphical User Interfaces (GUIs) with windows, buttons, and other interactive elements.
```python
import tkinter

# Create the main window
window = tkinter.Tk()

# Configure the window
window.title("My First GUI Program")
window.minsize(width=500, height=300)  # defines minimum window dimensions

# Creating a Label (Text on Screen)
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))

# Displaying Widgets (Layout Management)
my_label.pack(expand=True, side="left")  # pack() method: places the widget in the window
# Common parameters:
# side → position ("top", "bottom", "left", "right")
# expand=True → allows widget to take available space

# Keeping the Window Open (Event Loop)
window.mainloop()
# This keeps the window running, listens for user interactions, and must be placed at the end of the program.
```

Creating a Simple Tkinter Window
```python
import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()

window.mainloop()
```

Using `from tkinter import *`
```python
# Imports the entire Tkinter module into your program
# Allowing you to use all Tkinter classes and functions (like Label, Button, Entry) directly without writing tkinter before them.

# Example:
from tkinter import *

window = Tk()
window.title("My App")

label = Label(text="Hello World")
label.pack()

window.mainloop()
```
***

### Configuring Tkinter Widget Options
###### Widget options control properties like color, border width, font, and appearance of a widget. These can be set in three different ways:

1. At Object Creation
```python
# Using keyword arguments
button = tkinter.Button(fg="red", bg="blue")
```

2. Using Dictionary Syntax
```python
# Treating the option name like a dictionary index
button["fg"] = "red"
button["bg"] = "blue"
```

3. Using `config()`
```python
# Useful for changing multiple properties after the widget has been created
button.config(fg="red", bg="blue")
```
***

### Label Widget
###### Used to display text or images on the screen that the user cannot directly edit.

Creating a Label
```python
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()
```

Changing Label Text
```python
# Using dictionary syntax:
my_label["text"] = "New Text"

# Using `config()`:
my_label.config(text="New Text")
```

Positioning
```python
my_label.pack(side="left")
```
***

### Button Widget
###### Performs an action when clicked.

Creating a Button
```python
# A button usually calls a function when clicked
def button_clicked():
    print("I got clicked")

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()  # centers the widget by default
```

Updating the Button Command
```python
def change_label():
    my_label.config(text="Button Got Clicked")

button["command"] = change_label
# When the button is clicked, the label text changes
```
***

### Entry Widget (Input Field)
###### Used to accept single-line text input from the user.

Creating an Entry
```python
new_entry = tkinter.Entry(width=10)
new_entry.pack()
```

Getting User Input
```python
user_text = new_entry.get()  
# get() is a method of Entry and always returns a string
# Similar to an HTML input box
```

Setting Default Text
```python
# insert(index, text) is used to add text to an Entry widget. 
# This can be useful for setting default or placeholder-like text when the application starts.

new_entry.insert(0, "Enter your name")
# insert(0, text) → inserts text at the start of the Entry.

new_entry.insert(END, string = "Some text to begin with.")
# insert(END, text) → inserts text at the end of the existing text.

# Note:
# If the Entry is empty, both 0 and END insert text in the same position.
```
***

### Challenge: Display User Input in the Label
```python
def change_display():
    my_label.config(text=new_entry.get())

# Assign Function to Button
button["command"] = change_display
```
***

### Essential Tkinter Pattern
###### This pattern is used repeatedly throughout Tkinter applications.
```python
# Create widget
widget = tkinter.Widget(...)

# Add to screen
widget.pack()

# Update later
widget.config(...)
```
***

### Text Widget
###### Used to accept and display multi-line text input.

Creating a Text Widget
```python
text = Text(height=5, width=30)
text.pack()
```

Setting Cursor Focus
```python
text.focus()
# Places the cursor inside the text box when the application starts
```

Inserting Text
```python
text.insert(END, "Example of multi-line text entry.")  # END means insert at the end.
```

Retrieving Text
```python
text.get("1.0", END)  # 1.0 = Line 1, Character 0
```
***

### Spinbox Widget
###### Lets the user select a value from a fixed range using arrows.

Creating a Spinbox & Getting the Current Value
```python
def spinbox_used():
    print(spinbox.get())
    # spinbox.get() returns the currently selected value

spinbox = Spinbox(
    from_=0,
    to=10,
    width=5,
    command=spinbox_used
)

spinbox.pack()
```
***

### Scale Widget
###### Allows the user to select a numeric value by sliding a handle.

Creating a Scale & Getting the Current Value
```python
def scale_used(value):
    print(value)
    # The callback receives the current slider value as a string.

scale = Scale(
    from_=0,
    to=100,
    command=scale_used
)

scale.pack()
```
***

### Tkinter Variable Classes (`IntVar`)
###### Widgets such as Checkbuttons and Radiobuttons often use special Tkinter variables to store their state. 
###### Tkinter variable classes are special objects used to store the values of these widgets.
```python
checked_state = IntVar()  # Stores an integer value used by Tkinter widgets to track state
# checked_state is an object created from the IntVar class
```
***

### Checkbutton Widget
###### A checkbox that can be either checked or unchecked.

Creating a Checkbutton & Getting the Current State
```python
# State Management with `IntVar()`
checked_state = IntVar()  # Stores integer values. (0: Off, 1: On)

def checkbutton_used():
    print(checked_state.get())

checkbutton = Checkbutton(
    text="Is On?",
    variable=checked_state,
    command=checkbutton_used
)

checkbutton.pack()
```
***

### Radiobutton Widget
###### Allows users to choose one option from a group.

Creating Radio Buttons & Getting the Selected Option
```python
def radio_used():
    print(radio_state.get())

# State Management with `IntVar()`
radio_state = IntVar()

radiobutton1 = Radiobutton(
    text="Option 1",
    value=1,
    variable=radio_state,
    command=radio_used
)

radiobutton2 = Radiobutton(
    text="Option 2",
    value=2,
    variable=radio_state,
    command=radio_used
)

radiobutton1.pack()
radiobutton2.pack()

# Note: How Radio Groups Work
# All radiobuttons in a group share the same variable (radio_state)

# Each button has a unique value:
# Option 1 → value = 1
# Option 2 → value = 2

# The variable stores the value of the selected button
```
***

### Listbox Widget
###### Displays a list of items from which the user can select one or more.

Creating a Listbox
```python
listbox = Listbox(height=4)
listbox.pack()
```

Adding Items
```python
fruits = ["Apple", "Pear", "Orange", "Banana"]

# Listbox is created by looping through a python list
for item in fruits:
    listbox.insert(fruits.index(item),item)  # breaks if there are duplicate values
    
# Safer option
for item in fruits:
    listbox.insert(END, item)
```

Detecting Selection Events & Getting the Selected Item
```python
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox.bind("<<ListboxSelect>>", listbox_used)
# <<ListboxSelect>> is triggered when user selects an item
```
***

### Event Binding
###### A Tkinter feature that connects user actions (like clicks, key presses, or selections) to functions. 
###### Some widgets use `command=` callbacks, while others use event bindings with `.bind()`.
```python
# Using command=
button = Button(command=my_function)

# Using event Binding with bind()
widget.bind("event", callback)
# Example:
listbox.bind("<<ListboxSelect>>", listbox_used)
```
***

### Tkinter Layout Managers: `pack()`, `place()`, `grid()`
###### Tkinter requires a layout manager to display widgets on the screen. Without one, widgets will not appear.
```python
from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = user_input.get()
    my_label.config(text=new_text)
    
# Basic Window Setup
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")

# Button
button = Button(text="Click Me", command=button_clicked)

# Entry
new_entry = Entry(width=10)
user_text = new_entry.get()
# Note: Calling .get() immediately after creation will return an empty string because nothing has been typed yet.
```

1.  pack()
###### Simplest layout manager that places widgets one below another by default and can adjust direction using side.
```python
my_label.pack()

# Example:
button.pack(side="left")
```

2.  place()
###### Absolute positioning layout manager that uses exact coordinates.
```python
my_label.place(x=0, y=0)  # top-left corner
# Good for precise control, but not responsive to resizing

# Note: 
# In Tkinter, (0, 0) is the top-left corner of the window. 
# Unlike Turtle Graphics, the origin is not at the center of the screen. 
# Coordinates increase rightward (x) and downward (y).  
```

3.  grid()
###### Layout manager that organizes widgets in rows and columns and treats the window like a table.
```python
my_label.grid(column=0, row=0)
button.grid(column=1, row=1)
user_input.grid(column=2, row=2)
# Flexible layout system - Best for most GUI apps
```

#### Important Rules + Summary
1. You cannot mix pack() and grid() in the same window  
2. You can use place() with either, but it’s usually avoided in complex layouts
3. grid() positions are relative to each other   
4. Tkinter needs a layout manager for widgets to appear on screen:
   - `pack()` → simple vertical/horizontal stacking
   - `place()` → exact positioning
   - `grid()` → structured row/column layouts (recommended)
***

### How to Add Padding Around Widgets
###### Padding adds space around widgets in the grid layout.
```python
# padx = horizontal space (left and right)
# pady = vertical space (top and bottom)

# Padding around individual widgets (grid) → space outside the widget
my_label.grid(column=0, row=0, padx=20, pady=20)

# Padding inside the widget itself → increases widget size
button = tkinter.Button(text="Button", padx= 10)
button.config(padx=30, pady=50)
button.grid(column=1, row=1)

# Padding around the entire window
window.config(padx = 20, pady=20)

# grid(padx, pady) → space outside  
# Button/Label/etc(padx, pady) → space inside
```
***

### Tkinter Widgets Summary
Key Widgets

| Widget | Purpose                | Common Methods |
|---------|------------------------|---------------|
| `Tk()` | Main application window | `title()`, `minsize()`, `mainloop()` |
| `Label` | Display text           | `config()`, `pack()` |
| `Button` | Trigger actions        | `command`, `pack()` |
| `Entry` | User Text Input        | `get()`, `insert()`, `pack()` |

Advanced Widgets

| Widget | Purpose | Common Methods / Features |
|---------|---------|--------------------------|
| `Text` | Multi-line text input | `get()`, `insert()`, `focus()` |
| `Spinbox` | Numeric selector with up/down arrows | `get()` |
| `Scale` | Slider for selecting a value | `command` callback |
| `Checkbutton` | Toggle on/off option | `IntVar()`, `get()` |
| `Radiobutton` | Select one option from a group | `IntVar()`, `get()` |
| `Listbox` | Select item(s) from a list | `insert()`, `get()`, `curselection()`, `bind()` |
***

### Common Tkinter Constants

| Constant | Purpose |
|----------|---------|
| `END` | Last position in a widget |
| `LEFT` | Left side |
| `RIGHT` | Right side |
| `TOP` | Top side |
| `BOTTOM` | Bottom side |
***

### References:
- *[Python Docs: The Packer](https://docs.python.org/3/library/tkinter.html#the-packer)*
- *[TCL tk Docs: pack()](https://www.tcl-lang.org/man/tcl8.6/TkCmd/pack.htm)*
- *[TCL tk Docs Entry()](https://www.tcl-lang.org/man/tcl8.6/TkCmd/entry.htm)*
***
