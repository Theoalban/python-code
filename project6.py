#Exercise 1

#What if the user enter a floating number instead of an integer?
#use a try-except block to catch the error and handle it gracefully.
# use the while  loop to make sure that the user enters an integer.

while  True:
    try:
        num1 = int(input("Enter the first integer: "))
        num2 = int(input("Enter the second integer: "))
        break  # If both inputs are integers, break out of the loop
    except ValueError:
        print("Invalid input. Please enter integers only.")
# Calculate the sum of the two integers
sum_of_integers = num1 + num2

# Display the result
print("The sum of", num1,"and",num2,"is",sum_of_integers)
