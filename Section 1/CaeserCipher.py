import random
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
    InList = []     #list to store user input

    # Convert the string input to character list
    for i in userIn:
        InList.append (i)

    # interate over each and every single character in the list
    for a in range (len (InList)):  
        inIndex = ord (InList[a])                   # find the index of the letter in the *input*
        InList[a]= chr((inIndex + key) % 137439)    # convert back to character    

        # legacy implementation (Only capable of capital alphabet bAD)
        '''      
        # find the index of the letter in the *input*
        inIndex = FindInArray (__alphabetList__, InList[a])

        # check if the character is supported
        if (type (inIndex) != int):
            raise Exception ("Character not supported")

        InList[a] = __alphabetList__[(inIndex + key) % len(__alphabetList__)]
        '''

    # convert the list back into a string
    value = ""
    for i in InList:
        value += i

    return value

# testing
text = input("input")
print (Caesar_Encrypt (text))
