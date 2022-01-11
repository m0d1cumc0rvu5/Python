#!/usr/bin/env python3
'''

Creating a hirst painting via turtle library.

'''

import turtle as t
import random

color_list = [(223, 236, 228), (236, 230, 216), (140, 176, 207), (25, 32, 48), (26, 107, 159), (237, 225, 235), 
              (209, 161, 111), (144, 29, 63), (230, 212, 93), (4, 163, 197), (218, 60, 84), (229, 79, 43), 
              (195, 130, 169), (54, 168, 114), (28, 61, 116), (172, 53, 95), (108, 182, 90), (110, 99, 87), 
              (193, 187, 46), (240, 204, 2), (1, 102, 119), (19, 22, 21), (50, 150, 109), (172, 212, 172), 
              (118, 36, 34), (221, 173, 188), (227, 174, 166), (153, 205, 220), (184, 185, 210)]

tim = t.Turtle()
tim.shape("turtle")
t.colormode(255)
tim.penup()
x = -250
y = -200
tim.goto(x, y)
number_of_dots = 10


def move_horizontal():
    for i in range(0, number_of_dots):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)


move_horizontal()
while y % 50 == 0 and y < 201:
    y += 50
    tim.goto(x, y)
    move_horizontal()


screen = t.Screen()
screen.exitonclick()
