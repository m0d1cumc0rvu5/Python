#!/usr/bin/env python3

###this program is an enhanced magic8ball
###simplified

import random

messages = ['It is certain',
    'It is decidedly so',
    'Yes definately',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

print('What knowledge do you seek?')
input()
print(messages[random.randint(0, len(messages) - 1)])
