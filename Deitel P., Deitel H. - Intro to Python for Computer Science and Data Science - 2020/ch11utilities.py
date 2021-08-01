# ch11utilities.py
"""Utility function for printing a pass of the 
insertion_sort and selection_sort algorithms"""

def print_pass(data, pass_number, index): 
    """Print a pass of the algorithm."""
    label = f'after pass {pass_number}: '
    print(label, end='')

    # output elements up to selected item
    print('  '.join(str(d) for d in data[:index]), 
        end='  ' if index != 0 else '') 

    print(f'{data[index]}* ', end='')  # indicate swap with *

    # output rest of elements
    print('  '.join(str(d) for d in data[index + 1:len(data)]))

    # underline elements that are sorted after this pass_number
    print(f'{" " * len(label)}{"--  " * pass_number}')  
    