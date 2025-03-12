##### Problem statement

# Write a function that takes a number as an argument. 
# If the argument is a positive number, return the negative 
# of that number. If the argument is a negative number, 
# return it as-is.

############ PEDAC #################

# input: number
# output: negative of that number 

# rules
# if input number is positive, return negative of the number
# if input number is negative, return the number as is

# test cases
# print(negative(5) == -5)      # True
# print(negative(-3) == -3)     # True
# print(negative(0) == 0)       # True

# data structure
# could be integer or float

# algorithm
# 1. Define function with parameter `number`
# 2. Within body of function, `if number < 0` return number
#    `else return -number`

# code

def negative(number):
    if number < 0:
        return number
    return -number

print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True

print(negative(-7))