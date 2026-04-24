# Day 10 - Calculator Program
A calculator program that performs continuous operations (+, -, *, /) and allows the user to keep calculating with the previous result or start over.


## Notes

### Functions with Outputs
###### A function with output in Python is a reusable block of code that (allows output), returns a value using the return statement.
```python
# Plain Functions
def new_function():
    print("Hello")
```
```python
# Functions with Inputs
def function(name, location):  # we have to define the arguments each time
    # for the parameters name and location
    print(f"Hello {name}\m You are at {location}")
```
```python
# Functions with Outputs
# They allow you to have an output once the function is completed (executed)
def my_function():
    result = 3 * 2
    # the output keyword is `return`
    # after the word `return` we put whatever we want to be the output of this function
    return result

# Calling a Function with Output
my_function()  # this line is going to be replaced by the result
output_1 = my_function()  # we can save it inside a variable
# output_1 = result
# output_1 = 6
```
***

Print() Function vs. Return Keyword
```python
# Simply, print is used for displaying output, while return is used for passing data back.

def format_name(f_name, l_name):  # two parameters
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    print(f"{formated_f_name} {formated_l_name}")

format_name("angela", "YU")

# ------------------ Same Output ------------------- #

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

# We are saving the output of the function inside a variable
formated_string = format_name("anGELA", "YU")
print(formated_string)  # output: 'Angela Yu'
print(format_name("anGELA", "YU"))  # output: 'Angela Yu'
```
***

Built-in Functions & Output
```python
# For example, the len() function takes an input and has an output.
num_of_char = len("Angela")
print(num_of_char)  # output: 6

# when this built-in function runs (calculating the number of letters inside the input)
# is going to return the result as an output
# and this output is going to replace this part of the code, becoming:
num_of_char = 6
```
***

Function Output as Input
```python
def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_2(function_1("hello"))
print(output)  # output: Hellohello
```
***

### title() Method
###### The title() method returns a string with the first letter of each word capitalized and the rest in lowercase --> title case.
```python
# Title case means that the first letter of each word is capitalized, except for certain small words, such as articles and short prepositions.
# Syntax:
# str.title()
print("they're bill's friends from the UK".title())  # output: 'They'Re Bill'S Friends From The Uk'

name = "anGela yu"
name_title_case = name.title()
print(name_title_case)  # output: 'Angela Yu'
```
***

### Return Statement (detailed)
###### The return statement immediately exits a function, so any code after return inside the function will not be executed.
```python
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
        # if there isn't anything after the keyword `return` it prints out None (empty return)
        # so, the return statement can be used just to exit a function (early exit)
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    f"Result: {formated_f_name} {formated_l_name}"  #  a warning will appear

# Storing output in a variable
formatted_name = format_name(input("Your first name: "), input("Your last name: "))
print(formatted_name)
# or printing output directly
print(format_name(input("What is your first name? "), input("What is your last name? ")))
```
***

### Multiple Return Values
###### A function can return multiple values at once by separating them with commas. These values are returned as a tuple and can be unpacked into separate variables.
```python
def format_name(f_name, l_name):
    """Take a first and last name and format it
    to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."  # Return as an early exit
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"
```
***

### Docstrings - Documentation for our Functions
###### A docstring is a short description written inside triple quotes that explains what a function, class, or module does. It serves as built-in documentation.
```python
# For example, the built-in len() function of Python "Return the number of items in a container."

# the docstring has to go after the first line (after the declaration), at the first indented block
def format_name(f_name, l_name):
    """Take a first and last name and format it
    to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    return f"Result: {f_name.title()} {l_name.title()}"
```
Multi-line Comments
```python
# With docstrings we can write strings that are multi-line --> multi-line comments
"""
So,we can also use this to write a multi-line comment,
this will be interpreted as a comment.
"""
```
***

### Recursion
###### Recursion is a programming technique where a function calls itself in order to solve a problem, and stops when it reaches a base case.
###### The base case is the condition that tells the recursive function when to stop. Without it, the function would call itself forever.
###### A stack overflow happens when a function keeps calling itself without stopping, using up all memory and crashing the program.
```python
# In this example below, the calculate_sum function recursively calculates the sum of numbers from 1 to n.
# The base case is when n is 1, in which case it returns 1.
# Otherwise, it returns the sum of n and the sum of numbers from 1 to n-1.
def calculate_sum(n):
    if n == 1:   # base case
        return 1
    else:
        return n + calculate_sum(n - 1)

result = calculate_sum(5)
print(result)  # Output: 15
```
```python
# Although, we should be careful to use a function inside this function ONLY under a condition.
# Otherwise: It becomes an infinite loop
def calculator():
    print("123")
    calculator()

calculator()
```
***

### Flags in Python
###### A flag is a variable that signals if a condition is true or false (boolean variables), helping control the program’s flow.
```python
# Setting a variable as True or as False, to use it later as a condition
# (mostly in while loops or if/elif/else statements)
start_over = False
while not start_over:
    num = int(input("pick a number "))
    if num > 10:
        start_over = True
        print("End")
# The program is going to run (and asking us to provide a number) until we type a number that is greater than 10
# Then it prints 'End' and the loop stops
```
***

### Assigning a Function to a Variable
###### Giving a function a new name using a variable, so you can call it using that variable name. This allows for flexible and dynamic use of functions.
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Store functions in a dictionary
operations = {
    '+': add,  # we don't need the parentheses (), because we aren't using the function just storing it
    '-': subtract,
}

# Access a function by symbol and call it
op = operations['+']  # otherwise: operations["+"](10, 4)
print(op(10, 4))  # Output: 14

# Assign a function to a variable directly
operation = add
print(operation(5, 3))  # Output: 8

# Reassign to another function
operation = subtract
print(operation(5, 3))  # Output: 2
```
***