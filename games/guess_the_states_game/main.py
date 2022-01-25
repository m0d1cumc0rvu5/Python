#!/usr/bin/env python3

'''

Guess the U.S. states game

prerequisites require turtle/pandas libraries installed

'''
import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. Guess The States Game")
image = "blank_states_img.gif"
# create the background
screen.addshape(image)
turtle.shape(image)

answers = []
len_answers = len(answers)
while len(answers) < 50:
    answer_state = screen.textinput(title=f"{len(answers)}/50 Guess The States",
                                    prompt="What's another state's name?").title()

    data = pandas.read_csv("50_states.csv")
    states = data["state"].to_list()

    if answer_state == "Exit":
        missing_states = [ms for ms in states if ms not in answers]
        # missing_states = []
        # for state in states:
        #     if state not in answers:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_recall_better.csv")
        break
    if answer_state in states:
        answers.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_row = data[data.state == answer_state]
        t.goto(int(state_row.x), int(state_row.y))
        t.write(answer_state)
