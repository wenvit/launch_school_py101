##### Problem statement

# Write a function that computes the sum of all 
# numbers between 1 and some other number, inclusive,
# that are multiples of 3 or 5. For instance, if the 
# supplied number is 20, the result should be 
# 98 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20).

# You may assume that the number passed in is an integer greater than 1.

############# PEDAC ###############

# inputs: integer that is upper end of sequence
# outputs: sum of all multiples of 3 or 5 up to upper end of sequence

# rules
# assume the number passed to function is integer > 1
# sum of all multiples is inclusive of upper end of sequence

# mental model
# multiples of 3 or 5 have remainders of 0 when divided by 3 or 5
# determine multiples of 3 and 5 up to given integer endpoint, inclusive
# sum values in sequence of multiples

# data structure
# function definition has integer parameter
# range to loop over
# list to store multiples

# test cases
# These examples should all print True
# print(multisum(3) == 3)
# print(multisum(5) == 8)
# print(multisum(10) == 33)
# print(multisum(1000) == 234168)

# algorithm
# 1. Define function `multisum` with a parameter `upper_end`
# 2. Use list comprehension to loop over range from 1 to `upper_end + 1`
#    and add number to list if `number % 3 == 0 or number % 5 == 0`; 
#    assign list to variable `multiples`
# 3. After loop is complete, `return sum(multiples)`

# code

# def multisum(upper_end):

#     multiples = [
#         number
#         for number in range(1, upper_end + 1)
#         if (number % 3 == 0) or (number % 5 == 0)
#     ]

#     return sum(multiples)

# another way after reviewing Launch School solution:
# defines separate function for determine multiple of a number
# does not use `sum` function

def is_multiple(number, divisor):
    return number % divisor == 0

def multisum(upper_end):
    sum_of_multiples = 0

    for number in range(1, upper_end + 1):
        if is_multiple(number, 3) or is_multiple(number, 5):
            sum_of_multiples += number
    
    return sum_of_multiples

print(multisum(20) == 98)
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)






