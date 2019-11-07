# SECTION 3

import tk
import random
from collections import deque

try:
    from Cipher.CaesarEncrypt import Caesar_Encrypt_Key
    from Cipher.CaesarEncrypt import Set_Custom_Charset
    import Cipher.CaesarEncrypt
except:    
    import CaesarEncrypt
    from CaesarEncrypt import Caesar_Encrypt_Key

def MultiEncrypt_Recursive (message, iterations, alphabet = None):
    """Recursively multi encrypts a message using random shifts"""
    shifts = deque()
    for _ in range (iterations):
        shifts.append (random.randrange (0, len(alphabet)))

    return MultiEncrypt_Recursive_Key (message, shifts, alphabet)

# shift tuple: (index, key)
# TODO explore the idea of using a stack for shifts
def MultiEncrypt_Recursive_Key (message: str, shifts: deque, alphabet = None):
    """Recursively multi encrypts a message using the caesar cipher"""
    workingshift = shifts[0]

    value = DecryptCoord (message, workingshift, alphabet)

    # remove current shift
    shifts.pop ()

    # continue recursing if there are still tuples to process
    if (len(shifts) != 0):
        MultiEncrypt_Recursive_Key (value, shifts, alphabet)
        
    #return string
    return str(value)

def DecryptCoord (message, tup, alphabet) -> str:
    """Decrypts one coordinate (s, k) for s is the shift and k is the key"""

    value = ""
    c = str(message[tup[0]:])
    for k in range(len(c)):
        workingalphabetID = tk.findIndexInList (alphabet, c[k]) 
        o = workingalphabetID + tup[1]
        value = tk.str_append (value, alphabet[o % len(alphabet)], k)
    
    # Restore the string
    for a in range(tup[0]):
        value = tk.str_append (value, message[a], a)    

    return str(value)

# testing

a = "1234"
p=[]
for c in a:
    p.append (c)

ere = MultiEncrypt_Recursive_Key ("3241", [(0, 69),(3, 5),(2,9),(4,2)], p)
print (ere)