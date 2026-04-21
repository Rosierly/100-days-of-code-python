# Day 4 - Rock Paper Scissors Game
A simple rock-paper-scissors game where the user plays against the computer.

<img width="800" height="621" alt="day-04-project" src="https://github.com/user-attachments/assets/70690211-e77c-408f-a749-683d2dc36f53" />

## Notes

### Randomisation
###### It's a concept that introduces unpredictability, often used to build games or simulations where outcomes need to vary each time.
***

### Random module
###### The random module is used to make random choices, like picking items from lists, shuffling data, or generating random numbers.
random.randint()
```python
import random  # To use the random module we have to import it first.

# Generate and return a random integer between a and b (inclusive both),  a <= X <= b
random_integer = random.randint(1, 10)
print(random_integer)  # output: 7 (a number between 1 and 10, inclusive)
```
random.random()
```python
import random

# Generate and return a random floating point number between [0.0 to 1.0) - 1.0 not inclusive,  0.0 <= X < 1.0
random_number_0_to_1 = random.random()  # takes no arguments
print(random_number_0_to_1)  # output: 0.5100471938316743 (a float number between 0.0000000 - 0.99999999......)

# Extent the range
random_number_0_to_10 = random.random() * 10
print(random_number_0_to_1)  # output: 3.2287801394552442 (a float number between 0.00000000 - 9.9999999......)
```
random.uniform()
```python
import random

# Generate and return a random floating point number between a and b (inclusive both),  a <= X <= b
random_float = random.uniform(1, 10)
print(random_float)  # output: 9.8793265337558 (a float number between 0.00000000 - 10.0)
```
***

### Modules - How can we create our own?
###### Modules are files that contain reusable code — like functions, classes, or variables — that you can import into other programs-files.
my_module.py
```python
# Content of this python file
my_favourite number = 3.1415
```
main.py
```python
# 1st Way
import my_module

print(my_module.my_favourite_number)  # output: 3.1415
```
```python
# 2nd Way
from my_module import my_favourite_number

print(my_favourite_number)  # output: 3.1415
```
***

### Lists
###### A list is an ordered, changeable collection of items, even of different types (e.g., numbers, strings, or other lists), enclosed in square brackets [ ]
```python
# Syntax
fruits = ["Cherry", "Apple", "Pear"]
```
```python
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", 
                     "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee",
                     "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", 
                     "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada",
                     "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", 
                     "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# Indexing (between the square brackets we put the number of offset/ index we want)
print(states_of_america[0])  # output: 'Delaware'
print(states_of_america[2])  # output: 'New Jersey'

# Negative Indexing
print(states_of_america[-1])  # output: 'Hawaii'  (last item of the list --> index: -1)
print(states_of_america[-3])  # output: 'Arizona'
```
***

### Changing an Item in a List
```python
states_of_america[1] = "Pencilvania"
print(states_of_america[1])  # output: 'Pencilvania'
```
***

### List append() Method
###### Adds a single item to the end of a list.
```python
# Append Method - list.append(x)
states_of_america.append("Angelaland")
```
***

### List extent() Method
###### Adds all items from another list (or iterable) to the end of the list.
```python
# Extend Method - list.extend(iterable)
states_of_america.extend(["Angelaland", "Jack Bauer Land"])
```
***

### Selecting a Random Item from a List Using the len() Function and Indexing
```python
import random

fruits = ["Cherry", "Apple", "Pear"]

# Use len(list) to get the number of items in a list.
print(len(fruits))  # output: 3

# List indexing starts at 0, so the last item’s index is len(list) - 1.
random_index = random.randint(0, len(fruits) - 1) 

random_fruit = fruits[random_index]
print(random_fruit)  # output: Random fruit from the list (ex.'Apple')
```
***

### Selecting a Random Item with random.choice()
###### random.choice() returns a random item from a list or any other sequence (like a string, tuple or range).
```python
import random

fruits = ["Cherry", "Apple", "Pear"]
print(random.choice(fruits))  # Output: Random fruit from the list

x = "WELCOME"
print(random.choice(x))  # output: Random character from the string:
```
***

### IndexError: List Index Out of Range
###### This error occurs when you try to access a list index that doesn’t exist, outside the valid range of the list (from 0 to len(list) - 1).
```python
my_list = [10, 20, 30]
print(my_list[3])  # ❌ IndexError: list index out of range
```
***

### Nested Lists
###### A nested list is a list that contains other lists as its elements.
```python
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]  # nested list
print(dirty_dozen)  # output: [["Strawberries", "Nectarines", "Apples", ...],["Spinach", "Kale", ...]]

print(dirty_dozen[0])  # output: ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
print(dirty_dozen[1])  # output: ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

print(dirty_dozen[1][0])  # output: 'Spinach'
print(dirty_dozen[0][2])  # output: 'Apples'
```
***

### List index() Method
###### Returns the index (position) of the first occurrence of a specified value in a list. Indexing starts at 0.
```python
fruits = ['apple', 'banana', 'cherry']
print(fruits.index('cherry'))  # Output: 2

numbers = [4, 55, 64, 32, 16, 32]
print(numbers.index(32))       # Output: 3  (first occurrence)
```
***

### String split() Method
###### Splits a string into a list of substrings based on a specified separator. By default, splits on whitespace.
Basic Usage
```python
txt = "welcome to the jungle"
print(txt.split())  # Output: ['welcome', 'to', 'the', 'jungle']
```
Using a custom seperator
```python
txt = "hello, my name is Peter, I am 26 years old"
print(txt.split(", "))  # Output: ['hello', 'my name is Peter', 'I am 26 years old']

txt = "apple#banana#cherry#orange"
print(txt.split("#"))   # Output: ['apple', 'banana', 'cherry', 'orange']
```
split(seperator, maxsplit)
```python
# maxsplit (optional) limits the number of splits performed. Default is -1 (split all occurrences).
txt = "apple#banana#cherry#orange"
print(txt.split("#", 1))  # Output: ['apple', 'banana#cherry#orange']
```
***

### String strip() Method
###### A string method that removes whitespace (or specified characters) from the beginning and end of a string. It does not affect characters in the middle.
```python
# NO ARGUMENT
# By default, if you don’t pass any argument to strip(), it removes all kinds of whitespace characters from the start and end of a string.
# Whitespace characters include: spaces ' ', tabs '\t', newlines '\n', and others like carriage returns
text = "   Hello, World!   "
clean_text = text.strip()
print(clean_text)  # Output: 'Hello, World!'
```
```python
# WITH ARGUMENT
# If you pass a string argument, it will remove all characters in that string from both ends:
# It strips all x and y characters from the start and end until it finds a character not in "xy".
txt = "xyxxyHello World!yxyx"
print(txt.strip("xy"))  # Output: 'Hello World!'
```
***
