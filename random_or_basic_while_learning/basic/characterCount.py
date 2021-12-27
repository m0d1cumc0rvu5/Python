#!/usr/bin/env python3

#counts the number of occurrences of each letter in a string.


message = 'The total amount of characters in this sentence would be...'
count = {}



for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1


print(count)
