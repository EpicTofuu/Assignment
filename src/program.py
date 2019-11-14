# SECTION 5

# General Collection
# Do Not Write It Here

import os
import os.path
import argparse
import pickle
import Cipher
import tkProg

from os.path import join, isdir, dirname

Modules = []    # stores all modules
Actions = []    # stores all actions in modules and the module itself

from AlphabetScannerModule import AlphabetScannerMod
AlphabetMod = AlphabetScannerMod()

# import and instantiate each of the modules

# Single level enc
from CaesarEncryptModule import CaesarEncryptMod
Modules.append (CaesarEncryptMod(AlphabetMod))

# Single level dec
from CaesarDecryptModule import CaesarDecryptMod
Modules.append (CaesarDecryptMod (AlphabetMod))

# Multi level enc
from CaesarMultiEncryptModule import MultiEncryptMod
Modules.append (MultiEncryptMod (AlphabetMod))

# note, even if the modules are added automatically, always add the alphabet scanner manually and do it *last*
Modules.append (AlphabetMod)


# TODO
'''
# import all modules except the program itself !
ModulePaths = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]
ModulePaths.remove ("program.py") 

for module in ModulePaths:
    __import__ (os.path.splitext(os.path.basename(module))[0])
    Modules.append ()
    '''

def Args ():
    """Handles argument parsing"""
    parser = argparse.ArgumentParser(description="Directly run a process from the run command")
    parser.add_argument("ProcessName", metavar="N", type=str, nargs='+', help="The name of the process to run")
    args = parser.parse_args()
    return args

tkProg.ClearScreen()
print ("Caesar encryption and decryption")
print ()

# display all module actions but also log them into a mega list
n = 1
for mod in Modules:
    for action in mod.Actions:
        print (str (n) + ") " + action)
        Actions.append ((mod.Actions[action], mod))
        n += 1

# TODO add input checking
userin = int (input (""))

# Call the method
Actions[userin - 1][0](Actions[userin - 1][1])
