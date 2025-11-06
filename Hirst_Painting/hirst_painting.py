
import turtle as t
import random

t.colormode(255)
turtle = t.Turtle()

# List of rgb colors
COLOR_PALETTE =  [[255, 0, 0], [0, 255, 0], [0, 0, 255],
    (230, 209, 82), (56, 79, 137), (220, 129, 162), (227, 151, 80), (119, 179, 214), (169, 45, 76),
    (217, 56, 100), (173, 159, 24), (233, 79, 48), (135, 219, 179), (10, 61, 149), (124, 61, 54),
    (176, 26, 61), (143, 209, 229), (107, 49, 40), (65, 132, 214), (32, 159, 214), (158, 184, 230),
    (232, 162, 175), (247, 201, 3), (130, 205, 191), (235, 167, 159), (72, 49, 43), (16, 51, 98),
    (13, 82, 110), (85, 30, 35)
]

# Initial x and y coordinates
pos_x = -200
pos_y = -200

DOT_SIZE = 22
GRID_SIZE = 10
SPACING = 50

turtle.penup()

# Draw hirst painting
for _ in range(GRID_SIZE):
    for _ in range(GRID_SIZE):
        turtle.setposition(pos_x, pos_y)
        color = random.choice(COLOR_PALETTE)
        turtle.dot(DOT_SIZE, color)
        pos_x += SPACING

    pos_x = -200
    pos_y += SPACING
    turtle.speed(0)
    turtle.goto(pos_x, pos_y)

win = t.Screen()
win.exitonclick()
