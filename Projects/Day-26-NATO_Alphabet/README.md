# Day 26 - The NATO Alphabet
A Python program that converts user input words into NATO phonetic code words using a CSV-based lookup table.


## Packages used:
- pandas → data manipulation and analysis library for working with structured (tabular) data using DataFrames

## Notes

### Basic List Comprehensions
###### List comprehensions are a shorter way to create new lists from existing sequences. They are often used instead of for loops when building lists.
###### A sequence is an ordered collection of items, such as a list, string, tuple, or range. List comprehensions iterate through these items in order.
```python
# Syntax:
new_list = [new_item for item in iterable]
```
```python
numbers = [1, 2, 3]

# Creating a List with a Traditional for Loop
new_list = []
for n in numbers:
    add_1_num = n + 1
    new_list.append(add_1_num)

# Creating a List with List Comprehension
new_list = [n + 1 for n in numbers]

print(new_list)  # output: [2, 3, 4]
```

List Comprehensions with Strings
```python
name = "Angela"

# The comprehension iterates through each character in the string and stores it as an item in a new list.
letters_list = [letter for letter in name]

print(letters_list)  # output: ['A', 'n', 'g', 'e', 'l', 'a']
```

List Comprehensions with `range()`
```python
range_list = [n * 2 for n in range(1, 5)]

print(range_list)  # output: [2, 4, 6, 8]
```
***

### Conditional List Comprehensions
###### You can add an if statement to filter items while creating the list.
```python
# Syntax:
new_list = [new_item for item in iterable if condition]
```
```python
# ================================ Example: Filtering ================================
names = ["Alex", "Beth", "Carolina", "Dave", "Eleanor", "Freddie"]

short_names = [name for name in names if len(name) <= 4]

print(short_names)  # output: ['Alex', 'Beth', 'Dave']

# ========================== Example: Transforming + Filtering ==========================

# Create a new list containing names longer than 5 characters in ALL CAPS.
long_names = [name.upper() for name in names if len(name) > 5]

print(long_names)  # output: ['CAROLINA', 'ELEANOR', 'FREDDIE']
```
***

### Basic Dictionary Comprehensions
###### A dictionary comprehension is a shorter way to create dictionaries in Python.

Creating a Dictionary from an Iterable (List)
```python
# Syntax:
new_dict = {new_key: new_value for item in iterable}
```
```python
import random

names = ["Alex", "Beth", "Carolina", "Dave", "Eleanor", "Freddie"]

student_scores = {
    student: random.randint(1, 100)
    for student in names
}

print(student_scores)
# Output:
# {
#     'Alex': 78,
#     'Beth': 45,
#     'Carolina': 91,
#     'Dave': 62,
#     'Eleanor': 34,
#     'Freddie': 88
# }
```

Creating a Dictionary from Another Dictionary
```python
# Syntax:
new_dict = {
    new_key: new_value
    for (key, value) in dict.items()
}
```
```python
student_scores = {
    "Alex": 78,
    "Beth": 45,
    "Carolina": 91
}

uppercase_students = {
    name.upper(): score
    for name, score in student_scores.items()
}

print(uppercase_students)
# Output:
# {
#     "ALEX": 78,
#     "BETH": 45,
#     "CAROLINA": 91
# }
```
***

### The `dict.items()` Method
###### It's a built-in method that returns all key-value pairs in a dictionary as tuples (key, value), which can be unpacked into separate variables.
```python
student_scores = {
    "Alex": 78,
    "Beth": 45,
    "Carolina": 91
}

print(student_scores.items())
# Output:
# dict_items([
#     ('Alex', 78),
#     ('Beth', 45),
#     ('Carolina', 91)
# ])

# Returns a view object containing all key-value pairs.
# Each key-value pair is represented as a tuple.
# Commonly used in loops and dictionary comprehensions.
```
Example in a Loop
```python
for student, score in student_scores.items():
    print(student, score)
    # Output:
    # Alex 78
    # Beth 45
    # Carolina 91
```
***

### Conditional Dictionary Comprehensions
###### Creating a dictionary while filtering items using an if condition during iteration.
```python
# Syntax:
new_dict = {
    new_key: new_value
    for (key, value) in dict.items()
    if condition
}
```
```python
passed_students = {
    student: score
    for (student, score) in student_scores.items()
    if score >= 60
}

print(passed_students)
# Output:
# {
#     'Alex': 78,
#     'Carolina': 91,
#     'Dave': 62,
#     'Freddie': 88
# }
```
***

### Iterating Over a Pandas DataFrame
###### Looping through a DataFrame to access and process its data row-by-row or column-by-column using methods like `.items()` and `.iterrows()`
Create DataFrame
```python
import pandas

students_dict = {
    "students": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_df = pandas.DataFrame(students_dict)
print(student_df)
# Output:
#   students  score
# 0   Angela     56
# 1    James     76
# 2     Lily     98
```

DataFrame Iteration with `.items()` (Column-wise)
```python
for key, value in student_df.items():
    print(key)    # column name
    print(value)  # column data (Series)
    
# This loops through columns, not rows
# Each value is a Pandas Series
```

DataFrame Iteration with `.iterrows()` (Row-wise)
```python
for index, row in student_df.iterrows():
    print(index)  # row index
    print(row)    # full row as a Series

# Each row is a Pandas Series object
# You can access columns like attributes:

for index, row in student_df.iterrows():
    print(row.students)
    print(row.score)
```

Filtering Rows While Iterating
```python
for index, row in student_df.iterrows():
    if row.students == "Angela":
        print(row)
        # Output:
        # students    Angela
        # score           56
        # Name: 0, dtype: object
```

Dictionary Comprehension from DataFrame
```python
# You can build a new dictionary from a DataFrame:
new_dict = {
    row.students: row.score
    for index, row in student_df.iterrows()
}
# Result:
# {
#     "Angela": 56,
#     "James": 76,
#     "Lily": 98
# }
```
***
