# SECTION 2

import os
import os.path
import pickle
import tk 

def _importLanguage (language) -> dict:
    value = dict() 
    lines = []

    dirName = os.path.dirname (__file__)
    
    # Find languages
    languagePath = os.path.join (dirName, "LanguageCharDistributions", language) + ".txt"
    if (not os.path.exists (languagePath)):
        raise Exception (languagePath + " does not exist")
    
    f = open (languagePath, encoding="utf-8")
    #HasCapitals = f.readline() != "!"    # does the language have capitals? Really only important for non-european languages where the alphabet does not contain capitals

    for l in f:
        if (l[0] != "="): 
            lines.append (l)

    for i in range (0, len (lines), 2):
        letter = lines[i].strip()
        freq = lines [i + 1].strip()

        value [letter] = freq

    return value


# Returns: a list of tuples that contain both the decrypted message with the corresponding key
def Caesar_Decrypt (message, alphabet):    
    """Decrypts the given string using the caesar cipher algorithm"""
    value = []          # list of all possible decryptions

    for key in range (len(alphabet)):
        decrypted = Caesar_decrypt_Key (message, alphabet, key)

        addable = (decrypted, key)
        value.append (addable)

    return value 

def Smart_Caesar_Decrypt (message, alphabet, language = "English", giveTuple = True):
    """
    uses the chi squared algorithm to sort keys based on the probability of them returning a word in a given language.
    Language distribution packs can be added to the LanguageCharDistributions folder in the library
    Returns a tuple in the form (decryption, chi index, key)
    """

    value = []                              # used to hold all combinations, with respective chi indexes and keys
    LanDist = _importLanguage (language)    # list of all characters with their frequency distributions
    
    # iterate over all keys
    for key in range (0, len (alphabet)):   
        chiIndex = 0
        msg = Caesar_decrypt_Key (message, alphabet, key)

        # iterate over all characters *in the language distribution file*
        for alpha in LanDist:                   

            # Get a list of all characters that are in the string that are not included in the distribution file 
            # (this is to prevent the calculations of longer message lengths that throw off the chi algorithm with symbols)
            voidChar = 0
            for char in msg:
                if (not list (LanDist.keys()).__contains__ (char.upper())):
                    voidChar += 1

            c = msg.count (alpha) + msg.count (alpha.swapcase())                            # include both lowercase and uppercase                                                      Actual count
            e = (len(msg) - voidChar) * float (LanDist [alpha]) if float(LanDist[alpha]) > 0 else 0.01   # prevent a division by zero on the off chance the frequency distribution is zero           Expected count

            # using the chi-squared formula
            chiIndex += ((c - e) ** 2) / e

        v = (msg, chiIndex, key)
        value.append (v)    # append the item to the value list

    value.sort (key = lambda t: t[1]) # sort to smallest chi index

    if (not giveTuple):
        return value[0]
    
    return value

def Caesar_decrypt_Key (message, alphabet, key):
    """decrypts a string using a given key"""
    decrypted = "" 
    for char in message:
        if (alphabet.__contains__ (char)):
            decrypted = decrypted + alphabet[tk.findIndexInList (alphabet, char) - key]

    return decrypted

'''
# EXAMPLE
# testing do write it here
a = "abcdefghijklmnopqrstuvwxyz "
p=[]
for c in a:
    p.append (c)
o = Smart_Caesar_Decrypt ("very cool and good yes yes", p, "English", False)

print (o)

print ("done!")  
'''
    