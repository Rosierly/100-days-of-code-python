# Day 2 - Tip Calculator
A simple Python console program that calculates how much each person should pay when splitting a bill, including tip.

<img width="800" height="289" alt="day-02-project" src="https://github.com/user-attachments/assets/525d32b4-a053-4df4-91f2-b367f73421f4" />


## Notes

### Data Types
###### Data Types are categories of data that tell the computer what kind of value is being stored or processed, such as numbers, text, or boolean values.
***
String
###### A string is a sequence of characters enclosed in quotes, used to represent text.
```python
print("Hello")
"123"  # as long as it's inside quotes, it's considered a string
print("123" + "345")  # concatenation --> output: '123345'
```
***
Integer
###### An integer is a whole number (without any decimal places).
```python
print(123 + 345)  # output: 468
```
```python
# Large Integers (123,456,789 --> replacing commas with underscores)
print(123_456_789)  # output: 123456789
```
***
Float = Floating Point Number
###### A number that has decimal places.
```python
print(3.14159)
```
***
Boolean
###### A data type with only two possible values: True or False.
```python
print(True)
print(False)
```
***

### Subscripting
###### A method of pulling out a particular element from a string.
```python
# Note: counting always starts from zero
print("Hello"[0])  # output: 'H' (we get the first character of this string)
print("Hello"[4])  # output: 'o'

# Negative indices count from the end of the string.
print("Hello"[-1]) # output: 'o'

# Spaces count as characters too
street_name = "Abbey Road"
print(street_name[4] + street_name[7])  # output: 'yo'
```
***

### Type Error
###### A TypeError happens when you use a value with the wrong type for a function or operation.
```python
print(len(12345))   # ❌ TypeError
# This function requires a sized object (str, list, tuple, dictionary, set, range, etc.)
# Does not accept int, float, bool, None (there are not sized) --> will raise a TypeError
```
***

### Type Checking
###### There's a function that allows us to check the data type of any piece of data.
```python
print(type("abc")) # output <class 'str'>
print(type(1234))  # output <class 'int'>
print(type(3.14))  # output <class 'float'>
print(type(True))  # output <class 'bool'>
```
***

### Type Conversion
###### Converting a value from one data type to another. It's also known as Type Casting in Python.
```python
# Converting the strings into actual numbers, and doing the mathematical operation.
print(int("123") + int("456"))  # output: 579

# Type Conversion Functions
int()
float()
str()
bool()
```
```python
# Example Exercise:
name_of_the_user = input("Enter your name: ")
length_of_name = len(name_of_the_user)

print(type("Number of letter in your name: "))  # output: <class 'str'>
print(type(length_of_name))  # output: <class 'int'>

print("Number of letter in your name: " + str(length_of_name))
```
***

### Value Error
###### A ValueError happens when a value is the right type but has invalid content for an operation.
```python
# Sometimes you can't convert things into a different data type. Example:
print(int("abc"))   # ❌ ValueError
```
***

### Mathematical Operations
Addition
```python
print(123 + 456)
```
Subtraction
```python
print(7 - 3)
```
Multiplication
```python
print(3 * 2)
```
Division
```python
# REGULAR DIVISION --> returns a float
print(6 / 3)  # output: 2.0
print(type(6 / 3))  # output: <class 'float'>
# You always end up with a floating point number, even if the division is clean.
# This is called implicit typecasting, python is converting the result into a float.
```
```python
# FLOOR DIVISION (//)  --> returns an integer
print(6 // 3)  # output: 2
print(type(6 // 3))  # output: <class 'int'>
```
```python
# Example with Non-Clean Division
print(5 / 3)   # output: 1.6666666666666667
print(5 // 3)  # output: 1
# Behind the scenes, it's doing the division and then just removing all the decimal places.
```
Exponent (raise a number to a power)
```python
print(2 ** 3)  # output: 8
```
***

### PEMDAS(LR)
###### There's a certain level of priority for doing more than one mathematical operation in the same line of code.
```python
# Parentheses ()
# Exponents **
# Multiplication & Division * /
# Addition & Subtraction + -

# always left to right
```
```python
print(3 * 3 + 3 / 3 - 3)  # output: 7.0
print(3 * (3 + 3) / 3 - 3)  # output: 3.0
```
***

### How to Round a Number - Round function()
```python
# Round function()
print(round(3.9))  # output: 4
print(round(3.3))  # output: 3

# BMI
bmi = 84 /1.65 ** 2
print(bmi)  # output: 30.86053412462908
print(round(bmi))  # output: 31

# The Round function takes two inputs (number,ndigitis: number of digits)
print(round(bmi, 2))  # output: 30.85
```
```python
# Converting a float into an integer: 
bmi = 84 /1.65 ** 2
print(bmi)  # output: 30.86053412462908
print(int(bmi))  # output: 30 --> it floors the number
# Flooring a number: a programming term for removing all decimal places
```
***

### Assignment Operator
###### Assignment operators are used to assign or update values in variables.
```python
score = 0 # basic assignment 
# User points a score 
score = score + 1  # reassignment
score += 1  # shorthand assignment

# -= for subtraction
# *= for multiplication
# /= for division
# %= for modulus
```
***

### F-Strings (formatted string literals)
###### F-Strings help us put different data types inside strings using curly braces {}.
```python
score = 0
height = 1.8
is_winning = True
print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}.")
```
***
