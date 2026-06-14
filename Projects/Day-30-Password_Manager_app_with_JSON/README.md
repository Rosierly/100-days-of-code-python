# Day 30 - Password Manager App with JSON
An improved GUI-based password manager that generates, stores, and retrieves secure credentials using a JSON file and clipboard support.


## Update the NATO Alphabet Converter project (Day 25) by adding exception handling.

### Packages used (only for NATO Alphabet Converter):
- pandas → data manipulation and analysis library for working with structured (tabular) data using DataFrames

## Notes

### Common Python Errors (Exceptions)

`FileNotFoundError`
###### Occurs when you try to open a file that does not exist.
```python
with open("a_file.txt") as file:
    file.read()
# Cause: a_file.txt cannot be found in the current folder.
```

`KeyError`
###### Occurs when trying to access a dictionary key that does not exist.
```python
a_dictionary = {"key": "value"}
value = a_dictionary["non_existent_key"]
# Cause: The key "non_existent_key" is not inside the dictionary.
```

`IndexError`
###### Occurs when trying to access a list index that is out of range.
```python
fruit_list = ["Apple", "Banana", "Pear"]
fruit = fruit_list[3]
# Cause: The list has indices 0, 1, and 2, so index 3 does not exist.
```

`TypeError`
###### Occurs when performing an operation with incompatible data types.
```python
text = "abc"
print(text + 5)
# Cause: A string cannot be added to an integer.
```
***

### Exception Handling in Python (`try`, `except`, `else`, `finally`)
###### Python uses four keywords to handle errors safely and prevent program crashes: `try`, `except`, `else`, `finally`.
```python
try:
    # Contains code that might raise an exception (cause an error)
except SomeError:
    # Runs only if a specific exception occurs (handles the error)
else:
    # Runs only if no exceptions occurred in the try block
finally:
    # Runs no matter what happens (error or no error)

# Notes
# Errors in Python are called exceptions.
# Use try to test code that may fail.
# Handle expected errors with specific except blocks.
# Avoid a bare except: whenever possible.
# Use else for code that should run only when the try block succeeds.
# Use finally for cleanup tasks like closing files, releasing resources, cleanup operations.
```

Example: Handling Multiple Exceptions
```python
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    value = a_dictionary["non_existent_key"]

except FileNotFoundError:
    # Create the file if it doesn't exist
    file = open("a_file.txt", "w")
    file.write("Something")

except KeyError as error_message:
    # Access the error message that was generated from that exception
    print(f"The key {error_message} does not exist.")  # output: The key 'non_existent_key' does not exist.

else:
    # Runs only when no exceptions occur
    contents = file.read()
    print(contents)

finally:
    # Always runs
    file.close()
    print("File was closed.")
```
***

### Raising Exceptions - `raise` keyword
###### Manually triggers an exception when an invalid or logically impossible condition occurs, optionally with a custom error message.
```python
# ======================= Example 1: Validating User Input =======================
height = float(input("Height: "))
weight = int(input("Weight: "))

# Check if the height value is realistic
if height > 3:
    raise ValueError("Human height should not be over 3 meters.")  # stops the program with a custom error message
    # The code after raise does not execute

# BMI is only calculated if the height is valid
bmi = weight / height ** 2
print(bmi)

# ====================== Example 2: Raising an Exception Manually ======================
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    value = a_dictionary["non_existent_key"]

except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")

except KeyError as error_message:
    print(f"The key {error_message} does not exist.")

else:
    contents = file.read()
    print(contents)

finally:
    # Runs no matter what happens
    # We can manually raise our own exception
    raise TypeError("This is an error that I made up.") 
# Even if no error occured in the `try` block, `raise TypeError()` creates a new exception.
```
***

### JSON (JavaScript Object Notation)
###### JSON is a lightweight data format used for storing and transferring data. It is similar to Python dictionaries and uses key-value pairs.

Write JSON Data (`json.dump`)
```python
import json

new_data = {
    "website": "Amazon",
    "password": "jfU&6737G42"
}

with open("data.json", "w") as data_file:
    json.dump(new_data, data_file, indent=4)  # writes Python data into a JSON file
    
# `indent` Parameter
# Pretty-prints JSON with 4-space indentation (formats JSON for readability)
# Affects appearance only, not the actual data
```

Read JSON Data (`json.load`)
```python
import json

with open("data.json", "r") as data_file:
    data = json.load(data_file)  # converts JSON file data into a Python dictionary
    print(data)
    print(type(data))  # output: <class `dict`>
```

Update JSON Data
```python
# Update existing JSON data with new key-value pairs (3 steps)
import json

new_data_to_add = {
    "email": "me@"
}

# Read existing data
with open("data.json", "r") as data_file:
    data = json.load(data_file)

# Update data
data.update(new_data_to_add)

# Write updated data back
with open("data.json", "w") as data_file:
    json.dump(data, data_file, indent=4)
```
***

### References:
- *[Python JSON Module Documentation](https://docs.python.org/3/library/json.html)*
***
