##### Problem statement

# Write a program that asks for user's name, then greets the user. 
# If the user appends a ! to their name, the computer will yell 
# the greeting (print it using all uppercase).

# Examples
# What is your name? Sue
# Hello Sue.

# What is your name? Bob!
# HELLO BOB! WHY ARE WE YELLING?

############## PEDAC ###############

# inputs: name (str)
# outputs: greeting (str) - all uppercase if input name ends in '!'

# rules
# assume valid string is input as name
# if name ends with '!', return greeting in all uppercase
# else, return regular greeting

# test cases
# What is your name? Sue
# Hello Sue.

# What is your name? Bob!
# HELLO BOB! WHY ARE WE YELLING?

# data structure
# string

# algorithm
# 1. Define function `greeting` with a parameter `name` (str)
# 2. Within body of function: `if name[-1] == !` evaluates as 
#    truthy, return f-string with all caps `name` interpolated;
#    invoke `upper` method on `name` to render in all caps
# 3. else return f-string with `name` interpolated

def greeting(name):
    if name[-1] == '!':
        return (f'HELLO {name.upper()} '
                'WHY ARE WE YELLING?')
    return (f'Hello {name}.')

name = input('What is your name? ')
print(greeting(name))