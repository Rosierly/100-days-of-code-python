# Print the welcome message and collect the data from the user
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# Calculate the result and print it to the console
result = round((bill + bill * tip_percentage / 100) / people, 2)
print(f"Each person should pay: ${result}")


# Detailed explanation for the result
tip = bill * tip_percentage / 100
total_bill = bill + tip
result = round(total_bill / people, 2)
print(result)