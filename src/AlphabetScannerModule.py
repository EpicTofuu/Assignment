import os 
import pickle
import tkProg
from tkProg import Pause
from AlphabetContainer import AlphabetContainer

class AlphabetScannerMod:
    
    def __init__ (self):      
        self.ALPHABETFILENAME = "alphabets.pickle"
        self.Container = AlphabetContainer()
        if (os.path.exists (self.ALPHABETFILENAME)):
            self.LoadAlphabets ()

    def SaveAlphabets (self):
        """Save the container to a file using pickle"""
        with open (self.ALPHABETFILENAME, "wb") as pickleout:
            pickle.dump (self.Container, pickleout)

    def LoadAlphabets (self):
        """Load the container from a file using pickle"""
        
        with open (self.ALPHABETFILENAME, "rb") as picklein:
            self.Container = pickle.load (picklein)

        # check if the file uses the latest file standard
        if (self.Container.FileVersion != AlphabetContainer.CurrentFileVersion):
            print ("the alphabet file is out of date, please remove it from the program directory")
            self.Container = None
            return

        print (self.Container.Alphabets)   

    def TakeAlphabets (self):
        """used in getting the alphabet during inputs from other moduels"""
        
        print ("Which alphabet would you like to use?")

        inp = ""

        if (len (self.Container.Alphabets) > 0):
            print ("1) Choose from a preloaded list")
            print ("2) Import one right now")
            print ("3) Use the unicode standard")

            inp = input()
        else:
            print ("1) Import one right now")
            print ("2) Use the unicode standard")

            a = int(input()) + 1                # we've just removed option 1, account for this accordingly
            inp = 2 if (a == 1) else str (a)    # if the user has entered 0, they will be sent to the second option anyway

        if (inp == "1"):                # take from list           
            # accounting for all edgecases, should never happen                             
            if (len (self.Container.Alphabets) == 0):
                print ("there are no alphabets available, please add them via the import menu")
                self.TakeAlphabets()
            else:
                print ("which alphabet should be used?")
                for a in range (len(self.Container.Alphabets)):
                    print (str (a + 1) + ") " + self.Container.Alphabets[a][1])

                in1 = input()
                return self.Container.Alphabets[int (in1) - 1][0]

        elif (inp == "2"):              # import one manually      
            self.ImportAlphabets ()
            return self.Container.Alphabets[len(self.Container.Alphabets) - 1][0]   # take the latest created one

        else:                           # unicode
            return ""

    def ImportAlphabets (self):
        tkProg.ClearScreen()
        print ("Import new alphabet")
        print ()
        impPath = input ("Path of alphabet txt: ")
        print ("importing alphabet at " + impPath + "...")

        # check if path exists
        if (not os.path.exists (impPath)):
            print ("not a valid import path")
            return

        n : string  # name of alphabet
        s : string  # store the string that contains the alphabet

        f = open (impPath)
        
        n = None
        s = None

        for _ in f:
            wL = f.read()
            if (wL[0] == "#"):      # hash indicates the name of the alphabet
                n = wL.strip()        
            elif (wL[0] == "$"):    # $ indicates the actual alphabet
                s = wL.strip()
        f.close()

        # check if the alphabet exists
        if (s == None):
            print ("Error, this alphabet is empty, please ensure the alphabet has been marked with the $ indicator")
            return

        # name the alphabet if it hasn't been named already
        if (n == None):
            n = input ("This alphabet is unnamed, please input a name: ")

        #convert the string into an array 
        v=[]
        for c in s:
            v.append (c)

        v.pop (0)   # remove the dollar sign

        # store it all in the container
        self.Container.Alphabets.append ((v, n))
        self.SaveAlphabets ()

        print ("the alphabet has been stored successfully and stored accordingly")
        Pause()
        return

    def ManageAlphabets (self):
        tkProg.ClearScreen()

        l = len (self.Container.Alphabets)
        if (l == 0):
            print ("there are no alphabets, add some using the import menu")
            Pause()
            return
        else:
            for a in range (l):
                print (str (a + 1) + ") " + self.Container.Alphabets[a][1])

        inp = input("Which would you like to delete?")
        self.Container.Alphabets.pop (int (inp) - 1)
        self.SaveAlphabets ()
        print ("successfully deleted")
        Pause()
        return

        
    Actions = dict()
    Actions ["Import an alphabet"] = ImportAlphabets
    Actions ["Manage current alphabets"] = ManageAlphabets
        


    
                    