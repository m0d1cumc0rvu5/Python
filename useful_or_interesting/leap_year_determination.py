#!/usr/bin/env python3

'''
determine whether or not a given year is in fact a leap year.
'''
year = int(input("Which year do you want to check? "))


if year % 4 == 0 and year != 100 == 0 and year % 400 == 0:
    print('Leap year.')
if year % 4 == 0 and year % 100 == 0:
    print('Not a leap year.')
if year % 4 == 0:
    print('Leap year.')
else:
    print('Not leap year.')
