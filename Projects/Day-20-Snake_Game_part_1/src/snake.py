from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Creates and controls the snake."""

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates the initial snake body."""
        for num in range(-1, 2):  # initial snake position is centered on the screen
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(x=num * -20, y=0)
            # default turtle size is 20x20 pixels -> segments are placed edge-to-edge
            # x positions are reversed so the head starts on the right side
            self.segments.append(new_segment)

    def move(self):
        """Moves the snake forward."""

        # Move body segments from back to front
        for index in range(len(self.segments) - 1, 0, -1):  # excluding the head (index 0)
            self.segments[index].goto(x=self.segments[index - 1].xcor(), y=self.segments[index - 1].ycor())

        # Move head forward
        self.head.forward(MOVE_DISTANCE)

    # Snake game rule: the snake can't turn directly into itself
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
