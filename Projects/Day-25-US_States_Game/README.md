# Day 25 - U.S. States Game
A geography quiz game where the player guesses U.S. states on a map using Python Turtle Graphics, tracks their score, and saves the states they missed to a file at the end of the game.


## Notes

### Working with CSV Files and Analyzing Data with Pandas
***

CSV Files
###### A CSV (Comma-Separated Values) file is a text file used to store tabular data in a table-like format.
```python
# CSV are a common way of representing data that fits into tables, like a spreadsheet.
# Each line represents a row, and values are separated by commas.

# Contents/ Example of a CSV file
day,temp,condition
Monday,12,Sunny
Tuesday,14,Rain
```

Reading CSV Files with Basic Python
###### Using readlines() method to read a CSV file line by line into a list
```python
with open("weather_data.csv") as data_file:
    data = data_file.readlines()  # reads each line and stores them as items in a list
    print(data)

# Output:
# [
#     'day,temp,condition\n',
#     'Monday,12,Sunny\n',
#     'Tuesday,14,Rain\n'
# ]
```

Reading CSV Files with the Built-in csv Module
###### Python has a built-in module called csv that helps work with CSV files more easily.
```python
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)  # csv.reader() creates a CSV reader object that can be looped through row by row
    print(data)  # output: <_csv.reader object at 0x0000023F8B7C5E40>
```
```python
# Accessing a Single Column
# Extracting Temperature Data - Create a list that contains all temperatures

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)

    temperatures = []

    for row in data:
        print(row)  # each row is a list.
        # Output:
        # ['day', 'temp', 'condition']
        # ['Monday', '12', 'Sunny']
        # ['Tuesday', '14', 'Rain']

        # Check if the value is a digit to exclude the header row ("temp")
        if row[1].isdigit():  # row[1] accesses the second column ("temp")
            temperatures.append(int(row[1]))

    print(temperatures)  # output: [12, 14, 15, 18]
```

Using Pandas for Data Analysis
###### Pandas is a Python library used for data analysis and working with tabular data using DataFrames.
```python
import pandas  # Pandas is not built into Python, so it must be installed first.

# read_csv() loads the CSV file into a DataFrame (looks like a table)
data = pandas.read_csv("weather_data.csv")  # this method takes many optional arguments, the file path is required
print(data)  # data is formatted as a table, including row indices

# Output:
#        day  temp condition
# 0   Monday    12     Sunny
# 1  Tuesday    14      Rain
```
```python
# Accessing a Single Column
# Pandas uses the first row as column names, which are used to access each column.

print(data["temp"])  # "temp" refers to the temperature column.

# Output:
# 0    12
# 1    14
# Name: temp, dtype: int64
```

Comparison of Methods

| Method | Advantages | Disadvantages |
|---|---|---|
| `open()` | Simple and built into Python | Harder to organize and analyze data |
| `csv` module | Better CSV handling | Requires more manual work |
| `pandas` | Powerful and easy for data analysis | Requires installation |
***

### Pandas Basics: Series and DataFrames
###### A DataFrame is like an entire table (Excel sheet). Each sheet in an Excel file is a DataFrame in pandas.
###### A Series is like a single column (list-like structure). It's equivalent to a single column of data inside that table.
***

Using type() to Identify Pandas Data Structures
```python
import pandas

data = pandas.read_csv("weather_data.csv")

print(type(data))  # output: <class 'pandas.core.frame.DataFrame'>  -- pandas DataFrame object
print(type(data["temp"]))  # output: <class 'pandas.core.series.Series'>  -- pandas Series object
```

Converting DataFrames
```python
# ===================================== Examples =====================================

# SQL (requires a database connection + table name)
data_sql = data.to_sql(
    "weather_table",
    con=connection, 
    if_exists="replace", 
    index=False
)
# "weather_table" = table name
# con = SQLAlchemy engine or DB connection
# if_exists controls what happens if table already exists

# HTML (does not require any arguments, but optional parameters can be used)
data_html = data.to_html(index=False)  # render a DataFrame as an HTML table

# Excel (requires file name)
data_excel = data.to_excel("weather_data.xlsx", index=False)  # write object to an Excel sheet
# writes file to current directory

# ==================================== Dictionary ====================================

data_dict = data.to_dict()  # convert DataFrame to dictionary
print(data_dict)

# Output:
# {
#   'day': {0: 'Monday', 1: 'Tuesday'},
#   'temp': {0: 12, 1: 14},
#   'condition': {0: 'Sunny', 1: 'Rain'}
# }

# Each column becomes a key in the dictionary, and values are stored as nested dictionaries
# Each nested dictionary uses the row index as the key, and the corresponding cell values as the values.
```

Pandas Index: Row Labels and Export Behavior
```python
# index = labels used to identify rows in a DataFrame (can be integers, strings, or custom values)

# In export/output functions (CSV, Excel, HTML, SQL, etc.)
# index is ONLY a boolean:
# True  -> include row labels in output
# False -> exclude row labels from output

# Example:
data.to_csv("file.csv", index=False)

# IMPORTANT:
# If you want custom row labels, you must set the DataFrame index itself:
data.index = ["row1", "row2", "row3"]

# Example with custom index at creation time:
pd.DataFrame(
    {
        'Bob': ['I liked it.', 'It was awful.'],
        'Sue': ['Pretty good.', 'Bland.']
    },
    index=['Product A', 'Product B']
)

# Summary: 
# index in export functions → ONLY boolean (True / False)
# df.index = [...] → custom row labels (can be list, strings, numbers, etc.) df.index 
```

