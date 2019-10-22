Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # TODO implement unicode standard
AlphabetList = []
for n in Alphabet:
    AlphabetList.append (n)

# Finds the index of a given element in an array
# XXX TODO, check if array.Find () is a thing and utilise if it is
def FindInArray (array, element):
    for i in array:
        if (i == element):
            return i

# encrypts the given string "userIn", using the caesar cipher encryption algorithm
# userIn: the string to be encrypted
# key: the number of places to shift each character
# returns: the encrypted string
def Caesar_Encrypt (userIn, key):

    # TODO test other possibilities other than a string list
    
    InList = []     #list to store user input

    # Convert the string input to character list
    for i in userIn:
        InList.append (i)

    # interate over each and every single character in the list
    for a in range (len (InList)):
        # find the index of the letter in the *input*
        inIndex = FindInArray (AlphabetList, a)

        InList[a] = AlphabetList[inIndex + key]

    # conver the list back into a string
    value = ""
    for i in InList:
        value += i

    print (value)

# testing
Caesar_Encrypt ("dong", 3)