##### Problem statement

# Print all odd numbers from 1 to 99, inclusive, 
# with each number on a separate line.

# Bonus Question: Can you solve the problem by 
# iterating over just the odd numbers?

######### PEDAC ##############

# inputs: NA
# outputs: odd numbers from 1-99

# rules
# print all odd numbers from 1-99, inclusive
# print each odd number on a separate line

# mental model
# Odd numbers divided by 2 yield remainder of 1.
# Determine which numbers from 1 to 99, inclusive, are odd.
# Print the odd numbers.

# test cases
# ensure that 99 is included in the printed list of numbers  

# data structure
# integers
# bonus question - range

# algorithm 1
# 1. Initialize a variable called `number` to 1.
# 2. Set up a `while` loop to iterate as long as 
#    expression `number is <= 99` evaluates as truthy. 
# 3. Within the `while` block, if `number % 2 == 1`
#    evaluates as truthy, print number.
# 4. Increment `number` by 1 using augmented assignment.

# algorithm 2 - bonus question
# 1. Set up a `for` loop to iterate over a range using 
# `range` constructor with a start of 1, stop of 100, step of 2.
# 2. Print each integer in sequence. 

# code

# 1) while loop approach

# number = 1

# while number <= 99:
#     if number % 2 == 1:
#         print(number)
#     number += 1

# 2) range approach

for number in range(1, 100, 2):
    print(number)


## Further Exploration
# Consider adding a way for the user to specify the starting 
# and ending values of the odd numbers printed.

# test cases
# Start value should be printed if odd, but should not be printed if even.
# Stop value should be printed if odd, but should not be printed if even.
# Make sure negative values are handled appropriately.

# algorithm
# 1. Define a function with parameters of `start` and `stop`.
# 2. Within function body, use a `for` loop to iterate over a range.
# 3. `range` constructor function takes parameters of `start` and `stop + 1`.
# 4. Within `for` loop, if expression `number % 2 == 1` evaluates
#    as truthy, pass `number` as argument to `print`


# def odd_sequence(start, stop):
#     for number in range(start, stop + 1):
#         if number % 2 == 1:
#             print(number)
        
#odd_sequence(1, 99)  # same output as above solutions
#odd_sequence(-5, 10)  # -5, -3, -1, 1, 3, 5, 7, 9
#odd_sequence(-5, 11)  # -5, -3, -1, 1, 3, 5, 7, 9, 11
#odd_sequence(2, 16)   # 3, 5, 7, 9, 11, 13, 15
#odd_sequence(2, 15)   # 3, 5, 7, 9, 11, 13, 15

