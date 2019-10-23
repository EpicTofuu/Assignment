import random

Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # TODO implement unicode standard
AlphabetList = []
for n in Alphabet:
    AlphabetList.append (n)

# Finds the index of a given element in an array
# XXX TODO, check if array.Find () is a thing and utilise if it is
def FindInArray (array, element):
    for i in range (len (array)):
        if (array[i] == element):
            return i

# encrypts the given string "userIn" using a randomly generated key
# userIn: the string to be encrypted
def Caesar_Encrypt (userIn):
    k = random.randrange(0, 100)
    return Caesar_Encrypt_Key (userIn, k)

# encrypts the given string "userIn", using the caesar cipher encryption algorithm
# userIn: the string to be encrypted.
# key: the number of places to shift each character
# returns: the encrypted string
def Caesar_Encrypt_Key (userIn, key):

    # TODO test other possibilities other than a string list
    
    InList = []     #list to store user input

    # Convert the string input to character list
    for i in userIn:
        InList.append (i)

    # interate over each and every single character in the list
    for a in range (len (InList)):        
        # find the index of the letter in the *input*
        inIndex = FindInArray (AlphabetList, InList[a])

        # check if the character is supported
        if (type (inIndex) != int):
            raise Exception ("Character not supported")

        InList[a] = AlphabetList[(inIndex + key) % len(AlphabetList)]

    # conver the list back into a string
    value = ""
    for i in InList:
        value += i

    return value

# testing
text = input()
print (Caesar_Encrypt (text))