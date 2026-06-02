# Data Overlap
# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
# You are going to create a list called result which contains the numbers that are common in both files.
#
# e.g. if file1.txt contained: 1, 2, 3
# and file2.txt contained: 2, 3, 4
# result = [2, 3]
#
# IMPORTANT:  The output should be a list of integers and not strings!
# Try to use List Comprehension instead of a Loop.


def read_file(path):
    with open(path) as file:
        return [int(line.strip()) for line in file]


contents1 = read_file("file1.txt")
contents2 = read_file("file2.txt")

result = [num for num in contents1 if num in contents2]

print(result)
