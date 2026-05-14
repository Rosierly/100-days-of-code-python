# Day 20 - Snake Game Part 1
A Snake Game built with Python Turtle Graphics featuring smooth movement, keyboard bindings for directional controls, and object-oriented design.


## Notes

### Turtle Graphics Screen Methods
```python
from turtle import Screen

# Screen Setup
screen = Screen()  # creates the game window
screen.setup(width, height)  # sets screen dimensions (width and height are measured in pixels)
screen.bgcolor(color)  # changes background color
screen.title(title)  # sets window title

# Event Handling
screen.listen()  # listens for keyboard input
screen.onkey(fun=func, key=key)  # binds a function to a keyboard key
screen.onclick(fun)  # binds a function to a mouse click

# Screen Animation & Refreshing
# controls how often the screen refreshes (0 = manual updates, 1 = every action/default, 5 = every 5 actions)
screen.tracer(0)  # turns off automatic screen refreshing 
screen.update()  # manually updates/refreshes the screen

# Screen Utilities
screen.screensize()  # returns or sets the drawable canvas size
screen.clearscreen()  # clears the screen and resets everything
screen.reset()  # resets turtles and screen settings
screen.bye()  # closes the Turtle window

# User Input Dialogs
screen.textinput(title, prompt)  # opens a popup text input dialog
screen.numinput(title, prompt)  # opens a popup number input dialog -> returns a numeric value automatically
screen.ontimer(fun, t)  # runs a function after a delay (in milliseconds)

# Keep the Window Open
screen.mainloop()  # keeps the application running and listening for events (alternative to exitonclick())
screen.exitonclick()  # keeps the window open until the user clicks on it
# mainloop() is best for interactive programs and games.
# exitonclick() is best for simple/static Turtle drawings.
```
***

### Python Time Module Methods
###### The time module lets you work with time in Python, including delays, timers, and current time functions.
```python
import time

# Delays & Pausing
time.sleep(seconds)  # pauses the program for a number of seconds

# Current Time Functions
time.time()  # returns current time in seconds since Jan 1, 1970
time.ctime()  # returns the current date and time as a readable string (e.g. Tue May 14 15:30:22 2026)
time.localtime()  # returns current local time as a structured object (e.g. tm_hour=15, tm_min=30, tm_sec=22)

# High Precision Timing
time.perf_counter()  # high-precision timer -> more precise than time.time()

# ================================= Examples =================================

# Measuring Elapsed Time
start = time.time()
# some code here
end = time.time()
print(end - start)  # prints elapsed time in seconds

# Accessing Local Time Data
current_time = time.localtime()
print(current_time.tm_hour)  # output: 15
print(current_time.tm_min)  # output: 30
print(current_time.tm_sec)  # output: 22

# Measuring Execution time with perf_counter()
start = time.perf_counter()
# code to measure
end = time.perf_counter()
print(end - start)  # prints execution time in seconds
```
***

### Common Game Development Pattern
```python
from turtle import Screen
import time

screen = Screen()
screen.tracer(0)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)  # frame delay -> controls game speed / animation smoothness
```
***

### range() Function Parameters & Usage
###### The range() function generates a sequence of numbers and is commonly used in loops.
```python
range(stop)
range(start, stop)
range(start, stop, step)

# `start` -> number the sequence starts from (default is 0)
# `stop` -> sequence stops BEFORE this number (not included)
# `step` -> amount the numbers increase/decrease by (default is 1)

# Note:
# A negative `step` makes the sequence go backwards.

# ================================= Example =================================
range(10, 0, -1)  # output: 10, 9, 8, 7, ..., 1
```
***

### References:
- *[The tracer() method](https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.tracer)*
***
