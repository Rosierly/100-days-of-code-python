# Day 11 - Blackjack Game
A Python program that simulates a simplified game of Blackjack where the user plays against the computer (dealer).


## Notes

### `append()` vs. `+=` or `extend()` with Lists
###### In Python, append(), extend(), and += are used to add elements to a list — but they work differently depending on what you're adding.
```python
# append(item)
# Adds a single item to the end of a list.
# The item can be any data type (e.g., string, list, number).
new_list = []
new_list.append("apple")  # → ['apple']

# extend(iterable) or += iterable
# Adds each element of an iterable (like a list or string)
# Equivalent to a loop that appends each item one by one.
# += is shorthand for .extend() when working with lists.
fruits = ["apple", "banana"]
fruits.extend(["orange", "grape"])  # → ['apple', 'banana', 'orange', 'grape']

# OR using +=  (only with same data types)
fruits += ["kiwi"]  # → ['apple', 'banana', 'orange', 'grape', 'kiwi']
new_list += random_fruit  # ❌ TypeError (if random_fruit is a string or non-list object)
```
Example
```python
import random

fruits = ["apple", "banana", "orange"]
new_list = []

random_fruit = random.choice(fruits)
new_list.append(random_fruit)    # ✅ Adds a single item
fruits.extend(new_list)          # ✅ Adds each element of new_list to the fruits list
new_list += random_fruit         # ❌ TypeError: 'str' object is not iterable
```
***