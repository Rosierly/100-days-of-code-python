import pandas as pd

# Load the squirrel census dataset
squirrel_data_df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_colors = ["gray", "cinnamon", "black"]
fur_color_counts = []

# Count the number of squirrels for each fur color
for color in fur_colors:
    filtered_squirrels = squirrel_data_df[squirrel_data_df["Primary Fur Color"] == color.title()]
    fur_color_counts.append(len(filtered_squirrels))

# Create a table with the squirrel counts and export it as a CSV file
squirrel_count_df = pd.DataFrame({
    "Fur Color": fur_colors,
    "Count": fur_color_counts
})

squirrel_count_df.to_csv("squirrel_count.csv")
