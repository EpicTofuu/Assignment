message =  "YHUBORQJGRQJHSLF"

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

# do the stuff
for key in range (len(alphabet)):
    decrypted = ""
    for char in message:
        if (alphabet.__contains__ (char)):
            decrypted = decrypted + alphabet[findIndexInArray (alphabet, char) - key]

    print (decrypted + " with key " + str(key))

