# TODO optimise

try:
    import Cipher.tk  
except:
    import tk


# Usables: the number of possible encryptions, larger values imply longer waiting times
def MultiDecrypt_Recursive (message, alphabet, iterations, usables = 1, lan = "English") -> list:
    A = []

    # Generate all possible *decryptions* under the 0th iteration
    for I in range (len(message)):
        for n in range (1, len(alphabet)):
            msg = (tk.EncryptDecryptCoord(message, (I,n), alphabet, tk.Mode.DECRYPT))
            chi = tk.GetChiSquared (msg, lan)
            A.append ((msg, [(I,n)], chi))

    #return A    
    A.sort (key = lambda t: t[2]) # sort to smallest chi index
    L = round (usables)
    A = A[:L]   
    return _multiDecrypt_Recursive (iterations, message, alphabet, A, usables, lan)

def _multiDecrypt_Recursive (it: int, message, alphabet: str, V, usables: int, lan) -> tuple:

    B = []  # contains all *found* elements

    # for each element in A, generate a set of messages using all possible keys
    for e in V:
        for I in range (0, len(message)):
            for n in range (1, len(alphabet)):  # 0 is the identity key, no need to test
                h = []
                h.extend (e[1])
                h.append ((I,n))
                
                deString = tk.EncryptDecryptCoord (e[0], (I, n), alphabet, tk.Mode.DECRYPT)     # decrypted string

                chi = tk.GetChiSquared (deString, lan)

                B.append ((deString, h, chi))

    # Just take the lowest chi squared  
    B.sort (key = lambda t: t[2]) # sort to smallest chi index
    V = B[:usables]         

    # reduce iterations by 1
    it -= 1

    # shift the system
    if (it > 0):
        _multiDecrypt_Recursive (it, message, alphabet, V, usables, lan)   
    
    # return the value after n iterations
    return V + _multiDecrypt_Recursive ()
    # https://stackoverflow.com/questions/32514605/python-list-recursive-changes


# testing do write it here
a = "abcdefghijklmnopqrstuvwxyz "
p=[]
for c in a:
    p.append (c)
print ("starting...")
print (MultiDecrypt_Recursive ("eqpbkugblyegavj b", p, 3, 2))
# original 231
