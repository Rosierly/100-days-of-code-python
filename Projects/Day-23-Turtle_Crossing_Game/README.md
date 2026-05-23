# Day 23 - The Turtle Crossing Game


## Notes

### Randomness in Game
###### Randomness is used to make events happen unpredictably based on probability.
```python
import random

# ======================== Using random.randint ========================
if random.randint(0, 6) == 0:  # ~1 in 7 chance
    # do something

# ========================= Using random.random =========================
if random.random() < 0.15:  # Probability = 0.15 = 15% chance (more flexible and precise)
    # do something
```
***

### Creating a copy of a list
```python
cars = ["red", "blue", "green"]

# ============================== Using .copy() ==============================
cars_copy = cars.copy()
cars.remove("red")

# ================================ Using [:] ================================
cars_copy = cars[:]
cars.remove("red")

# ================================= Outputs =================================
print(cars)
# ["blue", "green"]

print(cars_copy)
# ["red", "blue", "green"]
```
***

### Why Copy a List Before Removing Items in a Loop
###### Removing items from a list while looping through it can cause elements to be skipped.
```python
cars = ["A", "B", "C", "D"]

for car in cars:
    print("Checking:", car)

    if car in ["A", "B"]:
        cars.remove(car)

print(cars)

# Output:
# Checking: A
#
# After removing "A", the list becomes: ["B", "C", "D"]
# The loop then moves to the next index, which is now "C", so "B" gets skipped.
#
# Checking: C
# Checking: D
```
Copying the List
```python
cars = ["A", "B", "C", "D"]

for car in cars[:]:
    print("Checking:", car)

    if car in ["A", "B"]:
        cars.remove(car)

print(cars)

# Output:
# Checking: A
#
# After removing "A", the original list becomes:
# ["B", "C", "D"]
#
# But the loop is iterating over a copy:
# ["A", "B", "C", "D"]
#
# So "B" is still checked normally.
#
# Checking: B
# Checking: C
# Checking: D
#
# Final List:
# ["C", "D"]
```
***
