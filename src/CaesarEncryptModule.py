import tk
from os.path import exists
from Cipher.CaesarEncrypt import Caesar_Encrypt, Caesar_Encrypt_Key

# TODO have a way of publically inputting an alphabet

class CaesarEncryptMod ():

    Actions = dict() 
    
    def __init__ (self):
        self.Name = "Caesar Encryption"

    def nekSelf (self):
        print ("die")

    def EncryptTxt (self):
        # take inputs
        tk.ClearScreen()
        path = input ("input path of txt to encrypt")
        tk.ClearScreen()
        outPath = input ("input path to output to, leave as blank if you want to output to the program directory")
        tk.ClearScreen()
        # TODO add a way to input the key into the file
        key = input ("input the value of the key to encrypt with, leave as blank for a randomly generated key")
        alphabetPath = input ("input path to alphabet, leave as blank for UNICODE standard")

        value = "" 
        alphabet = []

        # TODO move this into an alphabet class
        if (exists (alphabetPath)):
            f = open (path)
            alphabetStr = f.readline
            for c in alphabetStr:
                alphabet.append (c)

        # read the file 
        if (exists (path)):     # verify that the file exists
            input ("this file does not exist")
            f = open (path)
            msg = f.readline ()

            if (key == ""):
                u = Caesar_Encrypt (msg, alphabet)
                value = u[0]
                key = u[1]
            else:
                value = Caesar_Encrypt_Key (msg, key, alphabet)
        else:
            print ("The file does not exist, please try again")
            return

        print ("The encrypted message is " + value + " and it was encrypted using key " + key)
        
        # TODO writing to file
        # TODO have cmd style file navigation, just use os.system
        
        return
                    
    # add actions to the dictionary
    Actions ["Encrypt text file"] = EncryptTxt
    Actions ["Literally die"] = nekSelf

    