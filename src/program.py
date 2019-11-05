# SECTION 5

import argparse
import lib.CaesarEncrypt
import lib.CaeserDecrypt
import lib.MultiLevelCaesarDecrypt
import lib.MultiLevelCaesarEncrypt

# head of the program, will do everything required

def Args ():
    """Handles argument parsing"""
    parser = argparse.ArgumentParser(description="Directly run a process from the run command")
    parser.add_argument("ProcessName" metavar='P', type=str, nargs='+', help="The name of the process to run")
    args = parser.parse_args()
    return args

def init ():
    

    
    