# SECTION 1

import random
import enum

try:
    from Cipher.tk import findIndexInList, str_append
except:
    from tk import findIndexInList, str_append

def CaesarEncrypt (userIn: str, alphabet = None) -> tuple:
    """encrypts the given string using a randomly generated key. Encrypts on Unicode by default"""

    k = random.randrange(0, 100)
    return (CaesarEncryptKey (userIn, k, alphabet), k)

def CaesarEncryptKey (userIn: str, key: list, alphabet = None) -> str:  
    """encrypts the given string using the caesar cipher encryption algorithm"""
    InList = []     #list to store user input

    # Convert the string input to character list
    for i in userIn:
        InList.append (i)

    # assume that the user wants to encrypt using the entire unicode standard
    if (alphabet == None or len(alphabet) == 0):
        for a in range (len(InList)):
            inIndex = ord (InList[a])                   # find the index of the letter in the *input*
            InList[a]= chr((inIndex + key))      
    else:   # Otherwise, just use the given alphabet
        for a in range (len (InList)):
            inIndex = findIndexInList (alphabet, InList[a])     # find the index of the letter in the *input*
            if (inIndex != -1):                                 # check if the character is supported, act accordingly
                InList[a] = alphabet[(inIndex + key) % len(alphabet)]   

    # convert the list back into a string
    value = ""
    for i in InList:
        value += i

    return value


'''
# testing do write it here
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
p=[]
for c in a:
    p.append (c)

print (CaesarEncryptKey ("DON IS SMART", 3, a))
'''