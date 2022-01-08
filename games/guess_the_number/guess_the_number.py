#!/usr/bin/env python3

'''
guess the number game    
'''
import random
from art import logo

EASY_COUNT = 10      # if 0 exit while loop
HARD_COUNT = 5       # if 0 exit while loop
keep_going   = False # if turned to False 


def check_answer(guess, answer, turn):
  '''for practice. checks answer against guess and returns the turn total. '''
  if guess > answer:
    print('Too high.')
    return turn - 1
  elif guess < answer:
    print('Too low.')
    return turn - 1
  else:
    print(f'Winner winner chicken dinner! You won with {answer} as your answer!')

def difficulty():
  level = input('Choose a difficulty. Type "easy" or "hard".\n')
  if level == 'easy':
    return EASY_COUNT
  else:
    return HARD_COUNT


def game():
  print(logo)
  answer = random.randint(1, 100)
  print('Welcome to the Number Guessing Game!')
  print("I'm thinking of a number between 1 and 100.")
  turn = difficulty()
  

  guess = 0

  while guess != answer: 
    print(f'You have {turn} remaining to guess the number. ')

    guess = int(input('Guess a number...\n'))

    turn = check_answer(guess, answer, turn)
    if turn == 0:
      print('You ran out of guesses. Game over')
      return

game()
