#!/usr/bin/env python3

'''
convert names/input/text into phonetic alphabet based on user input

prerequisite requirement == pandas library to be installed

'''


import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

new_data = {row.letter: row.code for (index, row) in data.iterrows()}
print(new_data)

u_input = input("Supply a word, friend..\n").upper()

show_me_the_money = [new_data[n] for n in u_input]
print(show_me_the_money)
