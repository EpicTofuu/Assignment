# TODO optimise

# try except import pattern, imports according to where the library is called from
try:
    import Cipher.tk
    from Cipher.MultiLevelCaesarEncrypt import EncryptDecryptCoord    
    from Cipher.MultiLevelCaesarEncrypt import Mode
except:
    import tk
    from MultiLevelCaesarEncrypt import EncryptDecryptCoord  
    from MultiLevelCaesarEncrypt import Mode


def MultiDecrypt_Recursive (message, alphabet, iterations, includeNonNElements = False, includeZerothIteration = True) -> list:
    A = []

    # Generate all possible *decryptions* under the 0th iteration
    for I in range (len(message)):
        for n in range (len(alphabet)):
            msg = EncryptDecryptCoord(message, (I,n), alphabet, Mode.DECRYPT)
            A.append ((msg, (I, n)))

    return _multiDecrypt_Recursive (iterations, message, alphabet, A, includeNonNElements)

def _multiDecrypt_Recursive (it: int, message, alphabet: str, A, includeNonNElements, V = []) -> tuple:

    if (not includeNonNElements and it > 0):
        V.clear()

    B = []  # contains all *found* elements

    # for each element in A, generate a set of messages using all possible keys
    for e in A:
        for I in range (1, len(message)):
            for n in range (1, len(alphabet)):
                ap = (EncryptDecryptCoord (e[0], (I, n), alphabet), (I, n), Mode.DECRYPT)
                B.append (ap)
        
    V.extend (B)        

    # reduce iterations by 1
    it -= 1

    # shift the system
    if (it > 0):
        _multiDecrypt_Recursive (it, message, alphabet, B, includeNonNElements, V)      

    # return the value after n iterations
    return V

# testing do write it here
a = "1234"
p=[]
for c in a:
    p.append (c)
print (MultiDecrypt_Recursive ("4312", p, 4))
