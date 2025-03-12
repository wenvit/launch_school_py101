##### Problem statement

# Write a function that takes one argument, a positive integer, 
# and returns a string of alternating '1's and '0's, always 
# starting with a '1'. The length of the string should match 
# the given integer.

########### PEDAC ##############

# inputs: positive integer
# outputs: string of '1' and '0' with length = input integer

# rules
# assume valid input integer
# output string always starts with '1'
# output string alternates '1' and '0'

# mental model
# If input integer = 1, output = '1'
# If input integer is even, output = '10' * integer // 2
# If input integer is odd, output = '10' * integer // 2 + '1'

# data structure
# strings

# test cases
# print(stringy(6) == "101010")           # True
# print(stringy(9) == "101010101")        # True
# print(stringy(4) == "1010")             # True
# print(stringy(7) == "1010101")          # True

# algorithm
# 1. Define function `stringy` with input parameter `length`
# 2. if length == 1: return '1'
# 3. if length % 2 == 0: return '10' * length // 2  
# 4. if length % 2 == 1: return '10' * length // 2 + '1'

# code

# def stringy(length):
#     if length == 1:
#         return '1'
#     elif length % 2 == 0:
#         return '10' * (length // 2)
#     return '10' * (length // 2) + '1'

# another way after reviewing Launch School solution

# def stringy(length):
#     result = ''

#     for idx in range(length):
#         if idx % 2 == 0:
#             result += '1'
#         else:
#             result += '0'
    
#     return result

# reduce to ternary expression

def stringy(length):
    result = ''
    digit = ''

    for idx in range(length):
        digit = '1' if idx % 2 == 0 else '0'
        result += digit
    
    return result


print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True