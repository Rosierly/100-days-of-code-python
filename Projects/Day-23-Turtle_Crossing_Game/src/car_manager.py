from turtle import Turtle
import random

STARTING_SPEED = 8
SPEED_INCREMENT = 5
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
LANE_SPACING = 50


class CarManager:
    """Handles creation, movement, and difficulty scaling of obstacle cars."""

    def __init__(self, screen_size):
        self.screen_size = screen_size
        self.lanes = list(range(-self.screen_size // 2 + 100, self.screen_size // 2 - 100, LANE_SPACING))

        self.cars = []
        self.car_speed = STARTING_SPEED

    def create_car(self):
        """Randomly spawns a new car at the right edge of the screen."""
        if random.randint(0, 5) == 0:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            car.setheading(180)

            random_y = random.choice(self.lanes)  # make car movement structured and avoid random vertical overlap
            car.goto(self.screen_size // 2, random_y)

            self.cars.append(car)

    def move_cars(self):
        """Moves all cars across the screen at the current speed."""
        for car in self.cars:
            car.forward(self.car_speed)

    def remove_offscreen_cars(self):
        """Removes cars that have moved past the left edge of the screen."""
        for car in self.cars[:]:
            if car.xcor() < - self.screen_size // 2 - 50:
                car.hideturtle()
                self.cars.remove(car)

    def increase_speed(self):
        """Increases the speed of all cars for the next level."""
        self.car_speed += SPEED_INCREMENT
