##### Problem statement

# Write a function that takes two arguments, a string 
# and a positive integer, then prints the string as
# many times as the integer indicates.

############# PEDAC ###############
# inputs: string, positive integer
# outputs: string repeated integer number of times

# rules
# assume valid inputs
# print each iteration of string on a separate line

# data structure
# string, integer

# test case

# repeat('Hello', 3)
# Hello
# Hello
# Hello

# algorithm
# 1. Define function `repeat` with parameters `message` and `multiplier`
# 2. Use `for` loop with `range` constructor with 0 start and 
#    stop of `multiplier`
# 3. Within each iteration invoke `print`
#    function with f-string argument that interpolates `message`

# code

def repeat(message, multiplier):
    for _ in range(multiplier):
        print(f'{message}')

repeat('Hello', 3)
repeat("Let's try another test!", 10)

