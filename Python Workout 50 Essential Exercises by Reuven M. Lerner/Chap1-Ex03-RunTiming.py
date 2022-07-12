# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 17:26:19 2022

@author: Ichxorya
"""

# Float number exceptions handling
def float_input(n: str):
    try:
        n = float(n)
        return n
    except ValueError:
        print('Hey! That\'s not a valid number!')

# Function
def run_timing():
    number_of_runs = 0 
    total_time = 0
    
    while True:
        one_run = input('Enter 10 km run time: ')
        
        if not one_run: # If one_run is an empty string
            break
        
        number_of_runs += 1
        total_time += float_input(one_run)
    
    avg_time = total_time / number_of_runs
    
    print(f'Average time of {avg_time}, over {number_of_runs} runs.')
    
# Run
run_timing()