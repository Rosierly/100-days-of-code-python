# Day 13 - Debugging Techniques (No Final Project)
A day focused entirely on learning and practicing different debugging strategies in Python — identifying, reproducing, and fixing bugs efficiently.

## Notes

### Debugging: the process of removing bugs from your code - Steps to identify the bug and solve it
- Describe the Problem
- Reproduce the Bug
- Play Computer
- Fix the Errors
- Print is Your Friend
- Use a Debugger
***

### Describe the Problem
###### Clearly explain what the code is supposed to do and what it’s doing wrong.
```python 
def my_function():
  for i in range(1, 20):  # The range goes from 1 to 19 (20 is not included)
    if i == 20:
      print("You got it")
          
my_function()

# ❌ The for loop iterates over numbers from 1 to 19.
# Since 20 is not included, the condition i == 20 is never True, so "You got it" is never printed.

# ✅ TO FIX IT: replace 20 with 21
for i in range(1, 21):
    if i == 20:
        print("You got it")
```
***

### Reproduce the Bug
###### Run the code in a way that consistently shows the bug happening.
```python
from random import randint

dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)  # returns a number from 1 to 6 (inclusive)
print(dice_images[dice_num])

# ❌ This can cause an IndexError:
# The list has 6 items, but list indexing starts at 0.
# So the valid indices are 0 to 5.
# If dice_num == 6, you'll get an IndexError: list index out of range.

# ✅ TO FIX IT: Use randint(0, 5) to generate a valid list index.
dice_num = randint(0, 5)  # returns a number from 0 to 5 (inclusive)
```
***

### Play Computer
###### Go through the code line by line manually to see where it goes wrong.
```python
year = int(input("What's your year of birth?"))

if 1980 < year < 1994:
  print("You are a millennial.")
elif year > 1994:
  print("You are a Gen Z.")

# ❌ What happens if the year is equal to 1994? --> nothing gets printed.
# That's because 1994 is not greater than 1994 (first condition),
# and there is no else clause to catch it.
    
# ✅ TO FIX IT:
# Use >= 1994 in the second condition to include the year 1994
# or add an else statement to handle all other cases.
```
***

### Fix the Errors
###### Find the root cause and correct the code logic or syntax.
```python
# ❌ Original buggy version:
age = input("How old are you? ")
if age > 18:
print("You can drive at age {age}.")

# ✅ Fixed version:
age = int(input("How old are you? "))
if age > 18:
    print(f"You can drive at age {age}.")

# 🐞 1st Bug: IndentationError
# Pay attention when the editor or the console is giving you an error/ warning.
# The print statement was not indented, so Python raised an IndentationError.
# All code inside an `if` block must be indented properly.

# 🐞 2nd Bug: TypeError
# The input was not converted to an integer.
# Comparing a string (`age`) to an integer (`18`) raises a TypeError.
# Remember: input() always returns a string!

# 🐞 3rd Bug: Literal string formatting
# The original print used "{age}" in a regular string, not an f-string.
# It printed the text "{age}" instead of the actual value.
# Use an f-string (f"...") to include variable values in strings.
```
try-except block
```python
# ❌ In our fixed code above, if the user enters something that isn't a number, int() raises a ValueError,
# and the program crashes, because our input can't be converted to an integer.

# ✅ TO FIX IT: Use a try-except block to catch the ValueError and handle it, so our code doesn't crush.
try:
    age = int(input("How old are you? "))  # possibly dangerous line of code --> may raise ValueError
except ValueError:
    print("You have typed in an invalid number. Please try again with a numerical response such as 15.")
    age = int(input("How old are you? "))  # give the user another chance
    
if age > 18:
    print(f"You can drive at age {age}.")
```
***

### Print is your Friend
###### Use print() statements to check the values of variables and program flow.
```python
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))  # Mistake here
total_words = pages * word_per_page
print(total_words)  # output: 0

# ❌ No matter what input we provide, total_words is always 0. WHY?
# That's because `word_per_page == int(...)` checks for equality instead of assigning a new value --> (this line becomes True or False)
# So the value of word_per_page stays 0, and total_words = pages * 0.

# ✅ TO FIX IT: Replace the double equal sign (==) with a single one (=) to assign the input correctly.
# Using print statements helps spot the issue by showing that word_per_page was still 0.
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))  # Correct assignment
total_words = pages * word_per_page
print(f"pages = {pages}")
print(f"word_per_page = {word_per_page}")
print(total_words)
```
***

### Use a Debugger
###### Step through the code using debugging tools to inspect how it runs and where it fails.
```python
def mutate(a_list):
  b_list = []
  new_item = None  # to avoid getting a warning later about the global variable `new_item`
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])

# ❌ The output is [26] instead of a new doubled list.
# Because .append() is outside the loop, only the last doubled item (13*2=26) gets added.

# ✅ TO FIX IT: Move the .append() call inside the loop to add every doubled item to the list.
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)  # Now correctly inside the loop
    print(b_list)
    
mutate([1, 2, 3, 5, 8, 13])
```
Thonny & Breakpoint
```python
# Debugger: pythontutor.com --> thonny

# What is Breakpoint and how to we use it in a Debugger? 
# Inside most debuggers you can put a breakpoint, which tells the computer to stop at this specific line of code.
# Then, at that moment we can examine what all the variables and functions are doing (what they are equal to, 
# at this specific moment we added the breakpoint).

# Using Breakpoint in Pycharm:
# You set a breakpoint by clicking in the gutter (the left margin) next to a line number.
# That line turns red, meaning the program will pause there when run in Debug mode.
#
# While paused, Pycharm lets you:
# Check variables & Evaluate expressions (in Threads & Variables, next to Console)
# Execute code step-by-step --> step over, into, or out of functions
#  - Step over: Executes the current line and moves to the next one, without going inside any function call.
#  - Step into: Goes inside a function to see what it does line by line.
#  - Step out: Finishes running the current function and goes back to where it was called. Exits the function.
#  - Step Into my Code: It's like Step Into, but it skips built-in/library code and only steps into your own functions.
# Continue (Resume running until the next breakpoint or end of the program) or stop program
#
# You can mute a breakpoint to execute the code completely and see the output in the console without removing it.
```
***