# Day 16 - Coffee Machine Program in Object-Oriented Programming (OOP)
A simulation of a coin-operated coffee machine that, as required by the exercise, uses the provided modules to serve espresso, latte, or cappuccino while tracking resources and processing payments.

<img width="auto" height="540" alt="day-16-project" src="https://github.com/user-attachments/assets/9752f472-62e5-45b2-af38-713600a8fde2" />

## Notes

### Procedural Programming
###### It's a style of coding where a program is written as a sequence of step-by-step instructions. These instructions are grouped into reusable blocks called procedures (or functions).
***

### Object-Oriented Programming (OOP)
###### It's a way of writing programs where code is organized into objects that encapsulate data (attributes) and related functions (methods). This approach helps structure programs into modular, reusable, and easier-to-manage parts, especially for complex projects.
***

### Implementing Object-Oriented Programming (OOP)
###### When modeling real-world objects in code (e.g., a waiter in a restaurant), we focus on two things:
1) **Attributes** (What the object HAS)
###### Attributes are variables that store information about the object.
```python
is_holding_plate = True
tables_responsible = [4, 5, 6]
```

2) **Methods** (What the object DOES)
###### Methods are functions that define the actions an object can perform.
```python
def take_order(table, order):
    # takes order to chef

def take_payment(amount):
    # add money to restaurant
```
***

### Class
###### In Python, a class is like a blueprint for creating objects.
###### It defines the attributes (data) and methods (functions) that objects created from it will have.
```python
class CarBlueprint:
    pass

# Naming Convention
# Classes → PascalCase: each word starts with a capital letter (e.g., CarBlueprint) 
# Variables & functions → snake_case (e.g., car_speed, calculate_total)
```
***

### Object
###### An object is an instance of a class, created from that class.
```python
car = CarBlueprint()
# CarBlueprint → Class (blueprint)
# car → Object (instance of the class)
```
***

### Turtle Graphics (turtle module)
###### The turtle module is a built-in Python library that allows you to create drawings and graphics by controlling a virtual “turtle” that moves around the screen.
```python
# ------------------------------- Creating an Object -------------------------------
import turtle # importing a module named turtle

# Accessing the Turtle class from the turtle module and storing it inside a variable named timmy
timmy = turtle.Turtle()  # constructs an object

# Alternative way (same result)
from turtle import Turtle, Screen
timmy = Turtle()

# -------------------------------- Using an Object --------------------------------
print(timmy) # output: <turtle.Turtle object at 0x00000238A38078C0>

timmy.shape("turtle")

timmy.color("coral") # call a method to change the color

timmy.forward(100) # move forward by 100 paces
```
Using Attributes & Methods from the Screen Class
```python
from turtle import Screen

my_screen = Screen()  # my_screen is an object that represents the window

# Syntax for accessing attributes: `object.attribute`
print(my_screen.canvheight)
# canvheight is an attribute associated with the object my_screen

# Syntax for using methods: `object.method()`
my_screen.exitonclick()
# A method is a function tied to an object
# This method keeps the program running until you click on the screen.
```
***

### How to add Python Packages and use PyPI
###### The Python Package Index (PyPI) is a centralized repository of open-source packages written in Python, freely accessible to all.
###### To use a package from PyPI, you need to install it first.

- For Pycharm
###### `File` > `Settings`> Click on the project (file's name) > `Project Interpreter` > Click on the `(+)`
###### Then copy-paste the name of the package in the search bar, select it and click "Install Package"
- For Replit
###### Open the side menu → click on the packages icon
###### Search for the package by typing the name into the search bar → click `install`
###### The package will appear in your installed packages list.

```python
# In PyCharm, to see the source code:
# Right-click on the name of the package → Go to → Implementation(s)

# PrettyTable is simple Python library for displaying tabular data in a visually appealing ASCII table format.
import prettytable # mow we can use everything inside this package
# or
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"  # changing an attribute (align → from centered to left)

print(table)
```
***

### References:
- *[Turtle Graphics Documentation](https://docs.python.org/3/library/turtle.html)*
- *[Turtle Color Names](https://cs111.wellesley.edu/reference/colors)*
- *[Python Package Index (PyPI)](https://pypi.org/)*
- *[PrettyTable Package](https://pypi.org/project/prettytable/)*
- *[PrettyTable Package Documentation)](https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki)*
***

