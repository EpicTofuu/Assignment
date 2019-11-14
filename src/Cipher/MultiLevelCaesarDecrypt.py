# TODO optimise

try:
    import Cipher.tk  
except:
    import tk

def MultiDecrypt (message, alphabet, usables = 3, lan = "English", transformations = [], lowestchi = 9999, ogMessage = ""):    
    msg = ""    
    prev = (9999, (0, 0))     # (chi, key)

    for i in range (len(message)):
        for k in range (1, len (alphabet)):
            msg = tk.EncryptDecryptCoord(message, (i,k), alphabet, tk.Mode.DECRYPT)
            chi = tk.GetChiSquared (msg, lan)

            if (round (chi, 3) < round (prev[0], 3)):
                prev = (chi, (i,k))

    # base case
    if (prev[0] >= lowestchi):
        v = ogMessage
        for tr in transformations:
            v = tk.EncryptDecryptCoord (v, tr, alphabet, tk.Mode.DECRYPT)
            return (v, lowestchi, transformations)

    if (len(transformations) == 0):  # only set lowest chi on the first run
        lowestchi = prev[0] 
        ogMessage = message

    transformations.append (prev[1])

    return MultiDecrypt (tk.EncryptDecryptCoord (message, prev[1], alphabet, tk.Mode.DECRYPT), alphabet, usables, lan, transformations, prev[0], ogMessage)
            
    

# testing do write it here
a = " abcdefghijklmnopqrstuvwxyz"
p=[]
for c in a:
    p.append (c)

print ("starting...")
print (MultiDecrypt ("dtyktckcxlbd", p))
# original 231