Converting Series
```python
# Converting a pandas Series to a Python list
temp_list = data["temp"].to_list()  # convert the "temp" column to a list
print(temp_list)  # output: [12, 14]
```

Data Analysis (mean + max)
```python
# Python way
average_python  = sum(temp_list) / len(temp_list)

# Pandas way
average_pandas  = data["temp"].mean()  # .mean() is a pandas Series method that calculates the average

print(average_python, average_pandas)  # same output

max_temp = data["temp"].max()  # .max() is a pandas Series method that returns the largest value
print(max_temp)
```

Get Data in Columns
```python
print(data["day"])  # column access (recommended) using the column name as a string -> works like dictionary-style access
print(data.day) # attribute-style access (not recommended) -> works like object-style access

# pandas treats column names as attributes internally, which can cause issues if the name conflicts with built-in methods

# the indexing operator [] does have the advantage that it can handle column names with reserved characters in them 
# (e.g. if we had a country providence column, reviews.country providence wouldn't work).

# Both give the same output (header is not included):
# 0     Monday
# 1    Tuesday
# Name: day, dtype: object

print(type(data["day"]))  # output: <class 'pandas.core.series.Series'>
```

Get Data in Row (Filtering)
```python
print(data[data.day == "Monday"]) # filters rows where the "day" column is equal to "Monday"
# Output:
#    day  temp condition
# 0 Monday   12     Sunny

print(data[data.temp == data.temp.max()])  # filters rows where the "temp" column equals the max temperature
# Output:
#    day  temp condition
# 1 Tuesday   14     Rain
```

Working with a Single Row (Filtered Result)
```python
monday = data[data.day == "Monday"]
print(type(monday))  # output: <class 'pandas.core.frame.DataFrame'>
# because filtering always returns a DataFrame (even if it has only one row)

# One row contains multiple columns (multiple data types per column)
# To access a single column from the filtered result:
print(monday.condition)
# Output:
# 0    Sunny
# Name: condition, dtype: object

# returns the "condition" column as a Series
```

Converting Values (Example: Celsius → Fahrenheit)
```python
monday_temp = monday.temp[0]  # extract the first value from the 'temp' column Series
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)
```

Creating & Saving DataFrames from Scratch
```python
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

new_data = pandas.DataFrame(data_dict)

print(type(new_data))  # output: <class 'pandas.core.frame.DataFrame'>

print(new_data)
# Output:
#   students  scores
# 0      Amy      76
# 1    James      56
# 2   Angela      65

new_data.to_csv("new_data.csv")  # saves the DataFrame to a CSV file (including the index by default)
```
***

### Displaying an Image with Turtle Graphics
###### Turtle Graphics allows only GIF images to be displayed by registering them as custom turtle shapes.
```python
import turtle 
screen = turtle.Screen() 

# Register the GIF image as a custom shape 
screen.addshape("logo.gif") 

# Create a turtle and assign the image as its shape 
image_turtle = turtle.Turtle()
image_turtle.shape("logo.gif")

# Instead of creating a turtle object, you can also directly use the default turtle:
# Both approaches work, but creating a turtle object is more flexible when you need multiple independent turtles.
turtle.shape("logo.gif")

screen.mainloop()

# Turtle Graphics only supports GIF files as custom shapes.
# Animated GIFs are not automatically animated; Turtle displays a single frame.
# The image behaves like a turtle shape, so it can be moved, rotated, hidden, or shown like any other turtle object.
```
***

### Getting Mouse Click Coordinates in Turtle
###### Turtle allows you to capture mouse click positions on the screen using `onscreenclick()`.
```python
import turtle

def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
```
***

### .iloc[0] vs .item() in Pandas
###### When working with filtered Pandas DataFrames, you often end up with a single value stored inside a Series.
```python
# There are two common ways to extract that value: .iloc[0] and .item().

import pandas

# Example: filtering a single state
states_df = pandas.read_csv("./src/50_states.csv")
state_data = states_df[states_df.state == "Alabama"] # returns a filtered DataFrame containing only one row.

# Using .iloc[0]
x = state_data.x.iloc[0]
y = state_data.y.iloc[0]
# Selects the first value by position
# Works even if the index is not starting from 0

# Using .item()
new_x = state_data.x.item()
new_y = state_data.y.item()
# Extracts the value only if the Series contains exactly one element
# Will raise an error if the Series has more than one value
# Returns a plain Python value (not a Series)
```
***

### References:
- *[Google Sheet - Weather Data (used in examples)](https://docs.google.com/spreadsheets/d/1Rs1CKjiagTeXa53212JkjRSDu-tx77_YxEgGdkv5zRY/edit?gid=0#gid=0)*
- *[Pandas Documentation](https://pandas.pydata.org/docs/)*
- *[Pandas API Reference](https://pandas.pydata.org/docs/reference/index.html)*
- *[Pandas DataFrame Conversion Methods](https://pandas.pydata.org/docs/reference/frame.html#serialization-io-conversion)*
- *[Pandas Series .item() method](https://pandas.pydata.org/docs/reference/api/pandas.Series.item.html)*
- *[Kaggle | Learn Pandas](https://www.kaggle.com/learn/pandas)*
- *[Online US States Quiz](https://www.sporcle.com/games/g/states)*
***
