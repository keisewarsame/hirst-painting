import random
import turtle
from turtle import Turtle, Screen
tim = Turtle()
turtle.colormode(255)


def color_tuple(x_tuple):
    x = x_tuple[0]
    y = x_tuple[1]
    z = x_tuple[2]

    return x, y, z

color_list = [(43, 105, 171), (233, 206, 116), (225, 152, 87), (183, 50, 77), (118, 87, 50), (228, 120, 147), (214, 61, 80), (109, 110, 188), (130, 175, 210), (115, 185, 139), (55, 176, 110), (116, 168, 37), (202, 18, 42), (33, 56, 113), (221, 61, 50), (26, 142, 108), (154, 222, 193), (181, 170, 221), (30, 163, 170), (84, 35, 39), (40, 46, 80)]

tim.hideturtle()
tim.penup()
tim.setpos(-225, 0)

y_axis = 50

tim.speed(0)
for x in range(10):
    for i in range(10):
        random_color = random.choice(color_list)
        color = color_tuple(random_color)

        tim.dot(20, color)
        tim.penup()
        tim.forward(50)
    tim.setpos(-225, y_axis)
    y_axis += 50

screen = Screen()
screen.exitonclick()
