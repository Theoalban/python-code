# To interact with the os module, you need to import it first
import os
os.getcwd()
# The function 'os.getcwd()' returns the current working directory of your computer.  
print(f"The Current Working Directory is: {os.getcwd()}") 

# You can change the current working directory using 'os.chdir()'.  
try:
    os.chdir("/Users/johnnydempsey")
    print(f"\nNew Current Working Directory is: {os.getcwd()}")
except FileNotFoundError:
    print("\nFile Not Found Error - Invalid Path Provided.")    

os.mkdir ("MyFolder")  #creates a new folder named "MyFolder".  If this name already exists an error while occurred
os.rmdir ("MyFolder")
# If a folder named "TestFolder" exists in the new CWD and you try to delete it again, Python will raise an OSerror because
# The 'os.rmdir()' function removes a directory if it exists and is empty. If the directory contains files, an OSError will be raised.
