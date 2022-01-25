#!/usr/bin/env python3

"""

~!~/ miles to km converter \~!~

"""

from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=400, height=200)


blank = Label(text="                   ")
blank.grid(ipadx=35, ipady=30)

is_equal = Label(text="is equal to", font=("Arial", 12, "bold"))
is_equal.grid(column=0, row=1)

input = Entry(width=12, justify="center")
input.grid(column=2, row=0)


# # label
miles = Label(text="Miles", font=("Arial", 12, "bold"))
# my_label.pack() places label on screen this method is required to display the actual text
miles.grid(column=3, row=0, padx=35)

# # label 2
km = Label(text="Km", font=("Arial", 12, "bold"))
km.grid(column=3, row=1, padx=35)


answer = Label(text="0", font=("Arial", 12, "bold"))
answer.grid(column=2, row=1)


def calculate_clicked():
    print("I have now been clicked.")
    new_text = int(input.get())
    # TODO: Place equation here ... miles * by 1.609344
    new_text *= 1.609344
    # interactive: allows you to replace answer text with the below prompt when the button is actually clicked.
    answer.config(text=int(new_text))


calculate = Button(text="Calculate", command=calculate_clicked)
calculate.grid(column=2, row=3, pady=20)


# # always needs to be at very end of program
window.mainloop()
