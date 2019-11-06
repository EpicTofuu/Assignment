# TODO optimise

# try except import pattern, imports according to where the library is called from
try:
    import tk
except:
    import Cipher.tk

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

def MultiDecrypt_Recursive (message, alphabet, iterations, includeZerothIteration = True) -> list:
    A = []

    # Generate all possible *decryptions* under the 0th iteration
    for I in range (len(message)):
        for n in range (len(alphabet)):
            A.append (DecryptCoord(message, (I,n), alphabet))

    return _multiDecrypt_Recursive (iterations, message, alphabet, A)

# TODO make message an int where message actually holds the length
# TODO remove testing the identity tuple
def _multiDecrypt_Recursive (it: int, message, alphabet: str, A, V = []) -> list:
    B = []  # contains all *found* elements

    # for each element in A, generate a set of messages using all possible keys
    for e in A:
        for I in range (len(message)):
            for n in range (len(alphabet)):
                B.append (DecryptCoord (e, (I, n), alphabet))
        
    V.extend (B)        

    # reduce iterations by 1
    it -= 1

    # shift the system
    if (it > 0):
        _multiDecrypt_Recursive (n, message, alphabet, B, V)      

    # return the value after n iterations
    return V

# testing do write it here
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
p=[]
for c in a:
    p.append (c)
print (MultiDecrypt_Recursive ("ZRDFWKYVTFFC", p, 4))

# TODO 