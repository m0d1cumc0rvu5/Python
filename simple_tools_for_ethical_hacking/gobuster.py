#!/usr/bin/env python3

"""

GoBuster made simple

prerequisites == GoBuster installed

"""

import subprocess

# wordlists
small = "/usr/share/wordlists/directory-list-lowercase-2.3-small.txt"
medium = "/usr/share/wordlists/directory-list-lowercase-2.3-medium.txt"
large = "/usr/share/wordlists/directory-list-lowercase-2.3-big.txt"

ip = input('type ip addr here or domain: ')
wordlist = input('Assuming your wordlists are located in /usr/share/wordlists/\n'
                 'small - directory-list-lowercase-2.3-small.txt\n'
                 'medium - directory-list-lowercase-2.3-medium.txt\n'
                 'large - directory-list-lowercase-2.3-big.txt\n'
                 'what wordlist would you like? (s)mall (m)edium (l)arge: ').lower()
banners = input('banners? (y)ay (n)ay: ').lower()
http = input('http (y)ay or https (n)ay: ').lower()
extension = input("extensions (y)ay or (n)ay: ").lower()

if wordlist == "s" or wordlist == "small":
    wordlist = small
elif wordlist == "m" or wordlist == "medium":
    wordlist = medium
elif wordlist == "l" or wordlist == "large":
    wordlist = large

if banners == "n" or banners == "nay" or banners == "no":
    banners = '-q'

if http == "n" or http == "nay" or http == "no":
    http = "https"


if extension == "y" or extension == "yay" or extension == "yes":
    extension = 'php, html, htm, txt'


def gobuster():
    try:
        if banners == '-q' and http == 'https' and extension == 'php, html, htm, txt':
            subprocess.run(['sudo', 'gobuster', 'dir', '--url', f'https://{ip}/', '-w', wordlist, banners])
        elif banners == '-q' and http == 'https':
            subprocess.run(['sudo', 'gobuster', 'dir', '--url', f'https://{ip}/', '-w', wordlist, banners])
        elif banners == '-q' and extension == 'php, html, htm, txt':
            subprocess.run(['sudo', 'gobuster', 'dir', '--url', f'http://{ip}/', '-w', wordlist, banners])
        elif http == 'https' and extension == 'php, html, htm, txt':
            subprocess.run(['sudo', 'gobuster', 'dir', '--url', f'https://{ip}/', '-w', wordlist])
        elif banners == '-q':
            subprocess.run(['sudo', 'gobuster', 'dir', '--url', f'http://{ip}/', '-w', wordlist, banners])
        elif http == 'https':
            subprocess.run(['sudo', 'gobuster', 'dir', '--url', f'https://{ip}/', '-w', wordlist])
        elif extension == 'php, html, htm, txt':
            subprocess.run(['sudo', 'gobuster', 'dir', '--url', f'http://{ip}/', '-w',  wordlist])
        else:
            subprocess.run(['sudo', 'gobuster', 'dir', '--url', f'http://{ip}/', '-w', wordlist])

    except KeyboardInterrupt:
        print('You have exited the program.')

    else:
        print('No exceptions are caught.')


gobuster()
