from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# TODO 1: Create the screen
# TODO 2: Create and move a paddle
# TODO 3: Create another paddle
# TODO 4: Create the ball and make it move
# TODO 5: Detect collision with wall and bounce
# TODO 6: Detect collision with paddle
# TODO 7: Detect when paddle misses
# TODO 8: Keep Score

# Constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
X_POS = 350
Y_POS = 0

# Screen Setup
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Arcade Pong Game")
screen.bgcolor("black")
screen.tracer(0)

# Create Paddles, Ball & Scoreboard
right_paddle = Paddle((X_POS, Y_POS))
left_paddle = Paddle((-X_POS, Y_POS))
ball = Ball()
scoreboard = Scoreboard(SCREEN_HEIGHT)

# Listen for Keyboard Input & Bind Keys
screen.listen()
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

# Game Loop
game_on = True
while game_on:
    screen.update()
    time.sleep(ball.sleep_delay)  # controls game speed; smaller values make the animation/game smoother and faster
    ball.move()

    # Detect collision with top and bottom walls
    if ball.ycor() > SCREEN_HEIGHT / 2 - 20 or ball.ycor() < -SCREEN_HEIGHT / 2 + 20:
        ball.bounce_y()

    # Detect collision with paddles
    # Check `ball.x_direction` to prevent multiple bounces while the ball is still touching the paddle
    if (ball.xcor() > SCREEN_WIDTH / 2 - 80 and ball.distance(right_paddle) < 50 and ball.x_direction > 0
            or ball.xcor() < -SCREEN_WIDTH / 2 + 80 and ball.distance(left_paddle) < 50 and ball.x_direction < 0):
        ball.bounce_x()

    # Detect when the right player misses the ball
    if ball.xcor() > X_POS + 30:
        scoreboard.increase_score("left")
        ball.reset_position()

    # Detect when the left player misses the ball
    elif ball.xcor() < -X_POS - 30:
        scoreboard.increase_score("right")
        ball.reset_position()

screen.mainloop()
