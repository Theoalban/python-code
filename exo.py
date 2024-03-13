
import os

def Command(cmd):
    os.system(cmd)

if __name__ == "__main__":
    Command("ls") # list the contents of the current directory in Linux. 'ls' is not recognized on windws
