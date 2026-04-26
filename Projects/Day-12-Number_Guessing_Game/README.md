# Day 12 - Number Guessing Game
A number guessing game where the player chooses a difficulty, then tries to guess a secret number between 1 and 100 before running out of attempts.

<img width="800" height="525" alt="day-12-project" src="https://github.com/user-attachments/assets/061e8eb5-c4c2-4487-a90b-47a55804772b" />

## Notes

### Namespaces: Local vs. Global Scope
###### Scope is the region of a program where a variable or function is accessible and can be used --> local within a function and global throughout the entire script.
```python
enemies = 1

def increase_enemies():
    enemies = 2  # creates a new local variable, NOT updating the global one
    print(f"enemies inside function: {enemies}")  # output: 'enemies inside function: 2'

increase_enemies()
print(f"enemies outside function: {enemies}")  # output: 'enemies outside function: 1'
```
Local Scope
```python
# When you create a new variable or function inside another function, it's only accessible within that function because it has local scope.

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()  # output: 2
print(potion_strength)  # NameError: name `potion_strength` is not defined
# It's only defined inside the function, and we can use it ONLY there.
```
Global Scope
```python
# If we want a variable to be accessible outside the function, we define it in the global scope, like:
player_health = 10  # it's a global variable

def drink_potion():
    potion_strength = 2  # it's a local variable (defined inside a function)
    print(player_health)

# If I run my function the `player_health` variable will be printed out normally because it has global score.
drink_potion()  # output: 10
print(player_health)  # output: 10
```
Example & Namespace vs. Scope
```python
# Every variable and function has a namespace, that namespace is valid in certain scopes.
# A namespace is where a name lives; scope is where that name can be used.

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()
# drink_potion() function now has local scope within the function game()
# So, ONLY inside the game() function can we call the drink_potion() function.
```
***

### There is no Block Scope in Python
###### Python does not have block scope, meaning variables defined inside blocks like if, for or while are accessible outside those blocks within the same function or global scope.
```python
# In languages with block scope, variables exist only within the block they’re declared in (including nested blocks).

# Creating a Variable in Python inside:
# if / elif / statement
# for loop
# while loop
# --> Gives it Global Scope

# If you create a variable inside a function, it is only available within that function.
# This is the only way local scope is created.
```
Creating a Variable inside an if Block
```python
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

# The below print statement will give us a warning, because if the game level is not lower than 5 our variable `new_enemy` will never be declared.
# To avoid that we can initialize our variable beforehand (before the if statement):
new_enemy = None

if game_level < 5:
    new_enemy = enemies[0]  # Global Scope

print(new_enemy)  # output: 'Skeleton'
# Even though is defined inside an if statement, we can use it outside of it as well because it has Global Scope.
```
Creating a Variable inside a Function
```python
game_level = 3

def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]  # Local Scope

print(new_enemy) # NameError: name `new_enemy` is not defined
# Now, the line of code above will give us an error, because within the function there is Local Scope
# so the variable 'new_enemy' is ONLY available anywhere inside this function
```
***

### How to Modify a Global Variable
###### To modify a global variable inside a function, you use the global keyword to tell Python you mean the global variable, not a new local one.
```python
enemies = 1

def increase_enemies():
    global enemies  # this allows us to modify this variable inside the function
    # Without it, we cannot modify something that is global within a local scope, instead it creates a new local variable.
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()  # output: 'enemies inside function: 2'
print(f"enemies outside function: {enemies}")  # output: 'enemies outside function: 2'

# OTHERWISE, we get an error for trying to use `enemies` --> (enemies += 1) before declaring it
# UnboundLocalError: local variable `enemies` referenced before assignment

# We should avoid modifying global scope (inside a function that has local scope), because it can lead to unexpected problems.
```
Other Way
```python
# By using the `return` keyword to get the updated value of the variable `enemies` as the output of the function.
enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

# So now we can save this value in the global variable `enemies`
enemies = increase_enemies()  # enemies = 2
print(f"enemies outside function: {enemies}")
```
***

### Python Constants and Global Scope
###### Constants are variables meant to stay unchanged throughout the program, usually defined in the global scope using all-uppercase names (e.g., MAX_SPEED = 100).
```python
# Python doesn't have built-in support for constants like some other programming languages, but we follow a naming convention.
# Convention: UPPERCASE --> This reminds us NOT to modify this variable inside any function in our code.

# Global Constants
# By conversion, they're defined at the top-level (global scope) of a script or module so that they can be easily identified and modified (manually) if needed.
PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"
```
***
