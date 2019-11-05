# SECTION 2

import tk 

# Decrypts a caeser 
# Returns: a list of tuples that contain both the decrypted message with the corresponding key
def Decrypt (message, __alphabet__):
    
    # create letters array
    __alphabetlist__ = []
    for char in __alphabet__:
        __alphabetlist__.append (char)

    value = []          # list of all possible decryptions

    for key in range (len(__alphabetlist__)):
        decrypted = ""
        for char in message:
            if (__alphabetlist__.__contains__ (char)):
                decrypted = decrypted + __alphabetlist__[tk.findIndexInList (__alphabetlist__, char) - key]

        addable = (decrypted, key)
        value.append (addable)

    return value 
