### Problem statement:

# How can you determine whether a given string ends with an exclamation 
# mark (!)? Write some code that prints True or False depending on whether 
# the string ends with an exclamation mark.

# Test cases
# str1 = "Come over here!"  # True
# str2 = "What's up, Doc?"  # False
# empty string # False

### Solution:

def ends_in_exclamation(text):
    return text.endswith('!')

str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False
str3 = '' # False

print(ends_in_exclamation(str1))
print(ends_in_exclamation(str2))
print(ends_in_exclamation(str3))



