# Day 17 - Quiz Game Project
An object-oriented Python quiz game where the user answers true/false questions, receives feedback, and tracks their score.

<img width="900" height="533" alt="day-17-project" src="https://github.com/user-attachments/assets/78a917e5-7ef9-4025-a944-5d7a5346dfa1" />

## Notes

### Pass keyword
```python
# Creating an empty class or function raises an IndentationError: expected an indented block
# Because after a declaration and its colon, Python expects an indented block with some code.
# Use the keyword "pass" to define an empty class or function without errors.
def function():
    pass
```
***

### How to create your own class in python
```python
class User:  # name convention for class: PascalCase
    pass

user_1 = User()  # To initialize an object from a class, we have to add the parentheses at the end.
```
***

### Creating Attributes
```python
# An attribute is a variable that's associated with an object.
user_1.id = "001" # we've created a new variable named id, but in this case we attached it to an object.
user_1.username = "angela"
print(user_1.username)

# If we had lots of attributes, and we have to create more than one user.
user_2 = User()
user_2.id = "002"
user_2.username = "jack"
```
***

### Constructor - `__init__` function & creating attributes
###### It's a special method that runs when an object is created, used to initialize its attributes.
```python
# It's a part of the blueprint that allows us to specify what should happen when our object is being constructed.
# This is also known in programming as initializing an object.
# initialize = to set (variables, counters, switches etc.) to their starting values at the beginning of a program or a subprogram.

# In Python, we create the constructor by using a special function ➜ __init__()
# It's normally used to initialize attributes ➜ the things that the object will have
class User:
    
    def __init__(self, user_id, username):  # self = the actual object that's being created or being initialized
        self.id = user_id
        self.username = username
        print("new user being created...")


# The init function is going to be called every time we create a new object from this class.
user_3 = User("003", "timmy")
print(user_3.username)
```
Adding parameters to the `__init__` function
```python
# Adding parameters to __init__ means that every new object creation requires as many pieces of data as the number of parameters.
# Otherwise, a TypeError occurs, __init__() missing ... required positional arguments.
class Car:
    def __init__(self, seats):
        self.seats = seats  # is the same as (my_car.seats = 5)


my_car = Car(5)
```

Attributes with default value
```python
# Sometimes when we are creating our attributes, we might want a default value to start with.
# Example: Instagram App
class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        # We don't need to set the follower amount each time we construct a new object from this class
        # all users will have a default value of 0


user_4 = User("004", "tim")
print(user_4.followers)  # output: 0
```
Note
###### If you don't define an __init__ function in your class, Python will use a default empty __init__ function for you. This default __init__ function doesn't do anything, but it still gets called when you create an object from the class.
***

### Creating Methods
```python
# Setting an attribute and later on changing it inside a function
class Car:

    def __init__(self):
        self.seats = 5
        
    # In Python, methods inside a class must include 'self' as the first parameter, which refers to the object the method is called on.
    def enter_race_mode(self):
        self.seats = 2


car = Car()
print(car.seats)  # the default value of seats is 5

car.enter_race_mode()  # the value of seats is changed after calling this function
print(car.seats)  # the value of seats has changed to 2, due to the `enter_race_mode` method
```
```python
class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "angela")
user_2 = User("002", "jack")

# Using the follow method
user_1.follow(user_2)
print(user_1.followers) # output: 0
print(user_1.following) # output: 1
print(user_2.followers) # output: 1
print(user_2.following) # output: 0
```
***

### Types of Casing
- PascalCase
###### The first letter of each word capitalized, no underscores used.
- camelCase - camelCasing
###### The first letter of the 1st word is lowercase, but every subsequent word has its first letter capitalized, no underscores used.
- snake_case
###### All the words are lowercase, but they're separated by an underscore.
- kebab-case
###### All the words are lowercase and separated by hyphens (dashes).
***

### References:
- *[Trivia Database](https://opentdb.com/)*
***
