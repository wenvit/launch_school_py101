######### Problem statement

# Write a function that takes one integer argument and 
# returns True when the number's absolute value is odd, 
# False otherwise.

######### PEDAC ##############

# inputs: one integer
# outputs:  True or False

# rules
# when absolute value of integer is odd --> True
# when absolute value of integer is even --> False
# assume valid integer is passed to function

# mental model
# An odd number divided by 2 has a remainder of 1
# if this condition is true, return `True`
# else return `False`

# test cases
# 1 --> True
# 2 --> False
# 12 --> False
# 0 --> False
# -5 --> True
# -8 --> False

# data structure
# integer

# algorithm
# 1. Define function with a single parameter `num`
# 2. Return the boolean result of evaluating 
#    the expression: `abs(integer) % 2 == 1` 

###  code

def is_odd(num):
    return abs(num) % 2 == 1

print(is_odd(1))  # True
print(is_odd(2))  # False
print(is_odd(12)) # False
print(is_odd(0))  # False
print(is_odd(-5)) # True
print(is_odd(-8)) # False


