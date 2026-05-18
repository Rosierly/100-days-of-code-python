from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# PART 1: Snake Movement (day-20)
# TODO 1: Create the snake body (3 squares)
# TODO 2: Make the snake move continuously forward
# TODO 3: Control snake direction with keyboard input

# PART 2: Game Logic (day-21)
# TODO 4: Detect collision with food
# TODO 5: Create and update the scoreboard
# TODO 6: Detect collision with wall
# TODO 7: Detect collision with tail

# Constants
SCREEN_SIZE = 600
BOUNDARY = SCREEN_SIZE / 2 - 10

# Screen Setup
screen = Screen()
screen.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # turns off automatic screen updates

# Create Snake, Food & Scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Bind Keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Game Loop
game_on = True
while game_on:
    screen.update()  # manually refreshes the screen
    time.sleep(0.1)  # controls game speed
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall - screen edge is 300, but snake size is 20x20 so collision is checked at 280
    if (snake.head.xcor() > BOUNDARY or snake.head.xcor() < -BOUNDARY
            or snake.head.ycor() > BOUNDARY or snake.head.ycor() < -BOUNDARY):
        game_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:  # excluding the head
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()
            break

screen.exitonclick()
