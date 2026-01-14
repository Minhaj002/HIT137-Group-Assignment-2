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
        draw_fractal_edge(length, depth)
        turtle.left(angle)

def main():
    sides = int(input("Number of polygon sides: "))
    length = int(input("Length of each side: "))
    depth = int(input("Recursion depth: "))

    turtle.speed("fastest")
    turtle.hideturtle()

  # Position turtle near the center
    radius = length / (2 * math.sin(math.pi / sides))
    t.penup()
    t.setpos(-length / 2, -radius / 3)
    t.pendown()

    draw_polygon(sides, length, depth)

    t.done()
    
    if __name__ == "__main__":
    main()

t.screen.mainloop()



