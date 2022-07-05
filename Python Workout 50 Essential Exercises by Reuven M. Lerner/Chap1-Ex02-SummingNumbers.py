# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 19:15:44 2022

@author: Ichxorya
"""

# Functions
def sum(*numbers, start=0):
    for number in numbers:
        start += number
    return start

def avg(*numbers):
    return sum(*numbers) / len(numbers)
    
# Run
print(sum(*[1, 2, 10]))

