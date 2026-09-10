import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("codevisuals_")

t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()
turtle.tracer(5)

for i in range(200):
    color = colorsys.hsv_to_rgb(i / 200, 1.0, 1.0)
    t.pencolor(color)
    for _ in range(4):
        t.forward(i)
        t.left(90)
    t.left(5)

turtle.update()
turtle.exitonclick()