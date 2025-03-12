##### Problem statement

# Write a function that determines and returns the UTF-16 string value
# of a string passed in as an argument. The UTF-16 string value is the 
# sum of the UTF-16 values of every character in the string. 
# (You may use ord to determine the UTF-16 value of a character.)

# # These examples should all print True
# print(utf16_value('Four score') == 984)
# print(utf16_value('Launch School') == 1251)
# print(utf16_value('a') == 97)
# print(utf16_value('') == 0)

# The next three lines demonstrate that the code
# works with non-ASCII characters from the UTF-16
# character set.
# OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
# print(utf16_value(OMEGA) == 937)
# print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)

########### PEDAC ###############

# inputs: string
# output: sum of all UTF-16 values of string characters

# rules
# Use `ord` function to determine UTF-16 value of individual characters
# Assume valid string is passed to function.

# data structure
# function defined with string parameter

# test cases
# # These examples should all print True
# print(utf16_value('Four score') == 984)
# print(utf16_value('Launch School') == 1251)
# print(utf16_value('a') == 97)
# print(utf16_value('') == 0)

# The next three lines demonstrate that the code
# works with non-ASCII characters from the UTF-16
# character set.
# OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
# print(utf16_value(OMEGA) == 937)
# print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)

# algorithm
# 1. Define function `utf16_value` with a parameter `text`
# 2. Initialize `result` to 0
# 3. Use `for` loop to iterate over characters in `text`,
#    and invoke `ord` function passing each character as argument,
# 4. Using augmented assignment, add value returned by `ord` function 
#    call to `result`
# 5. Return `result`

# code

def utf16_value(text):
    result = 0

    for char in text:
        result += ord(char) 
    
    return result

print(utf16_value('Four score') == 984)
print(utf16_value('Launch School') == 1251)
print(utf16_value('a') == 97)
print(utf16_value('') == 0)

# The next three lines demonstrate that the code
# works with non-ASCII characters from the UTF-16
# character set.
OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
print(utf16_value(OMEGA) == 937)
print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)