# To use the 'Command' function defined in myFunction.py, you need to import "myFunction" module:
import myFunction as mf
# Now you can call any of its functions using dot notation (e.g., mf.function_name())
print(mf.Command("ls"))  # This will run the "ls" command on your system and print out the result.
 
 # or
result = mf.Command("pwd")
print(result)

#     Best practice
from myFunction import Command,hello
Command('pwd')
hello()
from os import system,mkdir
mkdir('folder1') #creates a folder named 'folder1' in the current directory.
system("cd folder1")#changes the working directory to 'folder1'.
#system("cls")  #  Clear the screen for windows.
#system('clear') # Clear the screen for Unix systems.