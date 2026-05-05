students = [
    {"name": "Alice", "scores": [85, 90, 78]},
    {"name": "Bob", "scores": [60, 65, 70]},
    {"name": "Charlie", "scores": [95, 100, 92]},
    {"name": "Diana", "scores": [50, 55, 58]}
]


# List Comprehension
# TODO 1: Create a list of names of students whose average score is above 80, and return them in uppercase.

# Without walrus
students_pass = [student["name"].upper() for student in students if sum(student["scores"])/len(student["scores"]) > 80]

# With the walrus operator (:=).
students_pass = [
    student["name"].upper()
    for student in students
    if (scores := student["scores"]) and sum(scores) / len(scores) > 80
]
# Note: Avoid using `and` to chain assignments (with :=); use it only for logical conditions.
# Bad:
# (scores := student["scores"]) and sum(scores) > 80   # unclear, relies on truthiness
# Good:
# (avg := sum(student["scores"]) / len(student["scores"])) > 80  # clear and direct


# Dictionary Comprehension
# TODO 2: Create a dictionary where:
#  key → student name (uppercase)
#  value → average score
#  include only students with average ≥ 80

student_dict = {
    student["name"].upper(): avg
    for student in students
    if (avg := sum(student["scores"]) / len(student["scores"])) > 80
}
