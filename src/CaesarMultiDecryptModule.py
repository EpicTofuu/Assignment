from Cipher.MultiLevelCaesarDecrypt import MultiDecrypt
import os
import tkProg
from datetime import datetime

class MultiDecryptMod:

    def __init__(self, alphabet):
        self.Name = "Multi Level Decryption"
        self.AlphabetContainer = alphabet

    def MultiDecryptTxt (self):
        # take inputs
        tkProg.ClearScreen()
        path = input ("input path of txt to decrypt ")
        tkProg.ClearScreen()
        outPath = input ("input path to folder output to, leave as blank if you want to output to the program directory ")
        tkProg.ClearScreen()
        outFileName = input ("What should the name of the file be, leave blank for default name, do not include file extensions ")
        alphabet = self.AlphabetContainer.TakeAlphabets ()  # take the working alphabet
        tkProg.ClearScreen()
        print ("working...")

        v = []

        # read the file and encrypt
        if (os.path.exists (path)):     # verify that the file exists
            f = open (path, "r")
            msgs = []
            msgs = f.readlines ()

            for msg in msgs:
                v.append (MultiDecrypt (msg, alphabet))
        else:
            print ("The file does not exist, please try again")
            return

        # write file
        T = ""
        if (outFileName == ""):
            T = "Multi decryption done at " + str(datetime.now())
        else:
            T = outFileName
        filepath = os.path.join (outPath, T) + ".txt"

        f = open (filepath, "w")
        for i in v:
            f.writelines (str(i[0]) + " " + str(i[1]) + " "+ str(i[2]))
        f.close()

        print ("done!")
        print (v)
        input()

    Actions = dict()
    Actions["Multi decrypt a text file"] = MultiDecryptTxt