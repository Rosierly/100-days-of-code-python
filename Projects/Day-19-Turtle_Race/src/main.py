from turtle import Turtle, Screen
from tkinter import messagebox
import random

# Available turtle colors for the race
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


def get_bet(screen):
    """Prompt the user for a valid turtle bet."""
    prompt = "Which turtle will win the race? Enter one of the following colors: "  # initial prompt

    while True:
        user_input = screen.textinput("Make your bet", f"{prompt}\n{', '.join(COLORS)}")

        # Clicking Cancel returns None, while clicking OK with an empty input returns an empty string ("")
        # Detects if the user clicks cancel
        if user_input is None:
            return None

        user_input = user_input.strip().lower()
        if user_input in COLORS:
            return user_input

        prompt = "Invalid color. Please enter a valid turtle color: "  # error message


def create_turtles():
    """Create and position the turtle racers."""
    turtles = []

    for index, color in enumerate(COLORS):
        racer = Turtle(shape="turtle")  # create a turtle object for each color
        racer.color(color)
        racer.penup()

        y_position = 125 - (index * 50)
        racer.goto(x=-230, y=y_position)

        turtles.append(racer)

    return turtles


def show_race_result(winning_turtle, user_bet):
    """Display the result of the turtle race."""
    race_result = ("Congratulations. You won."
                   if winning_turtle == user_bet
                   else "Too bad. You lost.")

    messagebox.showinfo(
        title="Race Result",
        message=f"{race_result}\nThe {winning_turtle} turtle won!"
    )


def main():
    """Set up and run the turtle race game."""
    # Screen setup
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=500, height=400)

    # Get the user's turtle bet, or safely exit if cancel is clicked
    user_bet = get_bet(screen)
    if user_bet is None:
        screen.bye()
        return

    # Create turtle racers
    racers = create_turtles()

    # Start the race loop
    race_is_on = True

    while race_is_on:
        for racer in racers:
            racer.forward(random.randint(0, 10))

            # Check if a turtle crossed the finish line
            if racer.xcor() > 230:
                show_race_result(racer.pencolor(), user_bet)

                race_is_on = False
                break

    # Keep the window open until clicked
    screen.exitonclick()


main()

