##### Problem statement

# Print all even numbers from 1 to 99, inclusive, with 
# each number on a separate line.

# Bonus Question: Can you solve the problem by iterating 
# over just the even numbers?

######### PEDAC ##############

# inputs: NA
# outputs: even numbers from 1-99, inclusive

# rules
# print all even numbers from 1-99, inclusive
# print each even number on a separate line

# mental model
# Determine which numbers from 1 to 99, inclusive, are even.
# Even numbers divided by 2 yield remainder of 0.
# Print the even numbers.

# test cases
# ensure that 1 and 99 are not included in the list of printed numbers

# data structure
# integers
# bonus question - range

# algorithm 1
# 1. Initialize a variable called `number` to 1.
# 2. Set up `while` loop to iterate as long as 
#    expression `number is <= 99` evaluates as truthy. 
# 3. Within the `while` block, evaluate expression `number % 2 == 0`.
# 4. If expression evaluates as truthy, invoke `print`
#    with `number` as argument.
# 5. Increment `number` by 1 using augmented assignment.

# algorithm 2 - bonus question
# 1. Set up `for` loop to iterate over a range using 
#   `range` constructor with a start of 2, stop of 100, step of 2.
# 2. Invoke `print` with each number iterated over in sequence. 

# code

# 1) while loop approach

# number = 1

# while number <= 99:
#     if number % 2 == 0:
#         print(number)
#     number += 1

# 2) range approach

for number in range(2, 100, 2):
        print(number)