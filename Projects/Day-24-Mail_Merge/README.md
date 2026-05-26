# Day 24 - The Mail Merge Project
A mail merge program that reads a list of names, replaces placeholders in a template letter, and generates personalized invitation letters automatically.

<img width="auto" height="620" alt="day-24-project" src="https://github.com/user-attachments/assets/a8adeaba-44b1-40db-88d4-43cc10d61be3" />

## Notes

### Python File Handling
Opening a File
###### The open() function opens a file and returns a file object.
```python
file = open("my_file.txt")  # this is a built-in function

# Parameters of `open()`
# - file → the path/name of the file
# - mode → how the file should be opened
# - Other optional parameters can also be specified
```
Reading a File
###### Use .read() to get the contents of the file as a string.
```python
file = open("my_file.txt")

contents = file.read()  # returns a string
print(contents)
```
Closing a File
###### Use .close() to manually close a file after you are done using it.
```python
file = open("my_file.txt")

contents = file.read()
print(contents)

file.close()

# Why close files?
# 
# When a file is opened, it uses computer resources.
# Closing the file manually:
# - frees resources
# - prevents memory/resource leaks
# - ensures changes are properly saved

# At some point it might close itself, but we don't know when or if that's going to happen.
```
***

### Using `with open()` (Recommended)
Reading a File
###### Use with open() to open and read a file safely.
```python
# A better and safer approach is using `with open()`, because automatically closes the file.
with open("my_file.txt") as text_file:
    file_contents = text_file.read()
    print(file_contents)
```
Reading Lines from a File
###### Use .readlines() to read a file line-by-line into a list.
```python
with open("names.txt") as file:
    lines = file.readlines()

print(lines)

# Example output:
# ["Alice\n", "Bob\n", "Charlie\n"]

# Each line keeps the newline character `\n`, so we may need to use the strip() method later.
```
Writing to a File
###### To modify a file, use mode "w" (write).
```python
with open("my_file.txt", mode="w") as text_file:
    text_file.write("New text.")

# "w" mode replaces all previous content
# If the file does not exist, Python creates it
```
Appending to a File
###### Use mode "a" (append) to add content without deleting existing text.
```python
with open("my_file.txt", mode="a") as text_file:
    text_file.write("\nAdd new text.")

# existing content stays and new text is added at the end
```
Creating a New File
###### If a file doesn't exist, and you use "w" mode, Python creates it automatically.
```python
with open("new_file.txt", mode="w") as new_file:
    new_file.write("New text.")
```
***

### Common File Modes
###### `"r"` ➝ Read (default)
###### `"w"` ➝ Write (overwrite)
###### `"a"` ➝ Append
###### `"rb"` ➝ Read binary
###### `"wb"` ➝ Write binary
***

### The strip() Method
###### Use .strip() to remove whitespace or specific characters from the beginning and end of a string.
```python
# strip() removes:
# - newline characters (`\n`)
# - spaces
# - tabs

text = "Alice\n"
clean_text = text.strip()
print(clean_text)
# Output: Alice

text = "   Hello   "
print(text.strip())
# Output: Hello
```
```python
# You can also remove specific characters
filename = "report.txt"
print(filename.strip(".txt"))

# Warning: strip() only removes characters from the beginning and end of the string.
```
***

### Root Directory
###### Files don’t just have names — they also have paths, which tell the computer where the file is located.
###### When accessing a file, paths begin from the root directory of the computer.
On Mac
###### The root is the Macintosh HD (the main hard drive).
```python
# Folders in paths are separated using a forward slash: `/`
/Users/Angela/Documents/file.txt
```
On Windows
###### The root is usually the C: drive.
```python
# Windows paths are separated using a backslash: `\`
C:\Users\Angela\Documents\file.txt
```
For Python
###### Even on Windows, Python commonly accepts forward slashes: `/` (Backslashes can accidentally create escape sequences)
```python
"C:/Users/Angela/Documents/file.txt"
# File paths must be written as strings
```
***

### Absolute and Relative Path
###### An absolute file path starts from the root directory of the computer.
###### A relative file path starts from the current working directory (the folder you are currently in).
```python
# Absolute Path
/Work/Project/talk.ppt  # Linux / macOS
C:\Work\Project\talk.ppt  # Windows

# Relative Path
./talk.ppt
```
```python
# ============================= Current Folder =============================
./talk.ppt
# `./` means look in the current folder
# If the file is already in the same folder as your Python file, you can shorten it to:
talk.ppt

# ============================== Parent Folder ==============================
../report.doc
# `../` means go up one folder level
# Current folder: Project
# File location: Work/report.doc

# =========================== Multiple levels Up ===========================
../../text.doc
# Each ../ moves up one folder level.
# ../../ moves up two folder levels.
```
***

## Snake Game V2 (Add a High Score)
Improvement: Add a local file that saves player's highest score and display it on the screen.

<img width="auto" height="550" alt="day-24-project2" src="https://github.com/user-attachments/assets/d1f2f558-a689-48f8-8b60-583a77665d95" />

### Notes
```python
# Working with Local Files and Directories

# Added a high score feature to the Snake Game using the Scoreboard class.
# However, when the program closes and runs again, the high score resets back to 0.

# To keep the high score permanently, we need to save it outside the program.
# We can do this by using an external file to store the player's highest score ("data.txt").
```
***

### References:
- *[The open() method](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)*
- *[The readlines() method](https://www.w3schools.com/python/ref_file_readlines.asp)*
- *[The replace() method](https://www.w3schools.com/python/ref_string_replace.asp)*
- *[The strip() method](https://www.w3schools.com/python/ref_string_strip.asp)*
***
