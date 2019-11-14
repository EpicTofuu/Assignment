# SECTION 2

import os
import os.path
import pickle
from Cipher.tk import findIndexInList, GetChiSquared

# Returns: a list of tuples that contain both the decrypted message with the corresponding key
def CaesarDecrypt (message, alphabet):    
	"""Decrypts the given string using the caesar cipher algorithm"""
	value = []          # list of all possible decryptions

	for key in range (len(alphabet)):
		decrypted = CaesarDecryptKey (message, alphabet, key)

		addable = (decrypted, key)
		value.append (addable)

	return value 

def SmartCaesarDecrypt (message, alphabet, lan = "English", yieldSize = None):
	"""
	uses the chi squared algorithm to sort keys based on the probability of them returning a word in a given language.
	Language distribution packs can be added to the LanguageCharDistributions folder in the library
	Returns a tuple in the form (decryption, chi index, key)
	"""

	value = []                              # used to hold all combinations, with respective chi indexes and keys
	
	# iterate over all keys
	for key in range (len (alphabet)):   
		msg = CaesarDecryptKey (message, alphabet, key)

		# Get the chi index for the decrypted string
		chiIndex = GetChiSquared (msg, lan)
		
		v = (msg, chiIndex, key)
		value.append (v)    # append the item to the value list

	value.sort (key = lambda t: t[1]) # sort to smallest chi index

	yS = 0 if (yieldSize is None) else yieldSize + 1

	# return the value as required
	return value [:yS] 

def CaesarDecryptKey (message, alphabet, key):
	"""decrypts a string using a given key"""
	decrypted = "" 
	for char in message:
		if (alphabet.__contains__ (char)):
			decrypted = decrypted + alphabet[findIndexInList (alphabet, char) - key]

	return decrypted

'''
# EXAMPLE
# testing do write it here
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
p=[]
for c in a:
	p.append (c)

o = SmartCaesarDecrypt ("GRQCLVCVPDUW", p)

print (o)

print ("done!")  
'''