# SECTION 2

import tk 

# Returns: a list of tuples that contain both the decrypted message with the corresponding key
def Caesar_Decrypt (message, alphabet):    
    """Decrypts the given string using the caesar cipher algorithm"""
    value = []          # list of all possible decryptions

    for key in range (len(alphabet)):
        decrypted = "" 
        for char in message:
            if (alphabet.__contains__ (char)):
                decrypted = decrypted + alphabet[tk.findIndexInList (alphabet, char) - key]

        addable = (decrypted, key)
        value.append (addable)

    return value 
