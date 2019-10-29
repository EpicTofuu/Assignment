# TODO remove comments
import random
import enum

alphabetList = []

class Encoding (enum.Enum):
    Custom = 0  
    Unicode = 1
    ASCII = 2

# TODO deprecrate if possible
def _findIndexInArray (array, item):
    for i in range (len (array)):
        if array[i] == item:
            return i
        
    return -1

# encrypts the given string "userIn" using a randomly generated key
# userIn: the string to be encrypted
# returns: a tuple with the encrypted message and the key in that order
def Caesar_Encrypt (userIn):
    k = random.randrange(0, 100)
    return (Caesar_Encrypt_Key (userIn, k), k)

# TODO remove
def Set_Custom_Charset (charset):
    alphabetList.extend(charset)

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
            inIndex = _findIndexInArray (alphabetList, InList[a])

            # check if the character is supported
            if (inIndex == -1):
                raise Exception ("Character not supported")

            InList[a] = alphabetList[(inIndex + key) % len(alphabetList)]       

    # convert the list back into a string
    value = ""
    for i in InList:
        value += i

    return value

# testing
k = "新大久保"
p = []
for c in k:
    p.append (c)
Set_Custom_Charset (p)
print (Caesar_Encrypt_Key ("大大久保新久新新大新", 1, Encoding.Custom))
