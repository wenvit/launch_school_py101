### Problem statement:

# Ben was tasked to write a simple Python function to determine 
# whether an input string is an IP address using 4 dot-separated 
# numbers, e.g., 10.4.5.11.

# Alyssa supplied Ben with a function named is_an_ip_number. 
# It determines whether a string is a numeric string between 
# 0 and 255 as required for IP numbers and asked Ben to use it. 
# Here's the code that Ben wrote:

# def is_dot_separated_ip_address(input_string):
#     dot_separated_words = input_string.split(".")
#     while len(dot_separated_words) > 0:
#         word = dot_separated_words.pop()
#         if not is_an_ip_number(word):
#             break

#     return True

# Alyssa reviewed Ben's code and said, "It's a good start, 
# but you missed a few things. You're not returning a false 
# condition, and you're not handling the case when the input 
# string has more or less than 4 components, 
# e.g., 4.5.5 or 1.2.3.4.5: both those values should be invalid."

# Help Ben fix his code.

### Solution

# need fixes:  
# handle invalid cases when input has > 4 components or < 4 components
# return False condition when len(ip) != 4 or if one of the elements 
#    is less than 0 or > 255

def is_an_ip_number(element):
    if element.isdigit():
        return int(element) in range(256)
    return False

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != 4:
        raise Exception('Valid IP addresses must have 4 components.')
    
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False
    return True

print(is_dot_separated_ip_address('204.255.104.0'))
