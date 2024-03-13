myset1 = {0, 1, 2, 3, 4, 5}  # Define the set as myset1

try:
    myset1.remove(1)  # Remove the element from myset1
except KeyError as e:
    print("Key Error:", e)
    print(myset1)
print(myset1)

# exo2:
while True:
    try:
        # Take two integers as input from the user
        num1 = int(input("Enter the first integer: "))
        num2 = int(input("Enter the second integer: "))

        # If both inputs are integers, break out of the loop
        break

    except ValueError:
        print("Invalid input! Please enter integers only.")

# Calculate the sum of the two integers
sum_of_integers = num1 + num2

# Print the sum
print("The sum of", num1, "and", num2, "is:", sum_of_integers)
