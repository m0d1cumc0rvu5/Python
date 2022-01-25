#!/usr/bin/env python3

"""

~!~/ snake ~!~\

single player game usable keys consist of either A, W, S, D or left, up, down, right keys

to run:
python3 main.py

"""


from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "Down")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "Left")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "Right")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    # detect collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or \
            snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        snake.reset()
        scoreboard.reset()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            snake.reset()
            scoreboard.reset()

screen.exitonclick()
