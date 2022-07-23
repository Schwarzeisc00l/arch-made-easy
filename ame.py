import os
from os.path import exists
print('Welcome to Arch Made Easy!')
print('This script will help you learn Arch!')
print('0-Apply easier .bashrc')
print('1-Read the documentation')
choose = input('Please choose an option: ')
if choose == 0:
    file_exists = exists('/usr/bin/python3')
    if file_exists == True:
        os.system('python3 apply-bashrc.py')
        print('Done! You can read the documentation now at [insert link]')
    if file_exists == False:
        os.system('sudo pacman -S python3')
        os.system('python3 apply-bashrc.py')
        print('Done! You can read the Wiki now at https://github.com/Schwarzeisc00l/arch-made-easy')

