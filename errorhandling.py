#use a try-except block to catch the error and handle it gracefully.
#a=1
try:
   print(a)
except Exception as e:  #catching an error when variable 'a' is not defined
   print("The variable 'a' is not defined.")
