#!/usr/bin/env python3

'''
rock, paper, scissors
'''

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

print('Welcome to the rock, paper, scissors game!')
human_input = int(input('What is your move? Rock(0), Paper(1), Scissors(2)?\n'))
if human_input == 0:
  print(rock)
elif human_input == 1:
  print(paper)
else:
  print(scissors)
print('Computer Choice: ')
computer_choice = random.randint(0,3)
if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
else:
  print(scissors)
if human_input == computer_choice:
  print('You tied!')
elif human_input == 0 and computer_choice == 1:
  print('You lose!')
elif human_input == 0 and computer_choice == 2:
  print('You win!')
elif human_input == 1 and computer_choice == 2:
  print('You lose!')
elif computer_choice == 0 and human_input == 1:
  print('You win!')
elif computer_choice == 0 and human_input == 2:
  print('You lose!')
elif computer_choice == 1 and human_input == 2:
  print('You win!')


