# SECTION 5

# General collection ! 
# do not write it here
import os
import argparse
import lib.CaesarEncrypt
import lib.CaesarDecrypt
import lib.MultiLevelCaesarDecrypt
import lib.MultiLevelCaesarEncrypt

def Args ():
    """Handles argument parsing"""
    parser = argparse.ArgumentParser(description="Directly run a process from the run command")
    parser.add_argument("ProcessName", metavar="N", type=str, nargs='+', help="The name of the process to run")
    args = parser.parse_args()
    return args
    

print ("Caesar encryption and decryption")
print ()

path = os.path.dirname(__file__)
for f in os.walk(path):
    print (f[0])
