# Day 1 - Band Name Generator
A simple Python console program that generates a band name by combining the name of your hometown and your pet's name.

<img width="562" height="326" alt="day-01-project" src="https://github.com/user-attachments/assets/e1131fbd-2241-4712-9be5-7ff2062168e6" />

## Notes

### print() Function
###### Displays output or messages to the screen (console).
```python 
print("Hello world!")
```  
***

### Strings
###### They are pieces of text, always inside single or double quotes.
```python
"This is a string."
```
***

### String Concatenation
###### Combining different strings.
```python
print("Hello" + "Angela")  # output: 'HelloAngela' (without a gap)
# 3 Ways to add a gap (space) between two strings. 
print("Hello" + " " + "Angela")  # output: 'Hello Angela'
print("Hello " + "Angela")
print("Hello" + " Angela")
```
***

### How to add a new line - \n
```python
print("Hello world!\nHello world!")
print("Hello world!\nHello world!\nHello world!")
```
***

### Escape character - backslash \
```python
print("Flour \"is\" an ingredient")
```
***


### Variables
###### A variable stores a piece of data under a name so you can use or change it later.
```python
name = "Jack"
print(name)  # output: 'Jack'
name = "George"  
print(name)  # output: 'George'
```
***


### input() Function
###### Gives the user the ability to enter a piece of data (input) and extracts it. Place the prompt text inside the parentheses.
```python
name = input("What is your name? ")  # save it under the variable name
print("Hello" + name + "!") # output: 'Hello Angela!' (if user input --> Angela)
```
```python
# same output - other way
print("Hello" +  input("What is your name?") + "!") 
# we'll first see the prompt text of the input function in the console, then is going to be replaced in the code.
```
***

### len() Function
###### Returns the number of items of an object, a string (characters), list, or other iterable.
```python
print(len(input("What's your name? ")))
```
```python
# same output - more detailed solution
username = input("What's your name?")
length = len(username)
print(length)
```
***

### Variable Naming Rules
###### - Make sure your variable names are descriptive.
###### - You can use more than one words (user_name). DON'T USE SPACES BETWEEN WORDS.
###### - Don't start with numbers (len1, len2).
###### - Don't use special words like print or input.
###### - If you later on spell wrong a variable name or do a typo, you'll get a NameError.
***

### Name Error
###### NameError occurs when you try to use a variable or function name that hasn’t been defined yet.
```python
name = "Jack"
print(nama)  # ❌ NameError
# the name of the variable it's spelled wrong
```
***

### Syntax Error
###### A mistake in the code that breaks Python’s grammar rules, making it un-runnable.
```python
print("Hello world!)  # ❌ SyntaxError
# the second double quote is missing
```
***

### Index Error
###### Incorrect or inconsistent spacing (tabs or spaces), that breaks Python's required code structure.
```python
    print("Hello" + " Angela")  # ❌ IndexError
```
***

### Comments #
###### A line of text that is not being considered as code by the computer.
```python
# Use a hashtag or highlight a line and press Ctrl + / (Windows), Command + / (Mac) to comment it afterward.
```
***

