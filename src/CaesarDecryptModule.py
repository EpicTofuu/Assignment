import os
import tkProg
import datetime
from Cipher.CaesarDecrypt import CaesarDecrypt, CaesarDecryptKey, SmartCaesarDecrypt
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
            value = CaesarDecrypt (msgStr, alphabet)
        elif (in1 == "2"):              # decrypt with known key
            workingKey = input ("what key should be used: ")
            value = CaesarDecryptKey (msgStr, alphabet, int(workingKey)) + " - Encrypted using key: " + workingKey
        else:                           # chi squared
            language = input ("which language pack should be chosen, leave blank for English ")
            # TODO maybe have a list of all languages
            if (language == ""):
                language = "English"

            topX = input ("How many top results should be returned, leave as 1 for only the most likely result ")

            value = SmartCaesarDecrypt (msgStr, alphabet, language, int(topX) - 1)             

        # write file
        print ("writing...")
        # output the file
        T = ""
        if (outFileName == ""):
            T = "Single layer encryption at " + str(datetime.datetime.now())
        else:
            T = outFileName
        filepath = os.path.join (outPath, T) + ".txt"
        f = open (filepath, "w")
        for i in value:
            f.write (str(i[0]) + " with key " + str(i[1]) + "\n")
        f.close()

        print (value)
        return

    # add actions to dictionary
    Actions = dict()
    Actions ["Decrypt text file"] = DecryptTxt