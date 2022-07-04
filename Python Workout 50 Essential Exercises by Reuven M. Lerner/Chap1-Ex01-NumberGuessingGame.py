# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 19:15:44 2022

@author: Ichxorya
"""

# Libraries

from random import randint as rd

# Function
def guessing_game():
    random_number = rd(0, 101) # Random number in range [0, 100]
    name = input('Enter your name: ')
    print(f'Hello, {name}!')
    
    while guess := int(input('Guess it: ')):
        if guess > random_number:
            print('Too high. Try again!')
            continue
        elif guess < random_number:
            print('Too low. Try again!')
            continue
        else:
            print(f'Just right. The number is {guess}')
            return

# Run
guessing_game()
