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
        # default turtle size is 20x20 pixels -> segments are placed edge-to-edge
        # x positions are reversed so the head starts on the right side
        for num in range(-1, 2):  # initial snake position is centered on the screen
            x = num * -20
            self.add_segment((x, 0))

    def add_segment(self, position: tuple[float, float]):
        """Creates and adds a new snake segment."""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Adds a new segment to the end of the snake."""
        self.add_segment(self.segments[-1].position())  # returns the turtle’s current coordinates as a tuple (x, y)

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
