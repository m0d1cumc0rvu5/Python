#!/usr/bin/env python3

'''
cli calculator in python
'''
import os
from art import logo


def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}


def calculator():
  print(logo)
  num1 = float(input("What's the first number? "))
  for symbol in operations:
    print(symbol)

  should_continue = True
  while should_continue:
    operations_symbol = input('Pick an operation. ')  
    num2 = float(input("What's the next number? "))
    calc_function = operations[operations_symbol]
    answer = calc_function(num1, num2)

    print(f'{num1} {operations_symbol} {num2} = {answer}')

    if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation.\n") == "y":
      num1 = answer
    else:
      should_continue = False
      os.system('clear')
      calculator()

calculator()
