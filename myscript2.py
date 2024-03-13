# To use the 'Command' function defined in myFunction.py, you need to import "myFunction" module:
import myFunction as mf
# Now you can call any of its functions using dot notation (e.g., mf.function_name())
print(mf.Command("ls"))  # This will run the "ls" command on your system and print out the result.
 
 # or
result = mf.Command("pwd")
print(result)

