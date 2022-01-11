#!/usr/bin/env python3
'''

prerequites:

apt install python3-tk

this will install the turtle/tkinter python library
if it is not already installed

'''
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Who will win the race?",
                            prompt="Your Choices are (red/blue/yellow/orange/green/purple)")
colors = ['red', 'blue', 'yellow', 'orange', 'green', 'purple']
y_axis = [-150, -90, -30, 30, 90, 150]
all_turtles = []

for i in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_axis[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for i in all_turtles:
        if i.xcor() > 230:
            is_race_on = False
            winning_color = i.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The winning color was {winning_color} :)")
            else:
                print(f"Sorry you lose. The winning color was {winning_color} :(")


    for i in all_turtles:
        random_distance = random.randint(0, 10)
        i.forward(random_distance)

screen.exitonclick()
