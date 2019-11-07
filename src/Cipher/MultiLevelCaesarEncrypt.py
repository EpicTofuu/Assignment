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

def MultiEncrypt_Key (message: str, shifts: list, alphabet = None):
    """ multi encrypts a message using the caesar cipher"""
    value = ""
    for workingshift in shifts:
        value = tk.EncryptDecryptCoord (message, workingshift, alphabet, tk.Mode.ENCRYPT)        

    return value

def MultiEncrypt (message, iterations, alphabet = None):
    """Recursively multi encrypts a message using random shifts"""
    shifts = deque()
    for _ in range (iterations):
        shifts.append (random.randrange (0, len(alphabet)))

    return MultiEncrypt_Key (message, shifts, alphabet)

# testing

a = "1234"
p=[]
for c in a:
    p.append (c)

ere = MultiEncrypt_Key ("1111", [(0,1), (1,2), (1, 1)], p)
print (ere)