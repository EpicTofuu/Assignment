import tkProg
import os
from os.path import exists
from Cipher.CaesarEncrypt import Caesar_Encrypt, Caesar_Encrypt_Key

# TODO have a way of publically inputting an alphabet

class CaesarEncryptMod ():

    Actions = dict() 
    
    def __init__ (self, alphabet):
        self.Name = "Caesar Encryption"
        self.AlphabetContainer = alphabet

    def EncryptTxt (self):
        # take inputs
        tkProg.ClearScreen()
        path = input ("input path of txt to encrypt")
        tkProg.ClearScreen()
        outPath = input ("input path to output to, leave as blank if you want to output to the program directory")
        tkProg.ClearScreen()
        # TODO add a way to input the key into the file
        key = input ("input the value of the key to encrypt with, leave as blank for a randomly generated key")
        
        alphabet = self.AlphabetContainer.TakeAlphabets ()
            
        value = "" 

        # read the file 
        if (exists (path)):     # verify that the file exists
            os.path.join (outPath, "encrypted.txt")
            f = open (path)
            msg = f.readline ()

            if (key == ""):
                u = Caesar_Encrypt (msg, alphabet)
                value = u[0]
                key = u[1]
            else:
                value = Caesar_Encrypt_Key (msg, int(key), alphabet)
        else:
            print ("The file does not exist, please try again")
            return

        T = "Encryption with key " + key
        filepath = os.path.join (outPath, T) + ".txt"
        f = open (filepath, "w")
        f.writelines (value)
        f.close()

        print ("The encrypted message is " + value)
        print ("Key: " + key)
        print ("The file has been written to " + filepath)

        # TODO have cmd style file navigation, just use os.system
        
        return 1
                    
    # add actions to the dictionary
    Actions ["Encrypt text file"] = EncryptTxt

    