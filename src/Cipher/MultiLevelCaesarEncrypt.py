# SECTION 3

import tk
import random

try:
    from Cipher.CaesarEncrypt import Caesar_Encrypt_Key
    from Cipher.CaesarEncrypt import Set_Custom_Charset
    import Cipher.CaesarEncrypt
except:    
    import CaesarEncrypt
    from CaesarEncrypt import Caesar_Encrypt_Key

def MultiEncrypt_Key (message: str, shifts: list, alphabet = None):
    """ multi encrypts a message using the caesar cipher"""

    value = tk.EncryptDecryptCoord (message, shifts[0], alphabet, tk.Mode.ENCRYPT)        # shift the first element
    shifts.pop(0)

    for workingshift in shifts:
        value = tk.EncryptDecryptCoord (value, workingshift, alphabet, tk.Mode.ENCRYPT)   # shift all subsequent

    return value

# testing do write it here
a = "abcdefghijklmnopqrstuvwxyz "
p=[]
for c in a:
    p.append (c)

ere = MultiEncrypt_Key ("don is very smart", [(0,1), (12,2), (1, 1), (6, 5)], p)
print (ere)

'''
A = tk.EncryptDecryptCoord ("231", (0,1), p, tk.Mode.ENCRYPT)
B = tk.EncryptDecryptCoord (A, (1,2), p, tk.Mode.ENCRYPT)
C = tk.EncryptDecryptCoord (B, (1,1), p, tk.Mode.ENCRYPT)

print (A)
print (B)
print (C)
'''