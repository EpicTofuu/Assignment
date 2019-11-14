import os
import tkProg
from Cipher.CaesarDecrypt import Caesar_Decrypt, Caesar_decrypt_Key, Smart_Caesar_Decrypt
from os.path import exists

class CaesarDecryptMod:
    def __init__ (self, alphabet):
        self.Name = "Single Layer Decryption"
        self.AlphabetContainer = alphabet

    def DecryptTxt (self):
        # take inputs
        tkProg.ClearScreen()
        path = input ("input path of txt to decrypt ")
        tkProg.ClearScreen()
        outPath = input ("input path to folder output to, leave as blank if you want to output to the program directory ")
        tkProg.ClearScreen()
        outFileName = input ("What should the name of the file be, leave blank for default name, do not include file extensions ")
        alphabet = self.AlphabetContainer.TakeAlphabets ()  # take the working alphabet
        tkProg.ClearScreen()
        print ("Choose a decryption method")
        print ("1) Find all possible values for all possible keys")
        print ("2) Decrypt with a known key")
        print ("3) Find the most likely key")
        in1 = input()

        msg = []

        # read the file
        if (exists (path)):
            with open (path) as f:
                msg = f.readlines()

            # remove all whitespace characters
            msg = [x.strip() for x in msg]
            
        msgStr = "".join (msg)            
        value = "" 

        if (in1 == "1"):                # brute force
            value = Caesar_Decrypt (msgStr, alphabet)
        elif (in1 == "2"):              # decrypt with known key
            workingKey = input ("what key should be used: ")
            value = Caesar_decrypt_Key (msgStr, alphabet, int(workingKey)) + " - Encrypted using key: " + workingKey
        else:                           # chi squared
            language = input ("which language pack should be chosen, leave blank for English ")
            # TODO maybe have a list of all languages
            if (language == ""):
                language = "English"

            topX = input ("How many top results should be returned, leave as 1 for only the most likely result ")

            value = Smart_Caesar_Decrypt (msgStr, alphabet, language)[int(topX) - 1]             

        print (value)
        input()
        return

    # add actions to dictionary
    Actions = dict()
    Actions ["Decrypt text file"] = DecryptTxt