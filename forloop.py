num_v=0 #initilizing  the number of vowels to 0
num_c=0  #initialising the number of consonants to 0
_string = input("Enter a string: ")   #taking user's input
for char in _string.strip():     #iterating through each character in the given string
    if char.lower() in ['a','e','i','o','u']:      #checking whether the current character is a vowel or not
        print(f"{char} is Vowel")      
        num_v +=1                   #if it is, incrementing the count of vowels by 1
    else :                         #else part for 'if' statement
         print(f"{char} is a Consonant")      #printing that the character is a consonant
         num_c +=1                   #and incrementing the count of consonants by 1
print(f"\nNumber of Vowels={num_v}")          #displaying the total number of vowels
print(f"Number of Consonants={num_c}\n")      #displaying the total number of consonants</s>


