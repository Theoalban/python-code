# Pyhon script for LINUX environment
import os #gives access to the operating system
import platform #gives information about the OS like name and version
import sys #allows you to access system-specific functions

#Example of platform module
#import platform 
if  (platform.system() == "Linux"):
    print("This is a Linux System")
    print(f"The hostname is {os.uname().nodename}")
    print(f"The IP Address is {os.popen('hostname -I').read()} ")
    os.system('clear')
else:
    print ("Your platform is windows.")
    os.system('cls') 


#import sys 
print(sys.version) #Print Python version
print(sys.argv)   #Print command line arguments passed to python script
print(sys.arg[1]) #Access second argument from command line
sys.exit() #Exit from python now


_DIR="/var/log"        # Directory to store log files in.
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
                