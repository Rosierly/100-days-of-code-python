from turtle import Turtle

MOVE_DISTANCE = 10


class Player(Turtle):
    """Creates and controls the player turtle."""

    def __init__(self, screen_size: int):
        super().__init__()
        self.screen_size = screen_size
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.reset_position()

    def move(self):
        """Moves the player upward."""
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        """Returns the player to the starting position."""
        self.goto(0, -self.screen_size // 2 + 40)
        self.setheading(90)

    def reached_finish_line(self):
        """Returns True if the player reached the finish line."""
        return self.ycor() > self.screen_size // 2 - 30
