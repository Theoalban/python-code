# Defining functions without  calling  them, and use them  later
# Functions are like boxes that hold code. You can put your code in the box and then call it whenever you want to run that code.
# We will use them in myscript.py

import os

def hello():
    print("hello Dianna")
    print("how are you?")
    
def hello3(name):
    print(f"hello {name}")
    print("how are you?")

def Command(cmd):
    os.system(cmd)

def list_files(dir_path):     # This function lists all files in the current directory # Also list directories
    
    _DIR=dir_path          # Directory to store log files in.
    #_LOGFILE="test.log"     # Name of the log file.

    listing = os.listdir(_DIR)    # Get a list of all filenames in DIR.
    BLUE = "\033[94m"        # ANSI Blue color code.
    RESET = "\033[0m"         # Reset to normal color.


    for item in os.listdir(_DIR):   # iterate over all items in the directory

           path = os.path.join(_DIR, item)   # Join the base dir with each individual item 
           if os.path.isfile(path):                  # and check if it is a regular file (i.e., not a subdirectory).
                        print(f"{path} is a file")     # Print out if it's a regular file 
           else:
                        print(f"{BLUE}{path}{RESET} is a directory") # If not, then it's a directory
list_files("/etc") # Calling our function with an argument /etc as example
                