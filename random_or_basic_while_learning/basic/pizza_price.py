#!/usr/bin/env python3

'''
Determine what the pizza price would be determined by three pizza sizes and
two different pizza topping types.
'''



print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")


total = 0

if size == 'S':
    total += 15
if size == 'M':
    total += 20
if size == 'L':
    total += 25
if add_pepperoni == 'Y' and size == 'S':
    total += 2
if add_pepperoni == 'Y' and size != 'S':
    total += 3
if extra_cheese == 'Y':
    total += 1
print(f'Your final bill is: ${total}.') 
