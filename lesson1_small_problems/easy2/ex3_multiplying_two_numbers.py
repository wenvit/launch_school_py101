######## Problem statement

# Create a function that takes two arguments, 
# multiplies them together, and returns the result.

# Example
# print(multiply(5, 3) == 15)  # True

######### PEDAC ###########

# inputs: 2 numbers
# output: product of 2 numbers

# rules
# assume valid numbers are passed to function
# return product of 2 numbers

# test cases
# 5, 3 --> 15
# -5, 3 --> -15
# 0, 8 --> 0

# algorithm
# 1. Define function `multiply` with two parameters `num1` and `num2`
# 2. Return `num1 * num2`

# code 

def multiply(num1, num2):
    return num1 * num2

print(multiply(3, 5))
print(multiply(-5, 3))
print(multiply(0, 8))
print(multiply(0.5, 20))