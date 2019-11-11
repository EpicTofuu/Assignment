""" General toolkit full of general tools *for the library*"""

from enum import Enum
import os

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

def _importLanguage (language) -> dict:
    """import a language frequency distribution file, for GetChiSquared, not for public use"""
    value = dict() 
    lines = []

    dirName = os.path.dirname (__file__)
    
    # Find languages
    languagePath = os.path.join (dirName, "LanguageCharDistributions", language) + ".txt"
    if (not os.path.exists (languagePath)):
        raise Exception (languagePath + " does not exist")
    
    f = open (languagePath, encoding="utf-8")

    for l in f:
        if (l[0] != "="): 
            lines.append (l)

    for i in range (0, len (lines), 2):
        letter = lines[i].strip()
        freq = lines [i + 1].strip()

        value [letter] = freq

    return value

def GetChiSquared (msg, language = "English"):
    """Finds the probability of the given string being a word"""
    LanDist = _importLanguage (language)    # list of all characters with their frequency distributions
    chiIndex = 0

    # iterate over all characters *in the language distribution file*
    for alpha in LanDist:                   
        # Get a list of all characters that are in the string that are not included in the distribution file 
        # (this is to prevent the calculations of longer message lengths that throw off the chi algorithm with symbols)
        voidChar = 0
        for char in msg:
            if (not list (LanDist.keys()).__contains__ (char.upper())):
                voidChar += 1

        if (voidChar == len(msg)):
            print ("Error: the given word: " + msg + " uses only non-English characters")
            return 999999       # If all characters aren't English, how is the string meant to be in English?

        c = msg.count (alpha) + msg.count (alpha.swapcase())                                         # include both lowercase and uppercase                                                      Actual count
        e = (len(msg) - voidChar) * float (LanDist [alpha]) if float(LanDist[alpha]) > 0 else 0.01   # prevent a division by zero on the off chance the frequency distribution is zero           Expected count

        # using the chi-squared formula
        chiIndex += ((c - e) ** 2) / e
    return chiIndex