# ch11soundutilities.py
"""Functions to play sounds."""
from pysine import sine

TWELFTH_ROOT_2 = 1.059463094359  # 12th root of 2
A3 = 220  # hertz frequency for musical note A from third octave 

def play_sound(i, seconds=0.1):
    """Play a note representing a bar's magnitude. Calculation 
    based on https://pages.mtu.edu/~suits/NoteFreqCalcs.html."""
    sine(frequency=(A3 * TWELFTH_ROOT_2 ** i), duration=seconds)
    
def play_found_sound(seconds=0.1):
    """Play sequence of notes indicating a found item."""
    sine(frequency=523.25, duration=seconds) # C5
    sine(frequency=698.46, duration=seconds) # F5
    sine(frequency=783.99, duration=seconds) # G5

def play_not_found_sound(seconds=0.3):
    """Play a note indicating an item was not found."""
    sine(frequency=220, duration=seconds) # A3
       
