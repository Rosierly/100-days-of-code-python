# Day 3 - Treasure Island Game
A text-based adventure game where the player makes choices to find the treasure.

<img width="800" height="495" alt="day-03-project" src="https://github.com/user-attachments/assets/ea606887-8437-4334-bf0e-253d96d75eb7" />

## Notes

### Conditional if / else statement
###### If-else statements let a program choose what to do based on whether a condition is true or false.
```python
# Bathtub overflow
water_level = 50
if water_level > 80:
    print("Drain water")
else:
    print("Continue")
```
```python
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

# Be careful with the keywords if/else, colons and indentations!
if height >= 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry, you have to grow taller before you can ride.")
```
*** 

### Operator
###### An operator is a symbol in programming that has a specific function.
*** 

### Comparison Operators
###### Comparison operators are used to compare two values and return True or False based on the result.
```python
# >    Greater than
# <    Less than
# >=   Greater than or equal to
# <=   Less than or equal to
# ==   Equal to
# !=   Not Equal to
```
Assignment vs Equality Operators
```python
#  =   (one equal sign)    assign a value to a variable
#  ==  (two equal signs)   checking equality
```
***

### Modulo Operator (%)
###### The modulo operator (%) gives us (returns) the remainder after dividing one number by another.
```python
# When a division is clean --> no remainder:
print(10 % 5)  # output: 0 (10÷5=2)
print(9 % 3)  # output: 0  (9÷3=3)

# When a division is not clean (has decimal places) --> the modulo shows the leftover part:
print(10 % 3)  # output: 1 (10÷3= 3.3333333333333333...) or (10÷3= 3 with 1 remaining)
print(15 % 4)  # output: 3 (15÷4= 12 with 3 remaining)
```
```python
# Use the modulo to check evenness (if a number is even or odd)
number = int(input("What is the number you want to check? "))
if number % 2 == 0:  # if the number divides cleanly with 2 is even (no remainder)
    print("That's an even number.")
else:
    print("That's an odd number.")
```
***

### Nested if / else statements
###### Nested if-else means putting one if-else inside another to check more specific conditions (conditions within conditions).
### If / elif / else statement
###### An if-elif-else statement checks multiple conditions (at the same level), and runs only the first block where the condition is true, skipping the rest.
```python
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")
```
***

### Multiple If Statements in Succession
```python
# Multiple if: all conditions are checked independently, all true conditions run
# if condition1:
#   do A
# if condition2:
#   do B
# if condition3:
#    do C
```
```python
# if-elif-else:  ensures only one block runs --> only the first true condition runs, the rest are skipped.
# if condition1:
#   do A
# elif condition2:
#   do B
# else:
#    do C
```
```python
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif 45 <= age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")  # free tickets
    else:
        bill = 12
        print("Adult tickets are $12.")
        
    # Check regardless of the price of the ticket, if the user wants a photo.
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
        
    print(f"Your final bill is ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")
```
***

### Logical Operators
###### Logical operators are symbols used to combine or compare boolean values, returning True or False based on logical relationships. 
###### They let us check multiple conditions in a single line of code.
```python
# A and B   → Both conditions must be True
# C or D    → At least one must be True
# not E     → Reverses the condition (True becomes False)

# Example:
False or True or False  # → True
# Explanation: Evaluates from left to right → (False or True) → True → (True or False) → True
# The `or` operator returns True if at least one value is True.
```
```python
age = 16
has_id = True

# Check if the person is allowed entry
if age >= 18 and has_id:  # False and True --> False
    print("Access granted.")
else:
    print("Access denied.")
```
```python
age = int(input("What is your age? "))

# Both if statements check whether the user's age is between 45 and 55, inclusive.
if age >= 45 and age <= 45:
    pass
if 45 <= age <= 55:  # preferred way
    print("Everything is going to be ok. Have a free ride on us!")  # free tickets
```
***

### lower() & upper() method
###### lower() and upper() are string methods that convert all letters in a string to lowercase or uppercase and return it. (they take no argument)
```python
print("Hello".lower())  # output: 'hello'
print("Hello".upper())  # output: 'HELLO'
```
***

### Triple quotes 
###### To include multi-line strings in our code, docstrings (multi-line comments - documentation), we use triple quotes: ' ' ' or  " " "
###### For ASCII art we use only single triple single quotes: ' ' ' 
***
