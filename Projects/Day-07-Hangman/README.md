# Day 7 - Hangman Game
A classic hangman game where the user chooses difficulty, guesses letters, and tries to reveal the hidden word before running out of lives.


## Notes

### Flow chart Programming
###### A flowchart is a diagram that shows the steps of a process in order, using symbols. (represents the logic of our program)
***

### Using Variables Inside and Outside Loops
###### When a variable is defined inside a for or while loop in Python, and used outside the loop, it retains the value it had after the last loop iteration.
```python
letter = ""
for n in range(0, 5):
    letter = n
print(letter)
# After the loop ends, letter holds the value 4, which is the last value assigned during the loop.

game = "hangman"
for character in game:
    print(character)
# Each iteration gives you the next character in the string "hangman" (after the loop character = "n")
```
***

### How to import modules in Python (detailed)
###### In Python, the import statement lets you use code (functions, classes, variables) from external modules in your program.
1. Basic Import
```python
# Use the import keyword followed by the module name to import an entire module.
import collections

# You can access functions or classes in the module using dot notation:
collections.Counter()
```
2. Importing Specific Items from a Module
```python
# Use the `from` keyword to import specific classes, functions, or variables.
from math import pi

print(pi)  # Output: 3.141592653589793
```
3. Accessing Elements from a Custom Module
```python
# If you have a module like hangman_words with a list called word_list, you can access it like this:
# Import the whole module
import hangman_words
print(hangman_words.word_list)

# Or import specific items from the module
from hangman_words import word_list, stages
print(word_list)
```
4. Importing with an Alias
```python
# You can use the as keyword to give a module an alias for convenience:
import math as M
print(M.pi)  # Output: 3.141592653589793
```
***

### in & not in Keyword
###### The in keyword checks if a value exists within a sequence (like a list, string, tuple, or dictionary) and returns True if found, otherwise False.
###### The not in keyword checks if a value does not exist in a sequence and returns True if it’s absent.
```python
# Check if an item is in a list using `in` and `not in`
fruits = ['apple', 'banana', 'cherry']
print('banana' in fruits)  # Output: True
print('orange' in fruits)  # Output: False
print('orange' not in fruits) # Output: True

# Check if a character is in a string using `in` and `not in`
word = "hangman"
letter = "a"

if letter in word:
    print(f"'{letter}' is in the word!")
else:
    print(f"'{letter}' is NOT in the word.")
    
if 'z' not in word:
    print("'z' is not in the word!")  # gets printed --> the letter 'z' is not in the word
```
***
