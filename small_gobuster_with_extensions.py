
#small GoBuster python script with file extensions included

import subprocess

ip = input('type ip addr here: ')
small_gobuster = subprocess.run(['sudo', 'gobuster', 'dir', '--url', 'http://' + ip + '/', '-w', '/usr/share/dirbuster/wordlists/directory-list-2.3-small.txt', '-x', 'php,html,htm'])

small_gobuster()

