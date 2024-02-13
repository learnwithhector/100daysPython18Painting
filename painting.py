import random
from turtle import Turtle, Screen, colormode


def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


tim = Turtle()
tim.shape("turtle")
tim.speed("fastest")
colormode(255)

r = 15

tim.penup()
tim.hideturtle()
x = -300
y = -300
tim.goto(x, y)


def inner():
    global x, y
    for circle in range(12):
        tim.goto(x, y)
        tim.pendown()
        tim.color(generate_random_color())
        tim.begin_fill()
        tim.circle(r)
        tim.end_fill()
        tim.penup()
        x += 50


for row in range(12):
    inner()
    x = -300
    y += 50

screen = Screen()
screen.exitonclick()
