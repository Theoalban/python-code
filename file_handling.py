##1- use 'w' to write a new file or overwrite an existing file


with open("test.txt",  "w") as f: # create a file named test.txt and Open it in write mode
    f.write("\nHello World!")# add some text to the end of the file
    f.write("\n*This is Python programming language.")
    f.write("\nThank You!")  
#f.seek(0)                #   go back to the beginning of the file
#print(f.read())          # print     again all the contents of the file
                         #            (from the beginning)
f.close()               # close the file when you're done with it.


###2- Use 'a' to append text at the end of the file.
##IMPORTANT: Use 'try' and 'except' to handle potential errors  if the file does not exist.

with open("test.txt",  "a") as f: # create a file named test.txt and Open it in  append mode
    f.write("\nI love Python!")
    f.write("\nHello World!")# add some text to the end of the file
    f.write("\n*This is Python programming language.")
    f.write("\nThank You!")  
#f.seek(0)                #   go back to the beginning of the file
#print(f.read())          # print     again all the contents of the file
                         #            (from the beginning)
f.close()               # close the file when you're done with it.

##3- Use 'r'  to read from a file.
#IMPORTANT: If you use f.write( ) after r, it will give an error 
#IMPORTANT: If you try to change something in the file while reading from it, python will give an error message
#IMPORTANT: If you don’t specify the encoding parameter while opening a file for reading, Python will try to guess the correct encoding 
try:
   with open('test5.txt', 'r') as f: # Open the file in read only mode
    f.readline             # Print the entire content of the file
    f.close
except  FileNotFoundError:
    print ("The file does not exist.")


##4- Use 'r+' to read and modify a file. If the file does not exist raise an IOError exception.
 
try:
    with open('test.txt', 'r+') as f: # Open the file in read & write mode
        content = f.read()           # Read the entire content of the file
        print(content)              # Print the content of the file
        f.seek(0)                   #Use seek () method to change position in the file.
        f.write('\nNew Line added by TheoK.\n')   # Add a new line at the beginning of the file
except IOError:
    print ("The file could not be opened/created.")     

##6- Use dir () function to see what names (variables) are defined in the current scope.
print(dir(f))             # See what methods and properties are associated with the file object.

##7- Use help () function for more information about a specific method or property.
print(help(f.read))               # Get help on the read() method.



'''
f= open("test.txt", "w") # 'w', 'a',  'x', 'r' 
f.write("#this is the first line")
f.write("*this is the second line" \n)
print(f.read())
f.close()

try:
with open("test.txt","a") as f:
    f.write("first line\n")
    f.write("second line\n")
f.close
except:
   print ("check the file name")
'''