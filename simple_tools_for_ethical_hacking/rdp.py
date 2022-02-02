#!/usr/bin/env python3

"""

quick fix for linux xfreerdp syntax avoidance

"""

import subprocess

ip = input('type ip addr here: ')
username = input('type username here: ')
password = input('type password here: ')


def xfreerdp():
    return subprocess.run(['xfreerdp', '/dynamic-resolution', '+clipboard', '/cert:ignore', f'/v:{ip}',
                           f'/u:{username}', f'/p:{password}'])


try:
    xfreerdp()

except KeyboardInterrupt:
    print('You have exited the program.')

else:
    print('No exceptions are caught; a clean exit.')
