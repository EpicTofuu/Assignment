# SECTION 2

# finds the index of an item in a given array
def findIndexInArray (array, item):
    for i in range (len (array)):
        if array[i] == item:
            return i
        
    return -1

# Decrypts a caeser 
# Returns: a list of tuples that contain both the decrypted message with the corresponding key
def Decrypt (message, __alphabet__):
    
    # create letters array
    __alphabetlist__ = []
    for char in __alphabet__:
        __alphabetlist__.append (char)

    possibledecryptions = []        # list of all possible keys
    value = []                      # character array of current value

    for key in range (len(__alphabetlist__)):
        decrypted = ""
        for char in message:
            if (__alphabetlist__.__contains__ (char)):
                decrypted = decrypted + __alphabetlist__[findIndexInArray (__alphabetlist__, char) - key]

        addable = (decrypted, key)
        value.append (addable)

    return value 
