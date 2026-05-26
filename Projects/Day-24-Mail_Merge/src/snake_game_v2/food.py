from turtle import Turtle
import random


class Food(Turtle):
    """Creates and controls the food object."""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # default turtle size is 20x20, so food becomes 10x10
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.refresh()  # places the food at a random starting position

    def refresh(self):
        """Moves the food to a new random position."""
        self.goto(random.randint(-270, 270), random.randint(-270, 260))  # keeps food inside the screen boundaries
