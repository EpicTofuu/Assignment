# SECTION 3

from CaesarEncrypt import Caesar_Encrypt_Key
from CaesarEncrypt import Set_Custom_Charset
from CaesarEncrypt import Encoding

# shift tuple: (index, key)
def MultiEncrypt (message, shifts, alphabet):
    value = []                      # character array of final value
    for i in range (len(shifts)):
        Set_Custom_Charset (alphabet)       # TODO just implement this into the method's argument
        value.append (Caesar_Encrypt_Key (message[shifts[i][0]:], shifts[i][1], Encoding.Custom))

    return value

# testing

a = "abcdefghijklmnopqrstuvwxyz"
p=[]
for c in a:
    p.append (c)

print (MultiEncrypt ("dongstyle", [(2, 5)], p))

# TODO current returns encrypted elements from x and will return |message| - x characters
    