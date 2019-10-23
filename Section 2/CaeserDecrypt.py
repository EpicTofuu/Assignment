# additional functions
def findIndexInArray (array, item):
    for i in range (len (array)):
        if array[i] == item:
            return i
        
    return -1

# create letters array
l = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = []
for char in l:
    alphabet.append (char)

possibledecryptions = []

# Decrypts a caeser 
# Returns: a list of tuples that contain both the decrypted message with the corresponding key
def Decrypt (message):
    value = []

    for key in range (len(alphabet)):
        decrypted = ""
        for char in message:
            if (alphabet.__contains__ (char)):
                decrypted = decrypted + alphabet[findIndexInArray (alphabet, char) - key]

        addable = (decrypted, key)
        value.append (addable)

    return value 

print (Decrypt ("ENAHLXXUMXWP"))

# TODO
#def SmartDecrypt (message)