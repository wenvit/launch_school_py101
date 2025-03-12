###### Problem statement

# Build a program that randomly generates and prints Teddy's age.
# To get the age, you should generate a random number between 
# 20 and 100, inclusive.

########## PEDAC ###############

# input: NA
# output: random integer between 20 and 100, inclusive

# test case
# Teddy is 69 years old!

# algorithm
# 1. Import `random` module
# 2. Call `randrange` with start 20, end 101 (not inclusive)
#    assign returned value to `age` variable
# 3. Invoke `print` function with f-string argument that 
#    interpolates `age`

# code

# import random

# age = random.randrange(20, 101)

#print(f'Teddy is {age} years old!')

#Further Exploration

# Modify this program to ask for a name, then 
# print the age for that person. For an extra 
# challenge, use "Teddy" as the name if no name is entered.

import random

def get_name():
    name = input('Please enter your name: ')
    if name:
        return name
    return 'Teddy'

name = get_name()
age = random.randrange(20, 101)

print(f'{name} is {age} years old!')

