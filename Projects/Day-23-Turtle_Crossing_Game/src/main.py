import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

# Constants
GAME_SPEED = 0.1
SCREEN_SIZE = 600

# Screen Setup
screen = Screen()
screen.setup(height=SCREEN_SIZE, width=SCREEN_SIZE)
screen.bgcolor("black")
screen.tracer(0)

# Create Game Objects
player = Player(SCREEN_SIZE)
car_manager = CarManager(SCREEN_SIZE)
scoreboard = Scoreboard(SCREEN_SIZE)

# Listen for Keyboard Input & Bind Keys
screen.listen()
screen.onkeypress(player.move, "Up")

# Game Loop
game_on = True
while game_on:
    screen.update()
    time.sleep(GAME_SPEED)  # controls the game's refresh speed

    # Spawn and update cars
    car_manager.create_car()
    car_manager.move_cars()
    car_manager.remove_offscreen_cars()

    # Detect collision between the player and a car
    for car in car_manager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_on = False

    # Handle level up when the player reaches the finish line
    if player.reached_finish_line():
        scoreboard.increase_level()
        player.reset_position()
        car_manager.increase_speed()

screen.mainloop()
