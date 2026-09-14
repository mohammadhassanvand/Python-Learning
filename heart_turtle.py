"""
Heart - Turtle Graphics
-----------------------
Draws a "hairy" heart shape by scattering thousands of short random
strokes along a parametric heart curve. Run it and watch the heart
grow stroke by stroke.

    x(a) = 16 * sin(a)^3
    y(a) = 13*cos(a) - 5*cos(2a) - 2*cos(3a) - cos(4a)
"""

import turtle
import math
import random


def heart_point(a: float, scale: float) -> tuple[float, float]:
    x = 16 * math.sin(a) ** 3 * scale
    y = (13 * math.cos(a) - 5 * math.cos(2 * a)
         - 2 * math.cos(3 * a) - math.cos(4 * a)) * scale
    return x, y


def draw_heart(strokes: int = 6000) -> None:
    screen = turtle.Screen()
    screen.setup(700, 700)
    screen.bgcolor("black")
    screen.tracer(0)

    pen = turtle.Turtle()
    pen.hideturtle()

    for i in range(strokes):
        a = random.uniform(0, 2 * math.pi)
        scale = random.uniform(0.5, 16)
        x, y = heart_point(a, scale)

        angle = math.atan2(y, x) + random.uniform(-0.4, 0.4)
        length = random.uniform(4, 20)

        pen.pencolor(1.0, random.uniform(0.3, 0.8), random.uniform(0.65, 0.95))
        pen.width(random.uniform(0.4, 1.2))
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.goto(x + length * math.cos(angle), y + length * math.sin(angle))

        if i % 200 == 0:
            screen.update()

    screen.update()
    turtle.done()


if __name__ == "__main__":
    draw_heart()
