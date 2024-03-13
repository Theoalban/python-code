
#You initialize a dictionary d containing information about a person.
d = {'name': 'Serge', 'age': 30, 'profession': 'DevOps Engineer', 'courses': ['aws', 'linux', 'terraform']}
#The while True: loop ensures that the program continuously asks the user for input until the user enters 'q' to quit
while True:
    user_input = input("Enter your Nationality or q to quit : ")
    if user_input == "q": #If the user enters 'q', the loop breaks and the program terminates.
        break
    else:
        if 'nationality' not in d: #Checks whether 'nationality' is already  a key in the dictionary.
            d['nationality'] = [] #If it isn't, adds it with an empty list as its value.
        d['nationality'].append(user_input) #Adds the user's input to the list of nationalities for that person.
print(d['nationality']) #Prints the value of 'nationality'.
print(d) #Prints the entire dictionary.

    