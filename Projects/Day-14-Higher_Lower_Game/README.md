# Day 14 - Higher Lower Game
A game where the player is shown two public figures, brands, or entities and must guess which one has more social media followers.

<img width="800" height="458" alt="day-14-project" src="https://github.com/user-attachments/assets/3dd07510-8a09-45b1-8944-2fc257cb78ab" />

## Notes

### Setting a Default Parameter
###### Setting a default parameter means giving a function argument a value to use if no value is provided when the function is called.
```python
def greet(name=None):
    if name is None:
        print("Hello, stranger!")
    else:
        print(f"Hello, {name}!")
        
greet()           # Output: 'Hello, stranger!'
greet("Alice")    # Output: 'Hello, Alice!'
```
***
