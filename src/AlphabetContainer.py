import pickle

class AlphabetContainer:
    CurrentFileVersion = "20191112"

    def __init__ (self):
        self.FileVersion = AlphabetContainer.CurrentFileVersion     # current file version. Subject to change as class structure changes
        self.Alphabets = []                                         # List of all alphabet, id tuples