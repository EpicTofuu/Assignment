# SECTION 3

# no need to rewrite what's already been written
import tk
import CaesarEncrypt

from CaesarEncrypt import Caesar_Encrypt_Key
from CaesarEncrypt import Set_Custom_Charset

# shift tuple: (index, key)
def MultiEncrypt_Recursive (message, shifts, alphabet):
    Set_Custom_Charset (alphabet)       # TODO just implement this into the method's argument
    return str(__multiEncrypt (message, shifts, alphabet))

# recursive definition, remove this method once Set_Custom_Charset is removed
# message: the message to be encrypted
# shifts: a list of tuples (i, k) where i is the index (from 0) and k is the key
# alphabet: the custom alphabet to work with 
# returns: encrypted string
# TODO explore the idea of using a stack for shifts
def __multiEncrypt (message, shifts, alphabet):
    workingshift = shifts[0]

    # shift the selected values by the key
    value = Caesar_Encrypt_Key (message[workingshift[0]:], workingshift[1], CaesarEncrypt.Encoding.Custom)
    
    # rebuild the non encrypted parts of the message
    for i in range (workingshift[0]):
        value = tk.str_append (value, message[i], i)

    # remove current shift
    shifts.pop (0)

    # continue recursing if there are still tuples to process
    if (len(shifts) != 0):
        __multiEncrypt (value, shifts, alphabet)
        
    #return string
    return str(value)

'''
# testing
a = "1234567890"
p=[]
for c in a:
    p.append (c)

Set_Custom_Charset (p)       # TODO just implement this into the method's argument
ere = MultiEncrypt_Recursive ("234567", [(3, 5)], p)
print (ere)
'''