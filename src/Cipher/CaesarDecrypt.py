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

def Smart_Caesar_Decrypt (message, alphabet, lan = "English", giveTuple = True):
	"""
	uses the chi squared algorithm to sort keys based on the probability of them returning a word in a given language.
	Language distribution packs can be added to the LanguageCharDistributions folder in the library
	Returns a tuple in the form (decryption, chi index, key)
	"""

	value = []                              # used to hold all combinations, with respective chi indexes and keys
	
	# iterate over all keys
	for key in range (0, len (alphabet)):   
		msg = Caesar_decrypt_Key (message, alphabet, key)

		# Get the chi index for the decrypted string
		chiIndex = tk.GetChiSquared (msg, lan)
		
		v = (msg, chiIndex, key)
		value.append (v)    # append the item to the value list

	value.sort (key = lambda t: t[1]) # sort to smallest chi index

	# return the value as required
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


# EXAMPLE
# testing do write it here
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
p=[]
for c in a:
	p.append (c)

o = Smart_Caesar_Decrypt ("GRQCLVCVPDUW", p)

print (o)

print ("done!")  

	