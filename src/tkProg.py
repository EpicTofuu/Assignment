""" General toolkit full of general tools *for the program*"""

# program tk

import os
from os import system

def ClearScreen():
    """Clear all elements on screen"""
    if (os.name == "nt"):   
        system ("cls")
    else:
        system ("clear")

def Pause ():
    input("press enter to continue...")