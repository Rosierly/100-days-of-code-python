# Day 15 - Coffee Machine Program
A simulation of a coin-operated coffee machine that can serve espresso, latte, or cappuccino while tracking resources and processing payments.

<img width="auto" height="520" alt="day-15-project" src="https://github.com/user-attachments/assets/112cb6d5-f952-4ce3-a8a7-e98d605932f8" />

## Notes

### Dictionaries - get() Method
###### You can use the dict.get() method to safely retrieve a value from a dictionary without raising a KeyError if the key doesn’t exist.
```python
# Syntax
value = my_dict.get(key, default_value)
```
```python
# Example
fruit_colors = {
    "apple": "red", 
    "banana": "yellow"
}

# Key exists
color = fruit_colors.get("apple")  # Returns "red"

# Key doesn't exist, returns default
color = fruit_colors.get("orange", "unknown")  # Returns "unknown" instead of causing a KeyError
```
How to use .get() with Nested Dictionaries - Example from the Project
```python
MENU = {
    "latte": {
        "ingredients": {"water": 200, "milk": 150}
    }
}

selected = "latte"
ingredient = "milk"

amount = MENU[selected]["ingredients"].get(ingredient, 0)
print(amount)  # Output: 150
```
***

### Dictionaries - items() Method with a `for` loop:
###### The items() method returns a view of the dictionary’s key-value pairs as tuples, which can be iterated over in a for loop to access both keys and values simultaneously.
```python
fruit_colors = {"apple": "red", "banana": "yellow", "grape": "purple"}

for fruit, color in fruit_colors.items():
    print(f"The color of {fruit} is {color}.")
    
# Output
# The color of apple is red.
# The color of banana is yellow.
# The color of grape is purple.
```
***

### Formatting Numbers to 2 Decimal Places
###### `:.2f` is a format specifier that tells Python how to display a number (rounded to 2 decimal places, shown as a string).
###### `round(number, 2)` rounds a floating-point number to 2 decimal places, returning a numeric value.

```python
price = 3.14159

# Using :.2f in an f-string (formats as a string)
formatted_change = f"{price:.2f}"
print(formatted_change)  # Output: 3.14

# Using round() function (returns a float)
rounded_change = round(price, 2)
print(rounded_change)  # Output: 3.14

# Difference
# :.2f is for display formatting (string output).
# round() actually changes the numeric value (useful for calculations).
```
***

### String Formatting with format() Method
###### The format() method is a build-in function that inserts values into {} placeholders within a string to create formatted text.
```python
name = "Alice"
age = 30

# Using format() method to insert variables into a string
greeting = "My name is {}, and I am {} years old.".format(name, age)
print(greeting)  # Output: My name is Alice, and I am 30 years old.
```

### How to add TODOs in your code - TODO tab
###### A TODO is a comment in code marking a task to be done later, helping developers keep track of unfinished work.
```python
# TODO: Refactor this function to improve performance
def some_function():
    pass

# TODO tab -> follow up of all the TODOs in our file
# The TODO tab lists all TODO comments in your file to help you track and manage pending tasks easily.
```
***

### How to bring up the Emoji Keyboard on Windows and Mac
- **Windows:** Press `Windows key + .` (period) or `Windows key + ;` (semicolon) to open the emoji picker.
- **Mac:** Press `Control + Command + Space` to bring up the emoji viewer.
***

### PyCharm keyboard shortcuts (Windows)
###### Running & Debugging
| Action               | Shortcut        | Description                         |
|----------------------|-----------------|-----------------------------------|
| Run current script   | `Shift + F10`   | Run the current run configuration  |
| Debug current script | `Shift + F9`    | Debug the current run configuration|

---

###### Navigation & Search
| Action               | Shortcut               | Description                              |
|----------------------|------------------------|------------------------------------------|
| Find Action          | `Ctrl + Shift + A`     | Search for any action or setting         |
| Search Everywhere    | `Shift` (double tap)   | Search classes, files, symbols, actions  |
| Go to File           | `Ctrl + Shift + N`     | Quickly open any file                     |
| Go to Class          | `Ctrl + N`             | Jump to a class by name                   |
| Go to Symbol         | `Ctrl + Alt + Shift + N` | Jump to a symbol                        |
| Find in Path         | `Ctrl + Shift + F`     | Search text across the whole project     |
| Replace in Path      | `Ctrl + Shift + R`     | Search and replace across the project    |

---

###### Code Editing & Refactoring
| Action               | Shortcut        | Description                               |
|----------------------|-----------------|-------------------------------------------|
| Rename (Refactor)    | `Shift + F6`    | Rename variable/class/file safely          |
| Code Completion      | `Ctrl + Space`  | Basic code completion                      |
| Smart Code Completion| `Ctrl + Shift + Space` | Context-aware code completion          |
| Quick Fix / Intentions| `Alt + Enter`  | Show suggested fixes or intentions         |
| Comment/Uncomment Line| `Ctrl + /`     | Toggle line comment                        |
| Duplicate Line       | `Ctrl + D`     | Duplicate current line or selection         |
| Delete Line          | `Ctrl + Y`     | Delete current line                         |
| Reformat Code        | `Ctrl + Alt + L` | Auto-format your code                      |
| Show Parameter Info  | `Ctrl + P`     | Show method/function parameter info         |

---

###### Navigation History
| Action               | Shortcut            | Description                             |
|----------------------|---------------------|-----------------------------------------|
| Navigate Back        | `Ctrl + Alt + Left` | Go back in navigation history           |
| Navigate Forward     | `Ctrl + Alt + Right`| Go forward in navigation history        |

---

###### Tools
| Action               | Shortcut        | Description                     |
|----------------------|-----------------|---------------------------------|
| Open Terminal        | `Alt + F12`     | Open embedded terminal          |

---
###### Tips

- Double-tap `Shift` to search *anything* — files, classes, actions, symbols.
- Use `Alt + Enter` for quick fixes and intentions.
- Use `Shift + F6` for safe renaming across your code.
- `Ctrl + /` is great for quickly toggling comments.

*Reference: [JetBrains PyCharm Keyboard Shortcuts](https://www.jetbrains.com/help/pycharm/mastering-keyboard-shortcuts.html?keymap=secondary_windows)*
***
