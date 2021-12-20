#!/usr/bin/env python3


def collatz():
    print('pick a number?')
    number = int(input())
    if number % 2 == 0:
        number = number // 2
        print(number)
    else:
        number = 3 * number + 1
        print(number)

collatz()
