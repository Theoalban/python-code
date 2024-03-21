import math # This gives  access to the math module which contains functions for mathematical operations.

math.pi # this is the value of pi.
print(math.pi)

math.e # this is the value of e (the base of natural logarithms).used in exponential functions(e**x).
print(math.e)

math.exp(10) # returns e raised to the power of 10
print(math.exp(10))

math.cos(0) # Returns the cosine of 0 degrees, which is 1 
print(math.cos(0))

# The cos()  function can take any number as an argument and return its cosine.
angle_in_degrees =  30  
angle_in_radians = math.pi * angle_in_degrees / 180 # Converts from degrees to radians.

print("The cosine of", angle_in_degrees,"degrees is:")
print(math.cos(angle_in_radians), "or", math.cos(math.pi/6))  # Because there are six degrees in a complete  circle and one degree equals math.pi/6.


math.sin(0) # Returns the sine of 0 degrees, which is 0 
print(math.sin(0))

# The sin() function takes an angle  as its argument and returns the sine of that angle.
# It uses radians for input so you need to convert from degrees if your angles are given in degrees.
angle_in_degrees =  30      
angle_in_radians = math.pi * angle_in_degrees / 180  # Convert from degrees to radians.
sine_of_angle = math.sin(angle_in_radians)                  # Calculate the sine.
print("The sine of", angle_in_degrees,"degrees is", sine_of_angle)

math.sqrt # This function returns the square root of a number.
positive_number = 16  # A positive number.    
result1 = math.sqrt(positive_number)             # Get the square root.
print("The square root of", positive_number , "is", result1)

try:
    negative_number= -4      # A negative number.
    result2 = math.sqrt(negative_number)        # Try to get the square root
    print("The square root of", negative_number , "is", result2)  # This will raise a  ValueError because sqrt() does not accept neg
except  ValueError:          # This will catch errors 
    print("Error! Negative numbers cannot be taken to the power of zero.")

math.pow(5,2) # This returns 5 squared, or 5*5 which equals  25.
print(math.pow(5,2))







