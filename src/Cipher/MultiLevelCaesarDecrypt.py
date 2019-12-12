import Cipher.tk  
from Cipher.tk import EncryptDecryptCoord, GetChiSquared, Mode

def MultiDecrypt (message, alphabet, usables = 3, lan = "English", transformations = [], lowestchi = 9999, ogMessage = ""):    
    msg = ""    
    prev = (9999, (0, 0))     # (chi, key)

    for i in range (len(message)):
        for k in range (1, len (alphabet)):
            msg = EncryptDecryptCoord(message, (i,k), alphabet, Mode.DECRYPT)
            chi = GetChiSquared (msg, lan)

            if (round (chi, 3) < round (prev[0], 3)):
                prev = (chi, (i,k))

    # base case
    if (prev[0] >= lowestchi):
        v = ogMessage
        for tr in transformations:
            v = EncryptDecryptCoord (v, tr, alphabet, Mode.DECRYPT)
            return (v, lowestchi, transformations)

    if (len(transformations) == 0):  # only set lowest chi on the first run
        lowestchi = prev[0] 
        ogMessage = message

    transformations.append (prev[1])

    return MultiDecrypt (EncryptDecryptCoord (message, prev[1], alphabet, Mode.DECRYPT), alphabet, usables, lan, transformations, prev[0], ogMessage)
             
'''
# testing do write it here
a = " abcdefghijklmnopqrstuvwxyz"
p=[]
for c in a:
    p.append (c)

print ("starting...")
print (MultiDecrypt ("dtyktckcxlbd", p))
# original 231
'''