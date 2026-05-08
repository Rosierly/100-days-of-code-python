# Day 18 - The Hirst Painting
A Python program that recreates a Hirst-style dot painting using turtle graphics and colors extracted from an image.

<img width="auto" height="510" alt="day-18-project" src="https://github.com/user-attachments/assets/f05bf0e3-0afa-41ec-b7cd-7fda70d6644f" />

## Packages used:
- colorgram.py → extracts colors from images
- pillow → image-processing dependency used by colorgram.py

## Notes

### Python Tuples
###### A tuple is an ordered and immutable collection of values in Python.
```python
my_tuple = (1, 3, 8)
print(my_tuple[0]) # We can access each item like we do with lists, by typing their index.

# What's the difference between tuples and lists?
# In tuples you can't change the values like you can in lists (you also can't remove items).
# IF you try, you'll get a TypeError: 'tuple' object does not support item assignment
# Once you create your tuple, you can't change it later - it's immutable.

# If you need to modify it, you can convert it into a list:
my_list = list(my_tuple)    

# Modify the list
my_list[0] = 100
my_list.append(4)

# Convert list back to tuple
my_tuple = tuple(my_list)
```
***

### Importing, Aliasing and Installing Modules
Basic Import
```python
# keyword module_name
import turtle

turtle = turtle.Turtle() # this is how you create an object from the Turtle class
```
from...import...
```python
# keyword module_name keyword thing_in_module (like a list, function, class...)
from turtle import Turtle

turtle = Turtle() # we can create an object directly from the Turtle class
```
from...import *
```python
# Importing everything from a module lets you use its contents directly in the current file.
# However, it can make it harder to tell where functions or classes come from, and it’s generally uncommon. 
from turtle import *

# The turtle module automatically creates a default turtle object behind the scenes.
forward(100)  # Because of that, you can call methods like forward() directly.
```
Aliasing Modules
```python
# keyword module_name keyword alias_name
import turtle as t

turtle = t.Turtle() # we use "t" as a shorter alias for the turtle module
```
Installing Modules
```python
# Modules like turtle come with Python's standard library by default: a basic collection of built-in Python modules.
# However, some modules must be installed before you can use them (e.g. from pypi.org).

import heroes # This package isn't installed, so PyCharm shows an error warning suggesting installation.
# If a package isn't installed, you'll get a ModuleNotFoundError.

# Installed packages are added to the project's local virtual environment (.venv) — on a per-project basis.
# Project Folder > .venv > lib (here you can find the installed packages for that project)
```
Difference between modules and software
- ######  Software (like PyCharm) is installed once, and it's available globally across your computer.
- ###### Packages in a virtual environment are installed only into the project you're building.
***

### Tkinter (Tk)
###### Tkinter is Python’s built-in library used to create Graphical User Interfaces (GUIs).
###### GUIs display visual elements and allow user interaction through actions like clicking and dragging.
###### The turtle module relies on tkinter to display graphics on the screen.
***

### Turtle Graphics
###### Turtle graphics is a simple graphics system where shapes and patterns are created by moving a “turtle” around the screen with programming commands.
```python
from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape("turtle") # shape() method of Turtle class used to set the shape
turtle.pencolor("black")  # pencolor() method used to set the pen color
turtle.color("red")  # color() method used to change the turtle and pen color
turtle.fillcolor("green") # fillcolor() method used to set the fill color of the turtle shape
turtle.forward(100)
turtle.right(90)

# Keep the screen open until we click on it (by using the exitonclick method)
screen = Screen()
screen.exitonclick()

# You can change the drawing color using:
#   1. A color string (e.g. "red", "blue")
#   2. A hex color string (e.g. "#ff0000")
#   3. An RGB color value -> format: color(r, g, b)
```
***

### How to generate random RGB colors with Turtle Graphics
```python
import random
import turtle as t

tim = t.Turtle()

# 1. pencolor(colorstring)
#    Sets the pen color using a color name like "red", "yellow", or a hex color like "#33cc8c".

# 2. pencolor((r, g, b))
#    Sets the pen color using an RGB tuple.
#    Each RGB value must be in the range 0..colormode, where colormode is either 1.0 or 255.

# turtle.colormode(1.0 or 255)
# To use RGB values between 0 and 255, we must first set the colormode to 255.
# We change the colormode through the turtle module itself, not the Turtle object.
t.colormode(255)

def generate_random_color():
    """This function is going to return a random color using RGB"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

# or:

def generate_random_rgb():
    """This function is going to return a random color using RGB"""
    return tuple(random.randint(0, 255) for _ in range(3))

random_rgb = generate_random_rgb()
tim.pencolor(random_rgb)
```
***

### Turtle Challenges
Common Setup and Imports for Turtle Challenges
```python
# Use this setup code before running any of the Turtle challenges below
import turtle as t
import random

turtle = t.Turtle()

# Change the color mode so RGB values can use the range 0–255
t.colormode(255)


def generate_random_rgb():
    """This function is going to return a random color using RGB"""
    return tuple(random.randint(0, 255) for _ in range(3))


screen = t.Screen()
screen.exitonclick()
```
Draw a Square
```python
for _ in range(4):
    turtle.forward(100)
    turtle.left(90)
```
Draw a Dashed Line
```python
for _ in range(15):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
```
Drawing Different Shapes
```python
# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
# Each shape should have a random color and side length of 100.

for sides in range(3, 11):  # shapes with 3 to 10 sides
    turtle.pencolor(generate_random_rgb())
    
    for _ in range(sides):  # draw that shape
        turtle.forward(100)
        turtle.left(360 / sides)
```
Draw a Random Walk
```python
directions = [0, 90, 180, 270]

# speed() method (parameter: speed - a number from 0 to 10 or a speed string)
turtle.speed("fastest")  # make the turtle drawing faster
# pensize() method (parameter: width - pen thickness in pixels)
turtle.pensize(15)  # increase the thickness of the pen

for _ in range(200):
    turtle.color(generate_random_rgb())
    # setheading() method (parameter: to_angle - an integer or float)
    turtle.setheading(random.choice(directions))  # choose a random direction
    turtle.forward(30)
```
Draw a Spirograph
```python
def draw_spirograph(size_of_gap):
    """Draws circles while rotating the turtle by size_of_gap each time."""
    for _ in range(360 // size_of_gap):
        turtle.pencolor(generate_random_rgb())
        turtle.circle(100)
        turtle.left(size_of_gap)


turtle.speed("fastest")
draw_spirograph(5)
```
***

### References:
- *[Turtle Graphics Documentation](https://docs.python.org/3/library/turtle.html)*
- *[Trinket Turtle Colors](https://trinket.io/docs/colors)*
- *[Turtle Colors](https://cs111.wellesley.edu/reference/colors)*
- *[RGB Calculator Tool](https://www.w3schools.com/colors/colors_rgb.asp)*
- *[Colorgram Package Documentation](https://pypi.org/project/colorgram.py/)*
***
