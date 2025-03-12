####### Problem statement

# Write a function that takes a short line of text 
# and prints it within a box.
# You may assume the output will always fit in your terminal window.

############## PEDAC #############
# inputs: string
# outputs: string enclosed in box 

# rules
# corners of box are `+` signs
# top and bottom of box composed of `-` characters
#   for length of text string plus an additional `-`
#   before start of string and after end of string
# sides of box composed of `|` x 3 tall

# test cases
# print_in_box('To boldly go where no one has gone before.')
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

# print_in_box('')
# +--+
# |  |
# |  |
# |  |
# +--+

# data structure
# strings

# algorithm
# 1. Define function `print_in_box` with parameter `input_string`
# 2. Determine length of string and assign to variable `string_length`
# 3. Create string for top/bottom of box:  
#    '+' + '-' * (string_length + 2) + '+'
#    and assign to variable `top_bottom`
# 4. Create string for sides:
#    '|' + ' ' * (string_length + 2) + `|`
#    and assign to variable `sides`
# 5. Invoke `print` function with argument `top_bottom`
# 6. Invoke `print` with argument `sides`
# 7. Invoke `print` with f-string interpolating `input_string`
#    padded on each side with '| ' and ' |'
# 8. Invoke `print` with argument `sides`
# 9. Invoke `print` with argument `top_bottom`

# code

# def print_in_box(input_string):
#     string_length = len(input_string)
#     top_bottom = '+' + '-' * (string_length + 2) + '+'
#     sides = '|' + ' ' * (string_length + 2) + '|'

#     print(top_bottom)
#     print(sides)
#     print(f'| {input_string} |')
#     print(sides)
#     print(top_bottom)

# print_in_box('To boldly go where no one has gone before.')
# print_in_box('')

# Further exploration

#Modify this function so that it truncates the message 
# if it doesn't fit inside a maximum width provided 
# as a second argument (the width is the width of the box 
# itself). You may assume no maximum if the second argument is omitted.

#For a challenging but fun exercise, try word wrapping 
# messages that are too long to fit, so that they appear 
# on multiple lines but are still contained within the box. 
# This isn't an easy problem, but it's doable with basic Python.

# def print_in_box(input_string, max_width = 1):
#     string_length = len(input_string)
#     top_bottom = '+' + '-' * (max_width + 2) + '+'
#     sides = '|' + ' ' * (max_width + 2) + '|'

#     print(top_bottom)
#     print(sides)

#     if string_length < max_width:
#         print(f'| {input_string.center(max_width)} |')
#     else:
#         print(f'| {input_string[:max_width].center(max_width)} |')

#     print(sides)
#     print(top_bottom)

# print_in_box('To boldly go where no one has gone before.', 25)
# print_in_box('To boldly go where no one has gone before.', 5)
# print_in_box('To boldly go where no one has gone before.', 100)
# print_in_box('')

# version with word wrap

import math

def print_in_box(input_string, max_width = 1):
    string_length = len(input_string)
    top_bottom = '+' + '-' * (max_width + 2) + '+'
    sides = '|' + ' ' * (max_width + 2) + '|'

    print(top_bottom)
    print(sides)

    if string_length < max_width:
        print(f'| {input_string.center(max_width)} |')
    else:
        lines = math.ceil(string_length / max_width)
        start = 0
        stop = start + max_width
        for line in range(lines):
            print(f'| {input_string[start:stop].center(max_width)} |')
            start += max_width
            stop += max_width
    
    print(sides)
    print(top_bottom)

print_in_box('To boldly go where no one has gone before.', 25)
print_in_box('To boldly go where no one has gone before.', 5)
print_in_box('To boldly go where no one has gone before.', 70)
print_in_box('')