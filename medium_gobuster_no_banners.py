
#medium GoBuster python script with no banners included

import subprocess

ip = input('type ip addr here: ')
medium_gobuster = subprocess.run(['sudo', 'gobuster', 'dir', '--url', 'http://' + ip + '/', '-w', '/usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt', '-q'])

medium_gobuster()
