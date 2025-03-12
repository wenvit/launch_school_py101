##### Problem statement

# Write a function that takes a string argument and 
# returns a new string that contains the value of the 
# original string with all consecutive duplicate characters
# collapsed into a single character.

############# PEDAC ################
# inputs: string
# outputs: string with all consecutive duplicate characters 
#          collapsed into single character

# rules
# assume valid string input
# collapse any consecutive character duplicates into a single instance
# of that character
# if no consecutive character duplicates, return string as is

# test cases
# These examples should all print True
# print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
# print(crunch('4444abcabccba') == '4abcabcba')
# print(crunch('ggggggggggggggg') == 'g')
# print(crunch('abc') == 'abc')
# print(crunch('a') == 'a')
# print(crunch('') == '')

# data structure
# strings

# algorithm
# 1. Define function `crunch` with a parameter `input_string`
# 2. Within the function body, will use local variables
#    `prev_char` to keep track of the previous character 
#    and `collapsed` which will contain a new string
#    with no consecutive duplicated characters
# 3. `while input_string` is truthy:
# 3. Initialize both `prev_char` and `collapsed` to the first
#    character in `input_string` (character at index 0)
# 4. If `input_string` is an empty string, return empty string
# 5. Use `for` to loop over characters in `input_string`
# 6. If `prev_char == char`: `continue` ==> don't do anything, just 
#    jump to next iteration of loop 
# 7. else if `prev_char != char`, add `char` to `collapsed` and
#    reassign `prev_char = char`
# 8. return `collapsed`
# 9. return `input_string` if falsy 
#    (return `input_string` as empty string as is)

# code - 1st attempt

# def crunch(input_string):
    
#     while input_string:
#         prev_char = input_string[0]
#         collapsed = input_string[0]

#         for char in input_string:
#             if prev_char == char:
#                 continue
#             else:
#                 collapsed += char
#                 prev_char = char

#         return collapsed
#     return input_string

# simplification

def crunch(input_string):
    
    while input_string:
        collapsed = input_string[0]

        for char in input_string:
            if collapsed[-1] != char:
                collapsed += char

        return collapsed
    return input_string

print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')

# Launch School solution

# def crunch(text):
#     index = 0
#     crunched_text = ''

#     while index < len(text):

#         print(f'{'*' * 10} { index}' )
#         if index == len(text) - 1 or text[index] != text[index + 1]:
#             crunched_text += text[index]
#             print(crunched_text)

#         index += 1

#     return crunched_text