from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 70, "normal")

DASH_LENGTH = 20
GAP_LENGTH = 10


class Scoreboard(Turtle):
    """Creates and controls the Pong scoreboard."""

    def __init__(self, screen_height):
        super().__init__()

        self.screen_height = screen_height

        self.hideturtle()
        self.penup()
        self.pencolor("white")

        self.left_score = 0
        self.right_score = 0

        self.draw_middle_line()
        self.update_scoreboard()

    def draw_middle_line(self):
        """Draws the dashed line in the center of the screen."""
        line_turtle = Turtle()

        line_turtle.hideturtle()
        line_turtle.penup()
        line_turtle.pencolor("white")
        line_turtle.pensize(5)

        line_turtle.goto(0, self.screen_height / 2)
        line_turtle.setheading(270)

        number_of_dashes = self.screen_height // (DASH_LENGTH + GAP_LENGTH)

        for _ in range(number_of_dashes):
            line_turtle.pendown()
            line_turtle.forward(DASH_LENGTH)
            line_turtle.penup()
            line_turtle.forward(GAP_LENGTH)

    def update_scoreboard(self):
        """Clears and rewrites the current scores."""
        self.clear()

        self.goto(-100, 200)
        self.write(arg=self.left_score, align=ALIGNMENT, font=FONT)

        self.goto(100, 200)
        self.write(arg=self.right_score, align=ALIGNMENT, font=FONT)

    def increase_score(self, player_side):
        """Increases the score for the specified player."""
        if player_side == "left":
            self.left_score += 1

        elif player_side == "right":
            self.right_score += 1

        self.update_scoreboard()
