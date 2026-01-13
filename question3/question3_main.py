import turtle
import math

# Draw one fractal edge using recursion
def draw_fractal_edge(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        part = length / 3
        draw_fractal_edge(part, depth - 1)
        turtle.left(60)
        draw_fractal_edge(part, depth - 1)
        turtle.right(120)
        draw_fractal_edge(part, depth - 1)
        turtle.left(60)
        draw_fractal_edge(part, depth - 1)

# Draw the complete fractal polygon
def draw_polygon(sides, length, depth):
    angle = 360 / sides
    for _ in range(sides):
