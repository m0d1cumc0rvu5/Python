#!/usr/bin/env python3

from turtle import Turtle, Screen
from prettytable import PrettyTable

# timmy = Turtle()
# print(timmy)
# timmy.shape('turtle')
# timmy.color('cyan')
# timmy.forward(55)


# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


table = PrettyTable()
table.add_column("Findings", ["What", "A", "Pretty", "Table", "You", "Are"])
table.add_column("Usage", ["Useful", "You", "Shall", "Be", "I'm", "Sure"])
table.align["Findings"] = "r"
table.align["Usage"] = "l"
print(table)

