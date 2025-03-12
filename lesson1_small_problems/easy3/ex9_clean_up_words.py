##### Problem statement

# Given a string that consists of some words and 
# an assortment of non-alphabetic characters, 
# write a function that returns that string with 
# all of the non-alphabetic characters replaced 
# by spaces. If one or more non-alphabetic 
# characters occur in a row, you should only 
# have one space in the result (i.e., the 
# result string should never have consecutive spaces).

############ PEDAC ##########

# inputs: string
# outputs: string with non-alphabetic characters replaced with spaces

# rules
# assume valid string input
# resulting string should never have consecutive spaces

# mental model
# Iterate over input string, create new string by adding each alpha
# character as is, changing non-alpha characters to space and only 
# add a space if previous character is not a space 

# test case
# print(clean_up("---what's my +*& line?") == " what s my line ")
# True
# also want to test a single character '-' or 'a'

# data structure
# string

# algorithm
# 1. Define `clean_up` function with a parameter `text` (str)
# 2. If `len(text) == 1`: return `text` if text.isalpha() else ' '
# 3. Initialize string `text_cleaned` to first character of `text` if 
#    character isalpha else ' '
# 4. Initialize `idx` to 1
# 5. `while idx < len(text)`:
# 5. Assign `clean_char` to `text[idx]` if text[idx].isalpha()` else ' '
# 6. if clean_char is a space and last character of text_cleaned is a space,
#    reassign clean_char to an empty string
# 7. Reassign `text_cleaned` variable to value of `text_cleaned` concatenated 
#    with `clean_char` using augmented assignment
# 8. Increment `idx` by 1

# code

# first attempt

# def clean_up(text):

#     if len(text) == 1:
#         return text if text.isalpha() else ' '
    
#     text_cleaned = text[0] if text[0].isalpha() else ' '
#     idx = 1

#     while idx < len(text):
#         clean_char = text[idx] if text[idx].isalpha() else ' '

#         if clean_char.isspace() and text_cleaned[-1].isspace():
#             clean_char = ''

#         text_cleaned += clean_char
#         idx += 1
    
#     return text_cleaned


# print(clean_up("---what's my +*& line?") == " what s my line ")
# print(clean_up('a') == 'a')
# print(clean_up('-') == ' ')

# Improvement after review Launch School solution

# 1. Define `clean_up` function with parameter `text` (str)
# 2. Initialize `text_cleaned`` to empty string
# 3. Use for loop to iterate over `idx` and `char` variables 
#    assigned to index and characters returned by calling
#    `enumerate` function with `text` argument
# 4. Withn `for` loop, if `char.isalpha()` is truthy:
#    reassign `text_cleaned` to previous value concatenated with
#    `char`
# 5. elif idx == 0 or last character in `text_cleaned` is
#    not equal to space, concatenate `text_cleaned` and space
# 6. return text_cleaned
# 

def clean_up(text):
    
    text_cleaned = ''

    for idx, char in enumerate(text):

        if char.isalpha():
            text_cleaned += char 
        elif idx == 0 or text_cleaned[-1] != ' ':
            text_cleaned += ' '
    
    return text_cleaned


print(clean_up("---what's my +*& line?") == " what s my line ")
print(clean_up('a') == 'a')
print(clean_up('-') == ' ')