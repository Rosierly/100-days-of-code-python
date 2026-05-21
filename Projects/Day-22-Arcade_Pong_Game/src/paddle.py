from turtle import Turtle


class Paddle(Turtle):
    """Creates and controls a paddle."""

    def __init__(self, position: tuple[int, int]):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)  # 20 × 5 = 100px tall and 20 × 1 = 20px wide
        self.penup()
        self.goto(position)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
