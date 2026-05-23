from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    """Displays and updates the game score."""

    def __init__(self, screen_size: int):
        super().__init__()
        self.screen_size = screen_size
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-self.screen_size // 2 + 100, self.screen_size // 2 - 50)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the displayed level on the screen."""
        self.clear()
        self.write(arg=f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Displays the game over message on the screen."""
        self.goto(0, 0)
        self.write(arg="Game Over", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        """Increases the current level and updates the scoreboard."""
        self.level += 1
        self.update_scoreboard()
