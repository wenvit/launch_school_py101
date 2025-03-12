####### Problem statement

# A double number is an even-length number whose left-side digits 
# are exactly the same as its right-side digits. 
# For example, 44, 3333, 103103, and 7676 are all double numbers, 
# whereas 444, 334433, and 107 are not.

# Write a function that returns the number provided as an argument 
# multiplied by two, unless the argument is a double number.
# If the argument is a double number, return the double number as-is.

########### PEDAC ##############

# inputs: integer
# outputs: same integer input if double number, 
#          else integer * 2

# rules
# assume valid positive integer is input
# double number has even number of digits and 
#   left-side digits == right-side digits
# if integer is double number, return as is
# if integer is not double number, return integer * 2

# mental model
# Divide digits into halves and check whether the two halves are equal. 
# If so, return number as is.
# If not, return number multiplied by 2.

# test cases
# print(twice(37) == 74)                  # True
# print(twice(44) == 44)                  # True
# print(twice(334433) == 668866)          # True
# print(twice(444) == 888)                # True
# print(twice(107) == 214)                # True
# print(twice(103103) == 103103)          # True
# print(twice(3333) == 3333)              # True
# print(twice(7676) == 7676)              # True

# algorithm
# 1. Define `twice` function with parameter `number` (positive int).
# 2. Use `str` constructor to convert `number` to a string, assign
#    to variable `number_str`
# 3. Determine indices for slicing into
#    two substring halves for comparison: idx = len(number_str) // 2
# 4. If number_str[:idx] == number_str[idx:] return number
# 5. else return number * 2

def twice(number):
    number_str = str(number)
    idx = len(number_str) // 2

    if (number_str[:idx] == number_str[idx:]):
        return number
    return number * 2


print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True