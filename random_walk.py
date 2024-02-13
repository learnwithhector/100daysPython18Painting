import random
from turtle import Turtle, Screen, colormode


def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


tim = Turtle()
tim.shape("turtle")
tim.width(20)
tim.speed(10)
colormode(255)

for _ in range(100):
    # tim.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    tim.color(generate_random_color())
    tim.forward(50)
    tim.right(random.choice([0, 90, 180, 270]))

screen = Screen()
screen.exitonclick()
