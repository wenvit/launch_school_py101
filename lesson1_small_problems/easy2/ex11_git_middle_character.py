##### Problem statement

# Write a function that takes a non-empty string argument and 
# returns the middle character(s) of the string. If the string 
# has an odd length, you should return exactly one character. 
# If the string has an even length, you should return exactly two 
# characters.

############# PEDAC #################

# inputs: string
# outputs: middle character if string length odd,
#          middle 2 characters if string length even

# rules
# input must not be an empty string 
# if string length is even, returned value is a substring
# consisting of 2 middle characters (not 2 individual characters)

# mental model
# If string is truthy (not empty): determine length.
# If length of string is even, return substring starting at
# index of length / 2 -1 with stop of length / 2 + 1 (not inclusive)
# If length of string is odd, return character at the 
# index of length // 2. 


# test cases
# print(center_of('I Love Python!!!') == "Py")    # True
# print(center_of('Launch School') == " ")        # True
# print(center_of('Launchschool') == "hs")        # True
# print(center_of('Launch') == "un")              # True
# print(center_of('Launch School is #1') == "h")  # True
# print(center_of('x') == "x")                    # True
# print(center_of('')) # Please enter a valid string.

# data structure
# strings

# algorithm
# 1. Define function `center_of` with a parameter `text`
# 2. `if text == ''`, return error message
# 3. `elif len(text) % 2 == 0`: return `text` slice with 
#     start index of `len(text) // 2 - 1` and [need int division for index]
#     stop index of `len(text) // 2 + 1`
# 4. else return character at index of `len(text) // 2`

# code

def center_of(text):

    if text == '':
        return 'Please enter a valid string.'
    elif len(text) % 2 == 0:
        start = len(text) // 2 - 1
        stop = len(text) // 2 + 1
        return text[start:stop]
    else:
        return text[len(text) // 2]
        
print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True
print(center_of(''))  # Please enter a valid string.
    