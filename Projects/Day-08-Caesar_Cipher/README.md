# Day 8 - Caesar Cipher
A program that encrypts or decrypts messages using the Caesar cipher technique, shifting letters by a user-specified number.

<img width="800" height="641" alt="day-08-project" src="https://github.com/user-attachments/assets/99d95567-2669-4676-88dc-1d7b52009aa7" />

## Notes

### Functions with Inputs
###### A function with inputs lets you pass data into the function so it can use it when running.
```python
# A function that accepts an input and uses it inside the function body.
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

# It requires an argument for the variable `name`
# Otherwise, if we call the function without an input, we get a TypeError.
greet_with_name("Angela")  
greet_with_name("Billie") # output: 'Hello Billie\nHow do you do Billie?'
```
***

### Parameters & Arguments
###### A parameter is a variable in the function definition that acts as a placeholder for the value that will be passed to the function.
###### An argument is the actual value you pass to the function when you call it. It is assigned to the corresponding parameter.
```python
# `name` is a parameter in the function definition
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

# "Angela" and "Billie" are arguments passed to the function
greet_with_name("Angela")
greet_with_name("Billie")
```
***

### Positional vs. Keyword Arguments
###### Positional arguments are passed to a function in the exact order the parameters are defined. The position of each argument matters.
###### Keyword arguments are passed by explicitly naming each parameter, so the order doesn’t matter (this way you can skip optional parameters).
```python
# Functions with more than one input --> two parameters (name and location)
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

    
# POSITIONAL ARGUMENTS (default way)
greet_with("Jack Bauer", "Nowhere")  # output: 'Hello Jack Bauer\nWhat is it like in Nowhere?'
greet_with("Nowhere", "Jack Bauer")  # output: 'Hello Nowhere\nWhat is it like in Jack Bauer?'
# The first argument get assigned to the first parameter and the second argument gets assigned to the second parameter.

# KEYWORD ARGUMENTS (Named Arguments)
greet_with(location="Nowhere", name="Jack Brauer")
# A keyword argument is preceded by a parameter and the assignment operator (=)
```
***

### count() Method
###### .count() is a string or list method that returns the number of times a specified value appears within the string or list.
```python
print("Hello".count("e"))  # output: 1

score = "love score"
print(score.count("o"))  # output: 2
```
***

### index() Method 
###### The index() method returns the position (index) of the first occurrence of a specified value in a list or string. If the value isn't found, it raises a ValueError.
```python
list_of_char = ["a", "v", "o", "c", "a", "d", "o"]  # Alternatively, list_of_char = "avocado"
print(list_of_char.index("a"))  # output: 0 (the position of "a" only at the first occurrence)
# the return value is only the first occurrence of the item in the list, the rest of the occurrences are not returned.
```
***

### math.ceil() & math.floor() Methods
###### math.ceil(x): Rounds a number upward to the nearest whole number (integer), if necessary, and returns the result.
###### math.floor(x): Rounds a number downward to the nearest whole number (integer), if necessary, and returns the result.
```python
# Import math library
import math

print(math.ceil(1.4))     # Output: 2
print(math.ceil(-5.3))    # Output: -5
print(math.ceil(22.6))    # Output: 23
print(math.ceil(10.0))    # Output: 10

print(math.floor(0.6))    # Output: 0
print(math.floor(-5.3))   # Output: -6
print(math.floor(22.6))   # Output: 22
print(math.floor(10.0))   # Output: 10
```
***
