from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    """Creates and updates the game scoreboard."""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(0, 260)  # positions scoreboard at the top center of the screen
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears and redraws the updated score."""
        self.clear()  # removes previous score text before rewriting
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increases the score by 1 and updates the scoreboard."""
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        """Displays the game over message in the center of the screen."""
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
