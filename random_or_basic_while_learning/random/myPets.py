#!/usr/bin/env python3

myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a net names ' + name)
else:
    print(name+ ' is my pet.')
