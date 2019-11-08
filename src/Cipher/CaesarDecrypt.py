# SECTION 2

import os
import os.path
import pickle
import tk 

def _importLanguage (language) -> dict:
    value = dict() 
    lines = []

    dirName = os.path.dirname (__file__)
    
    # Find languages
    languagePath = os.path.join (dirName, "CharacterCounts", language) + ".txt"
    if (not os.path.exists (languagePath)):
        raise Exception (languagePath + " does not exist")
    
    f = open (languagePath)
    for l in f:
        lines.append (l)

    for i in range (0, len (lines), 2):
        value [lines[i].strip()] = lines [i + 1].strip()

    return value


# Returns: a list of tuples that contain both the decrypted message with the corresponding key
def Caesar_Decrypt (message, alphabet):    
    """Decrypts the given string using the caesar cipher algorithm"""
    value = []          # list of all possible decryptions

    for key in range (len(alphabet)):
        decrypted = Caesar_decrypt_Key (message, alphabet, key)

        addable = (decrypted, key)
        value.append (addable)

    return value 

def Smart_Caesar_Decrypt (message, alphabet = "English"):
    """uses the chi squared algorithm to sort keys based on the probability of them returning a word in a given language.
    Language distribution packs can be added to the CharacterCounts folder in the library"""

    value = []
    LanDist = _importLanguage (alphabet)

    for key in range (1, len (alphabet)):   # don't test the identity
        msg = Caesar_decrypt_Key (message, alphabet, key)
        for a in LanDist:
            c = message.count (a)
            e = len(message) * float (LanDist [a])

            # using the chi-squared formula
            chiIndex = ((c - e) ** 2) / e
            v = (msg, chiIndex, key, a)
            value.append (v)
    value.sort (key = lambda t: t[1])
    return value


def Caesar_decrypt_Key (message, alphabet, key):
    """decrypts a string using a given key"""
    decrypted = "" 
    for char in message:
        if (alphabet.__contains__ (char)):
            decrypted = decrypted + alphabet[tk.findIndexInList (alphabet, char) - key]

    return decrypted

# testing do write it here
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
p=[]
for c in a:
    p.append (c)
print (Caesar_Decrypt ("WHVWLQJ", p))
# print (Smart_Caesar_Decrypt ("WHVWLQJ", p))