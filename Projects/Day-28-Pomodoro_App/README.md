# Day 28 - Pomodoro GUI App
A Pomodoro timer desktop app built with Tkinter that alternates between focused work sessions and breaks, using a visual countdown and progress checkmarks to track completed cycles.


## Notes

### PhotoImage
###### Tkinter's built-in class for loading and displaying image files such as PNG and GIF.
```python
import tkinter as tk

image = tk.PhotoImage(file="tomato.png")

label = tk.Label(image=image)
label.pack()
```

Getting an image's dimensions
```python
# Use the width() and height() methods to retrieve the dimensions of a PhotoImage object.
width = image.width()
height = image.height()

print(width, height)
```
***

### Canvas Widget
###### A widget that allows you to draw and layer items such as images, text, shapes, and lines.
```python
import tkinter as tk

window = tk.Tk()

canvas = tk.Canvas(width=200, height=220)
canvas.pack()

image = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=image)
# The image parameter accepts a PhotoImage object, not a file path. 
# The x and y coordinates specify the center position of the image.

# Add text on top of the image.
canvas.create_text(100, 110, text="Hello")

window.mainloop()
```

Common Canvas Methods
```python
canvas.create_image(x, y, image=image)
canvas.create_text(x, y, text="Hello")
canvas.create_line(x1, y1, x2, y2)
canvas.create_rectangle(x1, y1, x2, y2)
canvas.create_oval(x1, y1, x2, y2)

# Note: Items added later are drawn on top of previously added items.
```
***

### Removing the Canvas Border (Outline Box)
###### Tkinter’s Canvas widget shows a default border (highlight/focus outline). You can remove it by disabling the highlight thickness and border.
```python
canvas = tk.Canvas(
    width=200,
    height=200,
    highlightthickness=0,  # removes the focus border line
    bd=0                   # removes the widget border (extra safety)
)
```
***

### Avoid `while` Loops in Tkinter
###### Tkinter GUI programs are event-driven, meaning they respond to user actions and system events through mainloop(). 
###### Using a blocking while loop stops the program from processing these events, freezing the GUI.
```python
import tkinter as tk

window = tk.Tk()
label = tk.Label(text="Hello")
label.pack()

# This freezes the GUI!
while True:
    print("Looping...")
    
window.mainloop()

# Note:
# In Tkinter, never block the main thread with while loops — use event-driven methods like .after() for updates and timers.
```

Example: GUI freezes for 5 seconds
```python
# The problem isn't the existence of a while loop itself—it's that Tkinter can't process events while the loop is running.
# If the loop runs for a long time before reaching break, the GUI will appear frozen during that time.

import tkinter as tk
import time

window = tk.Tk()

def start():
    count = 0

    while True:
        print(count)
        time.sleep(1)  # simulate work
        count += 1

        if count == 5:
            break

    print("Loop finished")

button = tk.Button(text="Start", command=start)
button.pack()

window.mainloop()

# Clicking Start freezes the GUI for 5 seconds. 
# The loop eventually ends, but the interface is unresponsive while the loop runs.
```
***

### Tkinter `after()` and `after_cancel()`
###### Tkinter is event-driven. Instead of using while loops for timers, countdowns, or repeated actions, use after() to schedule functions without blocking the GUI.

Basic Usage
```python
window.after(delay_ms, function)

# Parameters:
# 
# delay_ms → delay in milliseconds
# function → function to call after the delay
# Optional arguments can be passed after the function

# ================================= Example =================================
import tkinter as tk

window = tk.Tk()

def say_hello():
    print("Hello!")

window.after(3000, say_hello)  # run after 3 seconds

window.mainloop()
```

Creating a Repeating Timer
```python
# A function can schedule itself again using after(), creating a loop that runs at fixed intervals.

import tkinter as tk

window = tk.Tk()

count = 0

def update():
    global count

    print(count)
    count += 1

    window.after(1000, update)

update()

window.mainloop()

# This creates a non-blocking loop that keeps the GUI responsive.
```

Self-Calling Functions with after()
```python
import tkinter as tk

window = tk.Tk()
label = tk.Label(text="Hello")
label.pack()

def update_label(new_text):
    label.config(text=new_text)

    # Schedule this function to run again after 1 second
    window.after(1000, update_label, "Hello")

update_label("Hello")

window.mainloop()

# Note:
# The function schedules itself using after(). This is a form of looping without a while loop.
# Similar to recursion, but the next call is delayed and managed by Tkinter's event loop.
# Useful for clocks, countdowns, animations, and periodic updates.
```

Return Value of after()
```python
# after() returns an identifier (ID) for the scheduled task.

timer_id = window.after(1000, update)
print(timer_id)  # example: after#0

# Store this ID if you may need to cancel the task later.
```

