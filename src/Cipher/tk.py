""" General toolkit full of general tools *for the library*"""

from enum import Enum

# Library tk

# For the EncryptDecryptCoord function
class Mode (Enum):
    ENCRYPT = 0
    DECRYPT = 1

# list: the list to search
# item: the item to look for
# returns: the index of the item as an integer. For duplicates, only the smallest index will be returned. Returns -1 for unsuccessful operations
def findIndexInList (L: list, item) -> int:
    """finds the index of an item in a given list"""

    for i in range (len (L)):
        if L[i] == item:
            return i
        
    # return -1 when unsuccessful
    return -1


# s: the string to append to
# c: the character to append
# i: the index to append at, the existing character at i will not be replaced but shifted
def str_append (s: str, c: str, i: int) -> str:
    """ appends a character to a string at an index. This method *returns a value*, it does not set the value automatically TODO"""

    L = list (s)        
    L.insert (i, c)
    value = ""

    for a in L:
        value += str(a)

    return value
    
def EncryptDecryptCoord (message, tup, alphabet, mode) -> str:
    """Decrypts or encrypts one coordinate (s, k) for s is the shift and k is the key"""

    value = ""
    c = str(message[tup[0]:])
    for k in range(len(c)):
        workingalphabetID = findIndexInList (alphabet, c[k]) 
        o = workingalphabetID + tup[1] if mode == Mode.ENCRYPT else workingalphabetID - tup[1]
        value = str_append (value, alphabet[o % len(alphabet)], k)
    
    # Restore the string
    for a in range(tup[0]):
        value = str_append (value, message[a], a)    

    return str(value)