#!/usr/bin/env python3

from game_data import data
from art import logo, vs
import random, os


print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

def format_data(account):
  '''pull key values from each account'''
  account_name = account['name']
  account_desc = account['description']
  account_country = account['country']
  return f'{account_name}, from {account_desc}, located in {account_country}.'

#make game repeatable
while game_should_continue == True:


  #generate random account
  account_a = account_b
  account_b = random.choice(data)
  while account_a == account_b:
    account_b = random.choice(data)


  def check_answer(guess, a_followers, b_followers):
    '''use if statement to check if user is correct and return if      they are correct '''
    if a_followers > b_followers:
      return guess == 'a'
    else:
      return guess == 'b'


  print(f'Compare A: {format_data(account_a)}')
  print(vs)
  print(f'Compare B: {format_data(account_b)}')



  #ask user for a guess
  guess = input('Who has more followers? Type (A) or (B) ').lower()

  #check if user is correct
  #get follower count
  a_follower_account = account_a['follower_count']
  b_follower_account = account_b['follower_count']
  is_correct = check_answer(guess, a_follower_account, b_follower_account)

  os.system('clear')
  print(logo)
  #give user feedback on their answer
  if is_correct:
    score += 1
    print(f'You are correct! Current score: {score}')
  else:
    game_should_continue = False
    print(f'Sorry, you are incorrect. :( Final score: {score}')
