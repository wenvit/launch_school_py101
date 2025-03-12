##### Problem statement

# Write a function that takes a positive integer, n, 
# as an argument and prints a right triangle whose 
# sides each have n stars. The hypotenuse of the triangle 
# (the diagonal side in the images below) should have one 
# end at the lower-left of the triangle, and the other end
# at the upper-right.

########### PEDAC ############
# inputs: integer `n`
# output: right triangle depicted with `n` asterisks

# rules
# assume valid positive integer passed to function
# bottom and right side of triangle composed of `n` asterisks
# hypotenuse extends from bottom left to upper right

# mental model
# Function prints rows starting from top to bottom by looping 
# over a range with start of 1 and stop  of `n + 1`. 
# Starting at the top, print out `n - 1` spaces followed by 1 asterisk.
# Next row, print `n - 2` spaces, followed by 2 asterisks.
# Continue this pattern until the bottom row is made up of 
# `0` spaces and `n` asterisks. 

# test cases

# triangle(5)

#     *
#    **
#   ***
#  ****
# *****

# triangle(9)

#         *
#        **
#       ***
#      ****
#     *****
#    ******
#   *******
#  ********
# *********

# data structure
# integer, '*'
# range to loop over

# algorithm
# 1. Define function `triangle` with paramter `n` (int)
# 2. `for` loop with variable `count` to iterate over 
#    range with start of 1 and stop of `n + 1`
# 3. Within loop, invoke `print` with f-string to print (n - count) * ' ' 
#    concatenated with `count * '*'

# code

# def triangle(n):
#     for count in range(1, n + 1):
#         print(f'{(n - count) * ' ' + count * '*'}')

# triangle(5)
# triangle(9)

# Launch School solution uses variables for spaces & starts
# to make code more readable

def triangle(n):
    for count in range(1, n + 1):
        spaces = n - count
        stars = count
        print(f'{spaces * ' ' + stars * '*'}')

triangle(5)
triangle(9)