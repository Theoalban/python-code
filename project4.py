zip_code = input("Please enter your ZIP code: ")
l = len(zip_code)

try:
    zip_code_cast=int(zip_code) #Try to convert the user's entry into an integer.
    if l == 5:
       print("Your entry is valid")
    else:
       print("Please enter a valid entry")
except ValueError:
    print("ValueError, please only use numbers")
    #if a ValueError occurs during the conversion(non-numeric characters) , the code inside the except block is executed as part of error handling.

    #sol2:
                        
while True:
    zip_code = input("Please enter a zip code: ")
    z_1 = len(zip_code.strip())
    z_2 = zip_code.isdigit()
    
    if z_1==5 and z_2:
        print("Zip Code is Valid!")
        break
    elif not z_2:
        print("Only digits are allowed.")
    