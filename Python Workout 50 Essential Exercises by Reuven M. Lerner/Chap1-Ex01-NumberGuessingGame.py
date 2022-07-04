# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 19:15:44 2022

@author: Ichxorya
"""

# Libraries

from random import randint as rd

# Function
def guessing_game():
    random_number = rd(1, 101) # Random number in range [1, 100]
    guess = 0
    while guess != random_number:
        guess = int(input('Guess it: '))
        if guess > random_number:
            print('Too high. Try again!')
            continue
        elif guess < random_number:
            print('Too low. Try again!')
            continue
        else:
            print(f'Just right. The number is {guess}')
            return