# Day 9 - Secret Auction Program
A program that simulates a blind auction. Multiple users can enter their bids anonymously, and at the end, the highest bidder wins.

<img width="800" height="574" alt="day-09-project" src="https://github.com/user-attachments/assets/b398190c-56ce-4665-a3d2-4001cd741437" />

## Notes

### Dictionaries
###### A dictionary is a collection of key-value pairs, where each key is unique and linked to a specific value. (retrieve data efficiently by key, not by position)
***

Defining a dictionary
```python
# Syntax: {Key: Value}, we separate each of the key-value pairs using a comma
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

example_dictionary = {
    123: "a random number",
    23: "another random number",
}
```
***

Retrieving items from dictionary
```python
# To retrieve an item from a dictionary, you don't type the index but the key.
# For example, for lists, list[0] or list[2]
# Syntax: dictionary["Key"]
print(programming_dictionary["Bug"])  # output: 'An error in a program that prevents the program from running as expected.'
print(example_dictionary[123])  # output: 'a random number'
```
***

Adding items to dictionary
```python
# It gets added to the end of the dictionary
programming_dictionary["2nd_Loop"] = "Assigning the value of the key named: 2nd_Loop"
print(programming_dictionary)
```
***

Edit an item in a dictionary
```python
# To edit a value in a dictionary, use the key to assign a new value.
# This is the same syntax as adding a new item — but if the key already exists, the value will be updated.
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)  # output: 'A moth in your computer.'
```
***

Empty dictionaries
```python
# Creating an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary --> deletes all the items in the dictionary (all the keys)
programming_dictionary = {}
print(programming_dictionary)
```
***

Loop through a dictionary
```python
new_dictionary = {"Bug": "A moth in your computer",
                  "Function": "A piece of code that you can easily call over and over again."}

# Printing the key and the value at the same time
# When you loop through a dictionary you get access only to keys
for key in new_dictionary:
    print(key)
    # To get the value of each key at the dictionary you need to use the retrieving method
    print(new_dictionary[key])
```
***

### KeyError
###### A KeyError occurs in Python when you try to access a dictionary key that doesn't exist.
```python
# If you don't spell the key correctly or type a key that doesn't exist, a KeyError will occur.
print(programming_dictionary["Bog"])  # ❌ KeyError: "Bog"
```
***

### Difference between lists and dictionaries in Python
###### --> Use a dictionary when you have a set of unique keys that map to values.
###### --> Use a list if you have an ordered collection of items. (lists allow duplicate members)
***

### len() functions with dictionaries
###### The len() function returns the number of key-value pairs in the dictionary.
```python
my_dictionary = {
    "name": "Alice",
    "age": 25,
    "country": "Canada"
}

print(len(my_dictionary))  # Output: 3
```
***

### eval() Function
###### The eval() function in Python evaluates a string as Python code and returns the result.
```python
# Evaluate a math expression given as a string
result = eval("2 + 3 * 5")
print(result)  # Output: 17

# eval() takes the string "[1, 2, 3, 4]" and evaluates it as a real Python list.
list_str = "[1, 2, 3, 4]"
my_list = eval(list_str)
print(my_list)        # Output: [1, 2, 3, 4]
print(type(my_list))  # Output: <class 'list'>
```
***

### Nesting Lists & Dictionaries
###### Nesting means putting one data structure inside another (like a list inside a dictionary or a dictionary inside a list) to organize complex data.
```python
# We can use a list or a dictionary as a value (nested)
# Syntax:
dictionary = {
  Key: [List],
  Key2: {Dict},
}
# To access a specific item in nested data, take it step by step:
# Use the key first (for dictionaries), then the index (for lists), and so on.
```
***

Nesting a List in a Dictionary
```python
# we can't say "France": "Paris", "Lille", "Dijon"
# because each key can only have one value (so we turn it into a list instead)
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}
print(travel_log["France"][1])  # output: 'Lille'
```
***

Nesting a Dictionary in a Dictionary
```python
travel_log_1 = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 5},
}
print(travel_log_1["Germany"]["cities_visited"][2])  # output: 'Stuttgart'
```
***

Nesting Dictionaries in Lists
```python
# we can access their items by their position
# The first dictionary is the item at index 0, the second at index 1
travel_log_2 = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
]
print(travel_log_2[1]["cities_visited"][1])  # output: 'Hamburg'
```
***

Nesting a List into a List
```python
list1 = ["A", "B", ["C", "D"]]  # ["C", "D"] is the third item in the list
print(list1[2][1])  # output: 'D'
```
***

### .items() Method
###### Returns a view of the dictionary’s key-value pairs as (key, value) tuples. 
###### This is commonly used when looping through both the keys and values of a dictionary at the same time.
```python
# Syntax:
dictionary.items()
```
```python
student_scores = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 92
}

# Loop through keys and values using .items()
for name, score in student_scores.items():
    print(f"{name} scored {score}")
# output:
# Alice scored 90
# Bob scored 85
# Charlie scored 92
```
***

### max() Function with Dictionaries
###### Returns the largest key or value in a dictionary, with the key parameter to specify whether to compare keys or values.
```python
bids = {
    "Alice": 150,
    "Bob": 200,
    "Charlie": 180
}

# Get the maximum bid amount
highest_bid = max(bids.values())
print(highest_bid)  # Output: 200

# Get the bidder with the highest bid
highest_bidder = max(bids, key=bids.get)
print(highest_bidder)  # Output: Bob
```
***
