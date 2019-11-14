# SECTION 3


import random
from Cipher.tk import EncryptDecryptCoord, Mode
from Cipher.CaesarEncrypt import Caesar_Encrypt_Key

def MultiEncrypt (message : str, alphabet = None, numOfShifts = 3):
    """multi encrypts a message using a pre generated list of shifts"""
    shifts = []
    for i in range (numOfShifts + 1):
        shifts.append ((random.randrange (len(message) - 1), (random.randrange(len(alphabet)))))

    return (MultiEncrypt_Key (message, shifts, alphabet), shifts)

def MultiEncrypt_Key (message: str, shifts: list, alphabet = None):
    """ multi encrypts a message using a given list of shifts"""

    _shifts= []
    _shifts.extend(shifts)
    value = EncryptDecryptCoord (message, _shifts[0], alphabet, Mode.ENCRYPT)        # shift the first element
    _shifts.pop(0)

    for workingshift in _shifts:
        value = EncryptDecryptCoord (value, workingshift, alphabet, Mode.ENCRYPT)   # shift all subsequent

    return value


# testing do write it here
'''
a = "abcdefghijklmnopqrstuvwxyz "
p=[]
for c in a:
    p.append (c)

ere = MultiEncrypt ("don is very smart", p)
print (ere)

A = tk.EncryptDecryptCoord ("231", (0,1), p, tk.Mode.ENCRYPT)
B = tk.EncryptDecryptCoord (A, (1,2), p, tk.Mode.ENCRYPT)
C = tk.EncryptDecryptCoord (B, (1,1), p, tk.Mode.ENCRYPT)

print (A)
print (B)
print (C)
'''