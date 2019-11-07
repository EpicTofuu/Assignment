# SECTION 1

import tk
import random
import enum

def Caesar_Encrypt (userIn: str, alphabet = None) -> tuple:
    """encrypts the given string using a randomly generated key. Encrypts on Unicode by default"""

    k = random.randrange(0, 100)
    return (Caesar_Encrypt_Key (userIn, k, alphabet), k)

def Caesar_Encrypt_Key (userIn: str, key: list, alphabet = None) -> str:  
    """encrypts the given string using the caesar cipher encryption algorithm"""
    InList = []     #list to store user input

    # Convert the string input to character list
    for i in userIn:
        InList.append (i)

    # assume that the user wants to encrypt using the entire unicode standard
    if (alphabet == None):
        for a in range (len(InList)):
            inIndex = ord (InList[a])                   # find the index of the letter in the *input*
            InList[a]= chr((inIndex + key))      
    else:   # Otherwise, just use the given alphabet
        for a in range (len (InList)):
            # find the index of the letter in the *input*
            inIndex = tk.findIndexInList (alphabet, InList[a])

            # check if the character is supported
            if (inIndex == -1):
                raise Exception ("Character not supported")

            InList[a] = alphabet[(inIndex + key) % len(alphabet)]       

    # convert the list back into a string
    value = ""
    for i in InList:
        value += i

    return value

'''
# Example:

# create the alphabet
_customAlphabetstr_ = "新大久保"   
_customAlphabet_ = []
for c in _customAlphabetstr_:
    _customAlphabet_.append (c)
Set_Custom_Charset (p)

# print
print (Caesar_Encrypt_Key ("大大久保新久新新大新", 1, Encoding.Custom))


print (Caesar_Encrypt_Key ("My name is yun", 24, Encoding.Unicode))
'''