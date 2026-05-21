from turtle import Turtle

MOVE_DISTANCE = 2
STARTING_SLEEP_DELAY = 0.01
SPEED_MULTIPLIER = 0.9


class Ball(Turtle):
    """Creates and controls the Pong ball."""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

        self.x_direction = 1
        self.y_direction = 1

        # Controls game speed via time.sleep()
        self.sleep_delay = STARTING_SLEEP_DELAY

    def move(self):
        """Moves the ball across the screen."""
        new_x = self.xcor() + MOVE_DISTANCE * self.x_direction
        new_y = self.ycor() + MOVE_DISTANCE * self.y_direction
        self.goto(new_x, new_y)

    def bounce_x(self):
        """Reverses the ball's horizontal direction."""
        self.x_direction *= -1

        # Increase the ball's speed each time it touches a paddle
        self.sleep_delay *= SPEED_MULTIPLIER  # smaller sleep delays make the game faster

    def bounce_y(self):
        """Reverses the ball's vertical direction."""
        self.y_direction *= -1

    def reset_position(self):
        """Returns the ball to the center and resets its speed."""
        self.goto(0, 0)
        self.sleep_delay = STARTING_SLEEP_DELAY
        self.bounce_x()
