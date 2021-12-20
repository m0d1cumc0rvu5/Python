#!/usr/bin/env python3

#counts the number of occurrences of each letter in a string.
#with pprint

import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}


for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1


pprint.pprint(count)
