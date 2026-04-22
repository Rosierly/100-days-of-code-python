# Day 5 - Password Generator
A program that generates a random password based on user-specified numbers of letters, symbols, and numbers.


## Notes

### For Loop
###### A for loop is used to iterate over a sequence (like a list, tuple, or string) and execute a block of code for each item in that sequence.
Using the for loop with Python lists:
```python
# for item in list_of_items:
#     Do something to each item (Gets executed as many times as there are items in the list)
```
```python
fruits = ["Apple", "Peach", "Pear"]

# Loop through each fruit in the list
for fruit in fruits:
    print(fruit)  # On first iteration: fruit = "Apple", then "Peach", then "Pear"
# output: 'Apple\nPeach\nPear'

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruit + " Pie")  # output: 'Pear Pie'  (Careful with the indentation! This runs only once, after the loop ends.)
# In Python, the loop doesn't create its own scope. So, variables like `fruit` still exist after the loop ends and hold their last value ("Pear").
# output: 'Apple\nApple Pie\nPeach\nPeach Pie\nPear\n Pear Pie\nPear Pie'
```
***

### For Loops and the range() Function
###### for loops repeat code over a sequence, and range() generates integer sequences to control the loop.
```python
# range() Function:
# Generates a range of numbers used for looping.
# Returns a range object (not a list), which is why it’s mostly used in loops. (range object: an iterable sequence of integers.)
# The sequence starts at start (default 0), increments by step (default 1), and stops before stop (not included) --> all integers
range(start, stop, step)  # all optional except stop

# Usage with for loop:
for number in range(a, b):  # (b not inclusive)
  print(number)
```
```python
# The range() function has to be used in conjunction with another function.
print(range(1, 10))  # output: range(1, 10)

# range() returns a range object, so to see the sequence as a list, you can use list(range(...)).
r = range(1, 5)
print(r)           # Output: range(1, 5)  (this just shows the range object)
print(list(r))     # Output: [1, 2, 3, 4]  (this shows the full list of numbers)
```
Examples
```python
# Loop from 0 to 5 (default start=0)
for number in range(6):
    print(number)  # Output: 0 1 2 3 4 5 (each on a new line)

# Loop from 1 to 9 (10 not included)
for number in range(1, 10):
    print(number)  # Output: 1 2 3 4 5 6 7 8 9 (each on a new line)

# Loop from 4 to 11, stepping by 2
for number in range(4, 12, 2):
    print(number)  # Output: 4 6 8 10  (each on a new line)
```
***

### sum() Function
###### Returns the total (sum) of all items in an iterable (like a list or tuple). You can optionally add a starting value.
```python
expenses = [20, 35, 40, 25, 30]

print(sum(expenses))  # Output: 150

# Total spending including an extra $10 for a weekend dinner --> sum(iterable, start)
print(sum(expenses, 10))  # Output: 160
```
Mimic sum() function using a for loop
```python
total = 0
for amount in expenses:
    total += amount
print(total)   # Output: 150
```
***

### max() Function
###### Returns the largest value from an iterable (like a list, tuple, string, set, dict keys) or multiple arguments.
```python
temperatures = [68, 72, 75, 70, 69, 74, 71]

# Find the highest temperature
print(max(temperatures))  # Output: 75
```
Mimic max() function using a for loop
```python
max_temp = temperatures[0]  # Start with the first temperature
for temp in temperatures:
    if temp > max_temp:
        max_temp = temp
print(max_temp)  # Output: 75
```
Using max() with strings --> compares characters based on their Unicode (ASCII) values.
```python
word = "hello"
print(max(word))  # Output: 'o' (highest Unicode value - 111)
```
***

### len() Function
###### Returns the number of items in an object (like a list, string, or tuple).
```python
mylist = ["apple", "banana", "cherry"]
print(len(mylist))   # Output: 3
```
Mimic len() function using a for loop
```python
count = 0
for item in mylist:
    count += 1
print(count)
```
***


### statistics.mean() Function
###### Returns the arithmetic mean (average) of a list or iterable of numbers.
```python
import statistics

scores = [80, 90, 75, 85, 95]

average = statistics.mean(scores)
print(average)  # Output: 85 
print(type(average))  # Output: <class 'int'>
# If all values are integers and the mean is exactly an integer (no remainder), statistics.mean() returns an int, otherwise a float.
```
Mimic statistics.mean() function using a for loop
```python
scores = [80, 90, 75, 85, 95]
total = 0
count = 0

for score in scores:
    total += score
    count += 1

mean = total / count
print(mean)  # Output: 85.0
```
***

### List concatenation - Merging two lists
######  Combining two lists into one. This can be done using + operator, .extend() method, or a loop with .append() method.
 Using + Operator (Creates a New List)
```python
list_1 = [1, 2, 3]
list_2 = [3, 4, 5, 6]
sum_list = list_1 + list_2
print(sum_list)  # Output: [1, 2, 3, 3, 4, 5, 6]
```
Using .extend() Method (Modifies the Original List)
```python
test_list1 = [1, 4, 5, 6, 5]
test_list2 = [3, 5, 7, 2, 5]
test_list1.extend(test_list2)
print(test_list1)  # Output: [1, 4, 5, 6, 5, 3, 5, 7, 2, 5]
```
Using a for Loop with .append() (Manual Merge) - Naive Method
```python
list_1 = [1, 4, 5, 6, 5]
list_2 = [3, 5, 7, 2, 5]
for item in list_2:
    list_1.append(item)
print(list_1)  # Output: [1, 4, 5, 6, 5, 3, 5, 7, 2, 5]
```
***

### isdigit() Method
###### isdigit() checks if all characters in a string are digits (0–9). Returns True if all characters are digits, otherwise False.
```python
text1 = "12345"
print(text1.isdigit())   # Output: True

text2 = "123abc"
print(text2.isdigit())   # Output: False (contains letters)

text3 = ""
print(text3.isdigit())   # Output: False (empty string is not considered digits)

print("3.14".isdigit())  # Output: False (contains a dot)

print("-42".isdigit())   # Output: False (contains a minus sign)
```
***

### shuffle() Method
######  The shuffle() method takes a sequence, like a list, and randomly reorders the order of its items.
```python
import random

mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)  # Shuffles the list in place (randomizes order) --> modifies the original list
print(mylist)  # Output: Items in random order, e.g., ['cherry', 'apple', 'banana']
```
***

### join() Method
###### It's a string method that concatenates (joins) all the elements of an iterable (like a list or tuple) into a single string, using the string it is called on as the separator.
```python
# Syntax:
separator.join(iterable)
# separator: The string that will be placed between each element of the iterable.
# iterable: A sequence of strings (e.g., list, tuple) to join together.
```
```python
chars = ['P', 'y', 't', 'h', 'o', 'n']
word = ''.join(chars)  # Using empty string '' as separator
print(word)  # Output: Python

words = ['I', 'love', 'Python']
sentence = ' '.join(words)  # Using a space ' ' as separator - (or a newline \n)
print(sentence)  # Output: I love Python

letters = ['a', 'b', 'c']
result = '-'.join(letters)
print(result)  # Output: a-b-c

words = ['apple', 'banana', 'cherry']
result = ', '.join(words)
print(result)  # Output: apple, banana, cherry
```
***