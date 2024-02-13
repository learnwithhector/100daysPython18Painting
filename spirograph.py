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
num_circles = 100

for x in range(num_circles):
    r = 50
    tim.color(generate_random_color())
    tim.circle(r)
    tim.left(360 / num_circles)
    # tim.left(10)


screen = Screen()
screen.exitonclick()