# Day 19 - Turtle Race
A turtle graphics racing game where the user places a bet on a colored turtle and watches randomly moving racers compete to reach the finish line first.

<img width="auto" height="480" alt="day-19-project" src="https://github.com/user-attachments/assets/43cd7e8b-936a-40d1-a4fb-e0e70252f54a" />

## Notes

### Higher Order Functions & Functions as Arguments
###### A higher-order function is a function that accepts or returns other functions.
```python
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

# HIGHER-ORDER FUNCTIONS
# calculator() is a higher-order function because it accepts another function as an argument.
# Some programming languages do not support this concept, but it is commonly used in Python.
# Higher-order functions are especially useful for event handling and callbacks.

# The 3rd parameter accepts another function as an argument.
def calculator(n1, n2, func):
    return func(n1, n2)  # returns the result of a function, not the function itself

# PASSING FUNCTIONS AS ARGUMENTS
# When passing a function as an argument, we do NOT use parentheses.
# Parentheses () call the function immediately and are only used when you want to pass its return value.
# Without parentheses, we pass a reference to the function itself as the argument.

# Passing the add function as an argument
result = calculator(2, 3, add)
print(result)  # output: 5
```
***

### Event Listeners - Turtle Graphics
###### Event listeners wait for user actions (such as key presses or mouse clicks) and trigger functions in response.
```python
# Turtle Event Listeners - Using screen events
# listen() method → Allows the turtle screen to listen for and respond to user-triggered events (such as key presses).

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()  # creating an object from the Screen class to control our window


def move_forwards():
    """Move tim forward by 10 paces"""
    tim.forward(10)

    
screen.listen()  # using the listen() method of the Screen class to start listening for events

# In order to bind a keystroke to an event in our code, we use the onkey() method, an event listener.

# Parameters of onkey(fun, key)
#   fun = a function with no arguments or None
#   key = a string: key (e.g. "a") or key-symbol (e.g. "space")

# Binds a specific function to a specific key
screen.onkey(key="space", fun=move_forwards)  # use keyword arguments instead of positional arguments
screen.exitonclick()  # keep the window screen open
```
***

### Object State and Instances
###### Instance → A unique object created from a class.
###### State → The current attributes and behavior of an object at a given moment.
```python
from turtle import Turtle

# CLASSES & OBJECTS
# Classes are blueprints used to create objects.

timmy = Turtle()
tommy = Turtle()
timmy.color("green")
tommy.color("purple")

# INSTANCE
# Even though timmy and tommy are both Turtle objects, they function independently of each other.
# In programming, we say they are separate instances of the Turtle class (examples of Turtle objects).
# They can have different attributes and perform different actions at the same time.

# STATE
# Different instances can have different states.
# For example, timmy's color could be green while tommy's color is purple.
# In this case, they have different states in terms of their appearance attribute.
```
***

### Turtle Coordinate System
###### It is a 2D grid that uses x and y coordinates to position the turtle on the screen.
```python
# (0, 0) is the center of the screen
# Positive x → right
# Negative x → left
# Positive y → up
# Negative y → down
```
***

### Challenge: Make an Etch-a-Sketch
```python
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# Create separate functions for each movement direction because
# the onkeypress() method only accepts functions without arguments.


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_left():
    tim.setheading(tim.heading() + 10)  # Alternative: tim.left(10)


def turn_right():
    tim.right(10)  # Alternative: tim.setheading(tim.heading() - 10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()  # Move the turtle to the starting position (center of the screen)
    tim.pendown()


# onkeypress() triggers a function continuously while the specified key is being pressed.
screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
```

### References:
- *[The listen() method](https://docs.python.org/3/library/turtle.html#turtle.listen)*
- *[Turtle .textinput() documentation](https://docs.python.org/3.1/library/turtle.html#turtle.textinput)*
***
