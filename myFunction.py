# Defining functions without  calling  them, and use them  later
# Functions are like boxes that hold code. You can put your code in the box and then call it whenever you want to run that code.
# We will use them in myscript.py
def hello():
    print("hello Dianna")
    print("how are you?")
    
def hello3(name):
    print(f"hello {name}")
    print("how are you?")

def Command(cmd):
    import os
    os.system(cmd)