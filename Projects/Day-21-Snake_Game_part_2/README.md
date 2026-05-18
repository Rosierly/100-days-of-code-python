# Day 21 - Snake Game Part 2
A classic Snake game built with Python’s Turtle module where the player controls a snake, collects food to increase the score, and avoids collisions with walls and its own tail.

<img width="auto" height="550" alt="day-21-project" src="https://github.com/user-attachments/assets/970d057d-0583-48f2-86e6-b5d0ddf7ef57" />

## Notes

### Class Inheritance
###### It's a feature of OOP that allows a child class to inherit the attributes and methods of a parent class.
```python
# Parent Class (Superclass)
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


# Child Class (Subclass)
class Fish(Animal):  # the Fish class (subclass) inherits from the Animal class (superclass)
    
    def __init__(self):
        super().__init__() 
        # super() refers to the parent class (Animal)
        # super().__init__() gives Fish access to the parent class attributes and methods
    
    # Modifying a method inherited from the parent class
    def breathe(self):  # the method must have the same name as the parent class method to override it
        super().breathe()  # to keep the same functionality as the superclass we're inheriting from
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")

# Creating an object from the Fish class
nemo = Fish()

# Fish methods
nemo.swim()
nemo.breathe()

# Inherited attribute from Animal
print(nemo.num_eyes)

# The Fish object inherits:
# - Attributes from Animal (num_eyes)
# - Methods from Animal (breathe)
# - And can also modify inherited methods
```
Using a Different Method Name
```python
# super().breathe() adds the functionality of the parent class method.
# If the subclass method has the same name, it overrides the parent method.
# If it has a different name, it creates a new method instead.

class Animal:
    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):
    def breathe_underwater(self):
        super().breathe()
        print("Doing this underwater.")


nemo = Fish()

# Inherited parent method
nemo.breathe()  # output: # Inhale, exhale.

# New subclass method
nemo.breathe_underwater()  # output: Inhale, exhale. & Doing this underwater.
```
***

### How to Detect Collision with Turtle Graphics
###### Turtle Graphics has no built-in collision detection, so collisions are detected using the `distance()` method to check how close two objects are.
```python
turtle.distance(other_turtle)  # measures distance from the turtle to another turtle object
turtle.distance(x, y)  # measures distance from the turtle to x/y coordinates

# ================================= Examples =================================

if player.distance(enemy) < 20:  # if distance is less than 20 pixels -> collision detected
    print("Collision detected!")

if player.distance(100, 50) < 20:  # if player is close to coordinates (100, 50)
    print("Reached the target position!")
```
***

### Slicing Lists & Tuples
###### Python slicing is a way to access a portion of a sequence (like a list, string, or tuple).
```python
# Slicing Syntax -> sequence[start:stop:step]

# `start` -> index where slicing begins (included)
# `stop` -> index where slicing ends (not included)
# `step` -> increment between items (default is 1)
```
```python
# ================================= Lists =================================

# To get hold of a small section of a list, use slicing
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]

new_list = piano_keys[2:5]
# positions 2, 3, 4 -> "c", "d", "e"
# position 5 is not included because slicing stops BEFORE the stop index
# these are slicing boundaries (positions), not actual item positions
print(new_list) # output: ["c", "d", "e"]

# Slice from a starting position until the end
print(piano_keys[2:])  # output: ["c", "d", "e", "f", "g"]

# Slice from the beginning up to a position
print(piano_keys[:4])  # output: ["a", "b", "c", "d"]

# ================================= Tuples =================================

# Slicing also works with tuples
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

print(piano_tuple[1:])  # output: ("re", "mi", "fa", "so", "la", "ti")
print(piano_tuple[:4])  # output: ("do", "re", "mi", "fa")

# ================================= Step / Increment =================================

# The third slicing value sets the increment (step)

print(piano_keys[2:5:2])
# slicing from position 2 to 5, but taking every second item
# output: ["c", "e"]

print(piano_keys[::2])
# slices the entire list and skips every second item
# output: ["a", "c", "e", "g"]

print(piano_keys[::-1])
# negative step reverses the sequence
# output: ["g", "f", "e", "d", "c", "b", "a"]
```
***

### References:
- *[The shape() and shapesize() methods](https://docs.python.org/3/library/turtle.html#turtle.shape)*
- *[The write() method](https://docs.python.org/3/library/turtle.html#turtle.write)*
***
