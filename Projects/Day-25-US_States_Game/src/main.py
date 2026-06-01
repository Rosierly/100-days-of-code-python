import turtle
import pandas
from PIL import Image  # Pillow Library

black_states_img_path = "./blank_states_img.gif"
guessed_states = []

# Get Image Dimensions
with Image.open(black_states_img_path) as blank_states_img:
    blank_states_img.seek(0)  # get first frame (is used with image formats that contain multiple frames, such as GIFs)
    width, height = blank_states_img.size  # returns a tuple

# Screen Setup
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width, height)

# Add Background Image
screen.addshape(black_states_img_path)
turtle.shape(black_states_img_path)

# Create turtle object
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

# Load CSV and extract list of all states
states_df = pandas.read_csv("./50_states.csv")
all_states = states_df.state.to_list()

# Main Game Loop
while len(guessed_states) < len(all_states):
    user_answer = screen.textinput(
        title=f"{len(guessed_states)}/{len(all_states)} States Correct",
        prompt="What's another state's name?\nOr type 'Exit' to quit."
    ).title()

    if not user_answer:
        continue  # handle cancel/empty input

    # Exit game and save missing states to CSV
    if user_answer == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        pandas.DataFrame(missing_states, columns=["state"]).to_csv("states_to_learn.csv", index=False)
        break

    # Skip if the state was already guessed
    if user_answer in guessed_states:
        continue

    # Check if answer matches any state
    if user_answer in all_states:

        # Get coordinates for that state
        state_data = states_df[states_df.state == user_answer]
        x = state_data.x.iloc[0]
        y = state_data.y.iloc[0]

        # Move writer, display state name, and add to guessed states
        writer.goto(x, y)
        writer.write(user_answer)
        guessed_states.append(user_answer)

screen.mainloop()
