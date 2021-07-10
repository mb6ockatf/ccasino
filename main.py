##
# Playing the casino main file
#
import time
from ctw import ctw
# Introduction
print("You're playing the casino. You can choose:")
print(' - 1 to 18 or 19 to 36')
print(' - odd or not odd')
print(' - red or black')
print(' - any number from 1 to 36, 0 and 00')
print(' - print ! to quit')

# Game started
a = input('Type in your choice: ')
while a != '!':
    ctw(a)
    a = input('Type in your choice: ')
else:
    print('Bye')
    time.sleep(3)
    quit()
