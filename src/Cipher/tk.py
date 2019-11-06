""" General toolkit full of general tools *for the library*"""

# Library tk

# list: the list to search
# item: the item to look for
# returns: the index of the item as an integer. For duplicates, only the smallest index will be returned. Returns -1 for unsuccessful operations
# TODO deprecrate if possible
def findIndexInList (L: list, item) -> int:
    """finds the index of an item in a given list"""

    for i in range (len (L)):
        if L[i] == item:
            return i
        
    # return -1 when unsuccessful
    return -1


# s: the string to append to
# c: the character to append
# i: the index to append at, the existing character at i will not be replaced but shifted
def str_append (s: str, c: str, i: int) -> str:
    """ appends a character to a string at an index. This method *returns a value*, it does not set the value automatically TODO"""

    L = list (s)        
    L.insert (i, c)
    value = ""

    for a in L:
        value += str(a)

    return value

def IncrementTuple (tup: tuple, inc: int) -> tuple:
    """Given an upper limit, a tuple can be increased, where an overflow in x will result in an increment in y"""
    x = 0
    y = 0
    if (tup[0] + inc > tup[1]):
        x = inc % tup[1]
        y = tup[1] + 1        
    else:
        x = tup[0] + 1

    return (x,y)
