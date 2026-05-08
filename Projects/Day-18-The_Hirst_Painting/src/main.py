import colorgram
import turtle as turtle_module
import random


def get_colors():
    """Extract and return RGB colors from the image."""
    # Extract 50 colors from the image
    colors = colorgram.extract("../assets/image.jpg", 50)

    # Access and store RGB tuples in a list
    return [
        (color.rgb.r, color.rgb.g, color.rgb.b)
        for color in colors
        if color.rgb.r < 240 and color.rgb.g < 240 and color.rgb.b < 240  # Avoid white and near-white shades
    ]


def draw_painting(rows, columns, x, y, dot_size, spacing, rgb_colors, tim):
    """Draw the Hirst painting using colored turtle dots."""
    for _ in range(rows):
        tim.goto(x, y)  # move turtle to the beginning of the row
        y += spacing
        for _ in range(columns):
            tim.dot(dot_size, random.choice(rgb_colors))
            tim.forward(spacing)


def main():
    """Set up the turtle environment and create the Hirst painting."""
    turtle_module.colormode(255)

    # Painting settings
    rows = 10
    columns = 10
    start_x = -235
    start_y = -220
    dot_size = 20
    spacing = 50

    # Turtle setup
    tim = turtle_module.Turtle()
    tim.hideturtle()
    tim.speed("fastest")
    tim.penup()

    # Generate colors and draw painting
    rgb_values = get_colors()
    draw_painting(
        rows,
        columns,
        start_x,
        start_y,
        dot_size,
        spacing,
        rgb_values,
        tim
    )

    # Keep window open
    screen = turtle_module.Screen()
    screen.exitonclick()


main()
