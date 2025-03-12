######## Problem statement

# The or operator returns a truthy value if either or 
# both of its operands are truthy, a falsy value if 
# both operands are falsy. The and operator returns 
# a truthy value if both of its operands are truthy, 
# and a falsy value if either operand is falsy. 
# This works great until you need only one of t
# wo conditions to be truthy, the so-called exclusive or, 
# also known as xor (pronounced "ECKS-or").

# In this exercise, you will write an xor function 
# that takes two arguments, and returns True if 
# exactly one of its arguments is truthy, False otherwise.

############ PEDAC ###################

# inputs: 2 operands that can be evaluated as truthy or falsy (any data type)
# output: True or False 

# rules
# function returns True if one of the operands is truthy
# function returns False if both operands are truthy or both are falsy
# no short circuiting after evaluating the first operand

# test cases
# print(xor(5, 0) == True)
# print(xor(False, True) == True)
# print(xor(1, 1) == False)
# print(xor(True, True) == False)

# mental model
# xor returns `True` if 
# operand 1 True, operand 2 False
# operand 1 False, operand 2 True
# xor returns `False` if
# operand 1 True, operand 2 True
# operand 1 False, operand 2 False

# data structure
# boolean `True` and `False`

# algorithm
# 1. Define function `xor` with two parameters `operand1` and `operand2`
# 2. Invoke bool function on `operand1` and `operand2` and enclose in `[]`
#    operator to create list of booleans, assign to 
#    variable `bool_list`
# 3. Invoke `count` method with `True` as an argument on 
#    `bool_list`, assign to `result`
# 4. Return `result == 1`

# def xor(operand1, operand2):
#     bool_list = [bool(operand1), bool(operand2)]
#     result = bool_list.count(True)
#     return result == 1

# print(xor(5, 0) == True)
# print(xor(False, True) == True)
# print(xor(1, 1) == False)
# print(xor(True, True) == False)

## Another approach based on Launch School solution

def xor(operand1, operand2):
    if (operand1 and not operand2) or (operand2 and not operand1):
        return True
    return False


print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)
print(xor(None, None) == False)
print(xor('', ' ') == True)