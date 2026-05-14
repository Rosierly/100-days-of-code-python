from turtle import Screen
from snake import Snake
import time

# TODO 1: Create the snake body (3 squares)
# TODO 2: Make the snake move continuously forward
# TODO 3: Control snake direction with keyboard input

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # turns off automatic screen updates

# Create Snake
snake = Snake()

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

screen.exitonclick()
