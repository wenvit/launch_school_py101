##### Problem statement

# Write a function that takes two strings as arguments, 
# determines the length of the two strings, and then 
# returns the result of concatenating the shorter string, 
# the longer string, and the shorter string once again. 
# You may assume that the strings are of different lengths.

# Examples
# These examples should all print True
# print(short_long_short('abc', 'defgh') == "abcdefghabc")
# print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
# print(short_long_short('', 'xyz') == "xyz")

######## PEDAC #################

# inputs: 2 strings of different lengths
# outputs: concatented string consisting of 
#          shorter + longer + shorter string

# rules
# Assume strings are different lengths
# Assume arguments passed to function are of proper type (strings)
# Concatenate strings as follows: shorter + longer + shorter

# test cases
# examples given

# algorithm
# 1. Define function `short_long_short` with two parameters:
#    `string1` and `string2`
# 2. Within function, use `len` function to determine length of 
#    each string and assign the length values to variables
#    `len_string1` and `len_string2`
# 3. Write if/else statement to concatenate strings in proper order
#    `if len_string1 > len_string2: return string2 + string1 + string2`
#    `else return string1 + string2 + string1`

# code

def short_long_short(string1, string2):
    len_string1 = len(string1)
    len_string2 = len(string2)

    if len_string1 > len_string2:
        return string2 + string1 + string2
    else:
        return string1 + string2 + string1

print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")