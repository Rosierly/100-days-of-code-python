from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    """Creates and updates the game scoreboard."""

    def __init__(self):
        super().__init__()
        self.score = 0

        with open("data.txt") as data:
            try:
                self.high_score = int(data.read())
            except (ValueError, FileNotFoundError):
                self.high_score = 0

        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(0, 260)  # positions scoreboard at the top center of the screen
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears and redraws the updated score."""
        self.clear()  # removes previous score text before rewriting
        self.write(arg=f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increases the score by 1 and updates the scoreboard."""
        self.score += 1
        self.update_scoreboard()

    def handle_game_over(self):
        """Displays the game over screen and shows a new high score message if achieved."""
        new_high_score = self.update_high_score()

        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

        if new_high_score:
            self.goto(0, -50)
            self.write(arg=f"NEW HIGH SCORE: {self.high_score}", align=ALIGNMENT, font=FONT)

    def update_high_score(self):
        """Updates and saves the high score if achieved, returning whether a new high score was set."""
        if self.score > self.high_score:
            self.high_score = self.score

            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

            return True

        return False
