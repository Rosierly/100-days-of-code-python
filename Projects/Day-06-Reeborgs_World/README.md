# Day 6 - Reeborg's World
Guide a robot through a maze using conditional logic and loops to reach the goal by following the right-hand rule: [Reeborg's World - Maze Challenge](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json)


## Notes

### Functions
###### A function is a reusable block of code that performs a specific task, can accept inputs (parameters) and optionally return a result.
```python
# Build-in Python Functions
num_char = len("Hello")  # len() functions gives us the number of items in a collection
print(int("9"))  # print() & int() function
```
```python
# Defining a Function
def my_function():
    print("Hello")
    print("Bye")

# Calling a Function
my_function()
```
***

### Indentation
###### Indentation in Python is the use of spaces (or tabs) to define the structure and grouping of code blocks, (like inside loops, functions, conditionals, etc.).
```python
# Python’s default indentation is 4 spaces = 1 tab (a single indent)
# PEP 8, Python's style guide, recommends using spaces, not tabs.
# Python 3 disallows mixing the use of tabs and spaces for indentation (it'll throw an error)
# Most code editors let you: Choose spaces vs tabs & Set the indentation size (ex. 4 spaces whenever you press the Tab key)

def my_function():
    if True:                # Indented 4 spaces (inside function)
        print("HELLO")      # Indented 8 spaces (inside if block)

my_function()  # Not indented — it's outside the function block
```
***

### While Loops
###### A while loop repeatedly executes a block of code as long as a given condition is true. When the condition becomes false, the loop stops.
```python
# Basic Syntax
while condition:
    # Code to repeat
```
```python
tasks_left = 6
while tasks_left > 0:
    tasks_left -= 1
    print(f"Tasks remaining: {tasks_left}")
# The loop stops when all tasks are done (tasks_left reaches zero).

def is_done():
    # Imagine this function checks if a task is finished
    return False  # For now, always returns False to keep looping


while not is_done():  # SAME --> while is_done() != True:
    print("Working on the task...")
# This means: keep working while the task is NOT done, returns False
```
***

### Infinite Loop
###### An infinite loop is a while loop that its condition never becomes false, so it never ends.
```python
# Example
while 5 > 3:
    print("Hello")
# This loop runs forever because 5 > 3 (5 greater than 3) is always true.
```
```python
# How to debug an infinite loop - Tip
while 5 > 3:
    print(5 > 3)  # Output: True (repeated forever
# You can print out the condition of the loop to see if it ever changes.
```
***

### Difference between For Loops & While Loops
###### A for loop is used to iterate over a sequence of items (like lists, strings, or ranges).
###### A while loop is used to repeatedly execute a block of code while a condition is true.
***

### Two uses of For Loops (we've seen)
######
```python
# Looping through each item in an iterable (like a list)
for item in list_of_items:
    # Do something to or with each item

# Looping through a sequence of numbers using range()
for number in range(a, b):
    print(number)
```
***