Cancelling a Scheduled Task
```python
# Use after_cancel() with the task ID returned by after().

timer_id = window.after(1000, update)

window.after_cancel(timer_id)

# This is commonly used for reset buttons, countdown timers, and stopping repeating tasks.
```
***

### How to change Canvas elements
###### In Tkinter, Canvas items (like text, shapes, etc.) are not widgets like Labels.  
###### They are objects stored inside the Canvas, and you update them using `itemconfig()` with their item ID.
```python
# For a label (widget)
label.config(text="new text")

# For a canvas text item
item_text = canvas.create_text(100, 100, text="initial text")
canvas.itemconfig(item_text, text="new text")  # update the existing canvas item using its ID
```
***

### Number Formatting with Format Specifiers
###### Format specifiers control how values are displayed in f-strings. They are placed after a colon (`:`) inside the braces.
```python
# ==================================== Example 1 ====================================

number = 5
print(f"{number:03d}")  # output: 005
# 03d means:
# 0 → pad with zeros
# 3 → minimum width of 3 characters
# d → display as a decimal integer

# ==================================== Example 2 ====================================

# Timer Formatting
minutes = 1
seconds = 5

print(f"{minutes:02d}:{seconds:02d}")  # output: 01:05
# This is commonly used in clocks, countdown timers, and time displays to ensure numbers always appear with two digits.

# ==================================== Example 3 ====================================

pi = 3.14159
print(f"{pi:.2f}")  # output: 3.14
# . → starts the precision specification
# 2 → display 2 digits after the decimal point
# f → format as a floating-point number
```
***

### Dynamic Typing in Python
###### Python uses dynamic typing, meaning you don’t need to declare a variable’s type. The type is determined automatically at runtime and can change during execution.
```python
# Type is assigned automatically
x = 10      # integer
x = "hello" # now a string

# Type can change
value = 3.14
print(type(value))  # float

value = "text"
print(type(value))  # str
```
***


## Tkinter Widget Options Cheat Sheet
###### These are the most frequently used arguments you can pass into Tkinter widgets like Label, Button, Canvas, Frame, etc.

| Argument            | Description | Example |
|---------------------|-------------|---------|
| canvas fill         | Color of text or shapes inside Canvas | `canvas.create_text(..., fill="white")` |
| bg / background     | Background color of widget | `bg="yellow"` |
| fg / foreground     | Text color | `fg="white"` |
| font                | Font family, size, style | `font=("Courier", 20, "bold")` |
| activebackground    | Background when clicked | `activebackground="green"` |
| activeforeground    | Text color when clicked | `activeforeground="white"` |
| highlightbackground | Border color when not focused | `highlightbackground="red"` |
| highlightthickness  | Thickness of focus border | `highlightthickness=2` |
| bd / borderwidth    | Border size | `bd=5` |
| relief              | Border style (flat, raised, sunken, groove, ridge) | `relief="raised"` |
| width               | Widget width (pixels or chars) | `width=10` |
| height              | Widget height | `height=2` |
| padx                | Horizontal padding | `padx=10` |
| pady                | Vertical padding | `pady=10` |
| anchor              | Content alignment | `anchor="center"` |
| text                | Displayed text | `text="Hello"` |
| textvariable        | Bind text to variable | `textvariable=my_var` |
| wraplength          | Wrap text after pixels | `wraplength=200` |
| justify             | Text alignment inside widget | `justify="center"` |
| image               | Display an image in widget | `image=my_img` |
| compound            | Combine text + image layout | `compound="center"` |
| command             | Function on click | `command=start_timer` |
| state               | Widget state (normal, disabled, active) | `state="disabled"` |
| cursor              | Mouse cursor style | `cursor="hand2"` |
| takefocus           | Allow keyboard focus | `takefocus=0` |
| pack()              | Simple layout manager | `widget.pack()` |
| grid()              | Row/column layout system | `widget.grid(row=0, column=1)` |
| place()             | Absolute positioning | `widget.place(x=50, y=100)` |
| fill (pack)         | Widget expansion in container (`x`, `y`, `both`, `none`) | `widget.pack(fill="x")` |
| expand | Whether widget takes extra space in container | `widget.pack(expand=True)` |
| columnspan | Number of columns a widget spans in `.grid()` | `widget.grid(row=0, column=0, columnspan=3)` |
| rowspan | Number of rows a widget spans in `.grid()` | `widget.grid(row=0, column=0, rowspan=2)` |
| sticky | Stretch/alignment inside grid cell | `grid(sticky="nsew")` |
***

### References:
- *[Color Hunt - Color Palettes](https://colorhunt.co/)*
- *[TCL tk Docs: after()](https://www.tcl-lang.org/man/tcl8.6/TclCmd/after.htm)*
- *[Python and Dynamic Typing Explained](https://stackoverflow.com/questions/11328920/is-python-strongly-typed)*
***
