# SECTION 1

# TODO remove comments
import tk
import random
import enum

# XXX TODO remove *please*
alphabetList = []

class Encoding (enum.Enum):
    Custom = 0  
    Unicode = 1
    ASCII = 2

# userIn: the string to be encrypted
# returns: a tuple with the encrypted message and the key in that order
def Caesar_Encrypt (userIn):
    """encrypts the given string "userIn" using a randomly generated key. Encrypts on Unicode by default"""

    k = random.randrange(0, 100)
    return Caesar_Encrypt_Key (userIn, k, Encoding.Unicode)

# TODO remove
def Set_Custom_Charset (charset):
    alphabetList.extend(charset)

# TODO clean up if possible

# encrypts the given string "userIn", using the caesar cipher encryption algorithm
# userIn: the string to be encrypted.
# key: the number of places to shift each character
# returns: the encrypted string
def Caesar_Encrypt_Key (userIn, key, encoder):  
    InList = []     #list to store user input

    # Convert the string input to character list
    for i in userIn:
        InList.append (i)

    if (encoder == Encoding.Unicode):
        for a in range (len(InList)):
            inIndex = ord (InList[a])                   # find the index of the letter in the *input*
            InList[a]= chr((inIndex + key) % 137439)    # convert back to character TODO fix modulo operator    
    elif (encoder == Encoding.ASCII):
        # TODO
        raise Exception ("not implemented yet")
    elif (encoder == Encoding.Custom):
        for a in range (len (InList)):
            # find the index of the letter in the *input*
            inIndex = tk.findIndexInList (alphabetList, InList[a])

            # check if the character is supported
            if (inIndex == -1):
                raise Exception ("Character not supported")

            InList[a] = alphabetList[(inIndex + key) % len(alphabetList)]       

    # convert the list back into a string
    value = ""
    for i in InList:
        value += i

    return value

'''
# Example:

# create the alphabet
_customAlphabetstr_ = "新大久保"   
_customAlphabet_ = []
for c in _customAlphabetstr_:
    _customAlphabet_.append (c)
Set_Custom_Charset (p)

# print
print (Caesar_Encrypt_Key ("大大久保新久新新大新", 1, Encoding.Custom))


print (Caesar_Encrypt_Key ("My name is yun", 24, Encoding.Unicode))
# TODO: fix line breaks
'''