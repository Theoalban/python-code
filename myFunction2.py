def hello1(): 
    print("Hello World!")
    print("Hello Theo")
hello1()
print(type(hello1)) #<class 'function'>    

#Function with parameters
def hello2(name):
    print(f"Hello, {name}!")
    print("how are you?")
hello2("John")

#NOTE: Run this code on command line using >python filename.py to execute it.
# Because we need to provide a Linux command(eample: ls)
import os
def Command2(cmd):
    os.system(cmd)
if __name__ == "__main__":
    Command2("ls") # list the contents of the current directory in Linux. 'ls' is not recognized on windws

def Command2(cmd):
    import os
    os.system(cmd)
Command2("dir") # list the contents of the current directory in Windows.

#Recursive function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))


## Functions in Python(Block of organized, reusable code used to perform a specific task)
# 1-User-defined functions (UDF)
def welcome():  # define a function named welcome
    print('Hi!! Welcome to our python course')
# Call the welcome function
welcome()

def hello():  # define a function named hello
    print('Hello everyone!')
# Call the hello function
hello()

# 2-Built-in functions(float(), input(), int(), print(), str(), type(), format(), sum())

# function arguments in python
# 1-Positional Arguments
def greet(name, message):
    print(f"Hello, {name}! {message}")
greet("Alice", "How are you?")

# 2-Keyword Arguments:specify which parameter each argument should be assigned to when calling a function.
def divide(a, b):
    return a / b
quotient1 = divide(a=2, b=5)  # keyword arguments a=2 and b=5
print('quotient1 value is:', quotient1)
quotient2 = divide(a=5, b=2)
print('quotient2 value is:', quotient2)  # keyword arguments a=5 and b=2

def greet(name, message):
    print(f"Hello, {name}! {message}")
greet(message="How are you?", name="Alice")

# 3- Keyword-only Arguments (use the *)
def greet(name, *, message="How are you?"):
    print(f"Hello, {name}! {message}")
greet("Alice", message="Nice to meet you!")

# 4-Default Arguments
def greet(name, message="How are you?"):  # The greet function takes 2 parameters 'name' and 'message'.The parameter 'message' has a default value 'How are you?'
    print(f"Hello, {name}! {message}")
greet("Alice")  # Output: Hello, Alice! How are you? ie Since the 'message' parameter is not provided, it will default to 'How are you?'

def add_num(a, b=2):
    return a + b
add1 = add_num(a=1)
print(add1)  # sol: 1+2=3, since the b parameter is not provided in add1, we use the defaul ie 2
add2 = add_num(a=1, b=3)
print(add2)  # sol: 1+3=4

# 4-Variable-length Arguments Or Variable number of arguments( allowing a function to accept an arbitrary number of arguments)
def add_num(*args):
    return sum(args)
sum_args = add_num(2, 4, 6, 8)
print('the sum of arguments is: ', sum_args)  # sol: the sum of arguments is:  20

def add_num(*args):
    total = 0
    for i in args:
        total += i
    return total
sum_args = add_num(2, 4, 6, 8)
print('the sum of arguments is: ', sum_args)  # sol: the sum of arguments is:  20

def greet(*names):
    for name in names:
        print(f"Hello, {name}!")
greet("Alice", "Bob", "Charlie")  # We will have 3 outputs Hello, Alice! Hello, Bob!, Hello, Charlie!

# 6-Required arguments: These arguments are mandatory, meaning that the function will raise an error if their values are not provided when the function is called.
def devide(a, b):  # Both a and b are required arguments
    return a / b
quotient = devide(8, 10)  # If you call the function devide without providing values for a and b, Python will raise an error.
print(quotient)  # Output: 0.8

###Global Variables:
### are accessible throughout the entire program, including inside functions. They are defined outside of any function.
###They are created when the program starts execution and are destroyed when the program terminates.
### can be accessed and modified from anywhere in the program, including within functions.
###Local Variables
###are defined within a function and are only accessible within that function's scope. They cannot be accessed from outside the function.
###are created when the function is called and exist only until the function finishes executing. They are destroyed (or garbage-collected) once the function exits
### are accessible only within the function in which they are defined. They cannot be accessed from outside the function
global_var = 10  # Global variable
def my_function():
    local_var = 20  # Local variable
    print("Inside function:", global_var)  # Accessing global variable
    print("Inside function:", local_var)  # Accessing local variable
my_function()
print("Outside function:", global_var)  # Accessing global variable outside function

###Return statement: used to exit a function and return a value (or values) to the caller.
# 1-Returning a Single Value:
def add(a, b):
    return a + b
result = add(3, 5)
print(result)  # Output: 8

def square(x):
    return x * x
result = square(4)
print(result)  # output 16

# 2-Returning Multiple Values:
def divide(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder
q, r = divide(10, 3)
print("Quotient:", q)  # Output: 3
print("Remainder:", r)  # Output: 1

# 3-Exiting Early:
def check_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
result = check_even(5)
print(result)  # Output: False

# 4-Returning None:
def do_nothing():
    return
result = do_nothing()
print(result)  # Output: None

# 5-Returning Early:
def process_data(data):
    if not data:
        return
    # Process data here


result = process_data([])
print(result)  # Output: None

###Exercices (Functions)
# 1- Write a code to display the first parameter
def my_function1(first_name, last_name):
    print("First name:", first_name)
my_function1("Theo", "K") #output: First name: Theo

#2- Complete the code to let the function return the x parameter + 18
def my_function2(x):
    return x + 18
result =my_function2(5)
print(result) # Output: 23

#3- Write a Python function to summarize all the numbers of a list
def summarize_numbers(num_list):
    total = 0
    for num in num_list:
        if isinstance(num, (int, float)): #For each element, it checks if it's an integer or a float using isinstance(num, (int, float))
            total += num
    return total

# Test the function
numbers = [1, 2, 3, 4, 5]
result = summarize_numbers(numbers)
print("Sum of numbers:", result)  # Output: Sum of numbers: 15

#4-If you do not know the number of arguments that will be passed into a function(add the prefix *)
def my_function3(*kids):
    print("The youngest child is " + kids[4])
my_function3("John", "Doe", "Alice", "Bob", "Eve") #output: .....Eve

#5- Write a Python function called max_two that return the maximum of two numbers
def max_two(a, b):
    if a > b:
        return a
    else:
        return b
# Test the function
num1 = 10
num2 = 20
print("Maximum of", num1, "and", num2, "is:", max_two(num1, num2))  # Output: Maximum of 10 and 20 is: 20

#6-base on max_two,  Write a Python function called max_three that return the maximum of three numbers
def max_three(a, b, c):
    max_of_ab = max_two(a, b)
    return max_two(max_of_ab, c)
# Test the function
num1 = 10
num2 = 20
num3 = 15
print("Maximum of", num1, ",", num2, ", and", num3, "is:", max_three(num1, num2, num3))  # Output: Maximum of 10 , 20 , and 15 is: 20




