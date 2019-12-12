import tkProg
import os
from Cipher.MultiLevelCaesarEncrypt import MultiEncrypt, MultiEncrypt_Key

class MultiEncryptMod:
    def __init__(self, alphabet):
        self.Name = "Multi Level Encryption"
        self.AlphabetContainer = alphabet
        
    def MultiEncryptTxt (self):
        # Take inputs
        tkProg.ClearScreen()
        path = input ("input path of txt to encrypt")

        if (not os.path.exists (path)):     # verify that the file exists
            print (path + " does not exist")
            return

        tkProg.ClearScreen()
        outPath = input ("input path to folder output to, leave as blank if you want to output to the program directory")

        if (not os.path.exists (outPath) and outPath != ""):     # verify that the file exists
            print (path + " does not exist")
            return
        tkProg.ClearScreen()
        outFileName = input ("What should the name of the file be, leave blank for default name, do not include file extensions")
        tkProg.ClearScreen()
        alphabet = self.AlphabetContainer.TakeAlphabets()   # take the working alphabet
        tkProg.ClearScreen()
        print ("would you like to import a file with the shifts or implement them manually")
        print ("1) Add them manually")
        print ("2) Take them from a file")
        print ("3) Randomly generate the shifts")
        in1 = input()

        shifts = []

        # take the shifts
        if (in1 == "1"):
            tkProg.ClearScreen()
            print ("Type . to indicate that you are finished")

            completion = 0      # 0 = index 1 = key
            while True:
                ind : int
                key : int

                if (completion == 2):     # add to list   2
                    shifts.append ((ind, key))
                    completion = 0

                inText = "input index " if (completion == 0) else "input key "
                in2 = input(inText)
                if (in2 == "."):        # exit condition
                    break

                if (completion == 0):       # taking index  0
                    ind = int (in2) 
                    completion += 1
                elif (completion == 1):     # taking key    1
                    key = int (in2)
                    completion += 1
        elif (in1 == "2"):
            shiftPath = input ("input path of text file with shifts ")
            
            # check if file exists
            if (not os.path.exists (shiftPath)):
                print ("shift path " + shiftPath + " does not exist")
                return

            inMode = "i"  # i = index k = key

            f = open (shiftPath)

            completion = 0

            lines = f.readlines()

            # reading file of shifts
            for line in lines:
                wL = line.strip()

                ind : int
                key : int

                if (completion == 0):       # taking index  0
                    ind = int (wL)
                    completion += 1
                elif (completion == 1):     # taking key    1
                    # if there are an uneven number of numbers in the file, break the loop and completely forget about what was being added
                    try:
                        key = int (wL)
                    except:
                        break
                    shifts.append ((ind, key))  # add to list
                    completion = 0
                    
            f.close()

        tkProg.ClearScreen()
        print ("opening file...")
   
        value = "" 

        # read the file 

        msg = ""

        with open (path) as f:
            msgA = f.readlines()
            msg = "".join(msgA)

        if (in1 == "3"):
            u = MultiEncrypt (msg, alphabet)
            value = u[0]
            shifts = u[1]
        else:
            value = MultiEncrypt_Key (msg, shifts, alphabet)

        # write the file
        print ("writing the file...")
        T = ""
        if (outFileName == ""):
            T = ("Encryption with key " + str(shifts))  
        else:
            T = outFileName
        filepath = os.path.join (outPath, T) + ".txt"

        f = open (filepath, "w")
        f.writelines (value)
        f.close()

        print ("done!")
        print (value + " encrypted with " + str(shifts))
        input()

    Actions = dict()
    Actions ["Multi encrypt a text file"] = MultiEncryptTxt