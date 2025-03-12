##### Problem statement

# Write a program that asks the user to enter an integer greater than 0,
# then asks whether the user wants to determine the sum or the product 
# of all numbers between 1 and the entered integer, inclusive.

# Example 1
# Please enter an integer greater than 0: 5
# Enter "s" to compute the sum, or "p" to compute the product. s

# The sum of the integers between 1 and 5 is 15.

# Example 2
# Please enter an integer greater than 0: 6
# Enter "s" to compute the sum, or "p" to compute the product.  p

# The product of the integers between 1 and 6 is 720.

########## PEDAC ##################

# inputs: integer > 0, 's' or 'p' indicating sum or product
# outputs: sum or product of sequence of numbers from 1 to integer

# rules
# Assume valid inputs (integer > 0).
# Sequence of numbers to add or multiply starts with 1 and ends with 
# integer entered by user, inclusive

# test cases
# user enters 's' and 5 --> 15
# user enters 'p' and 6 --> 720

# data structure
# range 

# algorithm
# 1. Prompt user for an integer; convert input string to integer data type; 
#    assign to variable `stop`
# 2. Prompt user to specify 's' for sum and 'p' for product; assign
#    to variable `operation`
# 3. `if operation == s` evaluates as truthy: 
#     initialize `result` to 0; `description` to 'sum'
#     use `for` loop to iterate over range with start of 1, stop of `stop + 1`
#     add next integer in sequence to `result` using augmented assignment
# 3. `else`: initialize `result` to 1; `description` to 'product'
#     use `for` loop to iterate over range with start of 1, stop of `stop + 1`
#     multiply `result` by next integer in sequence using augmented assignment
# 4. Invoke `print` function with f-string argument that interpolates
#    value of `result` variable

# code

stop = int(input('Please enter an integer greater than 0: '))
operation = input('Enter "s" to compute the sum, or "p" to compute the product: ')


if operation == 's':
    result = 0
    description = 'sum'
    
    for number in range(1, stop + 1):
        result += number

else: 
    result = 1
    description = 'product'

    for number in range(1, stop + 1):
        result *= number

print(f'The {description} of integers between 1 and {number} is {result}.')