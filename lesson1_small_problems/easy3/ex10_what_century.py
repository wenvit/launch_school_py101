##### Problem statement

# Write a function that takes a year as input 
# and returns the century. The return value 
# should be a string that begins with the century 
# number, and ends with 'st', 'nd', 'rd', or 'th' 
# as appropriate for that number.

# New centuries begin in years that end with 01. 
# So, the years 1901 - 2000 comprise the 20th century.

############## PEDAC ################

# inputs: year
# outputs: century (string consisting of number + 
#          'st', 'nd', 'rd', or 'th')

# rules
# assume years AD
# centuries begin in years that end with 01
# century names are associated with the max year
#   in the 100-year bin (years ending in '00')

# mental model
# Determine year of century name. Years that
# end in '00' are associated with the century name.
# Round up to the nearest 100. Convert century year to a string and
# remove the '00' from the end of the string. Concatenate resulting
# substring with: 'st' if '1' or ends in '1'
#                 'nd' if '2' or ends in '2'
#                 'rd' if '3' or ends in '3'
#                 'th' for everything else

# test cases
# print(century(2000) == "20th")          # True
# print(century(2001) == "21st")          # True
# print(century(1965) == "20th")          # True
# print(century(256) == "3rd")            # True
# print(century(5) == "1st")              # True
# print(century(10103) == "102nd")        # True
# print(century(1052) == "11th")          # True
# print(century(1127) == "12th")          # True
# print(century(11201) == "113th")        # True

# data structure
# integers for input year and rounding up to nearest 100
# string output

# algorithm
### Note: found function that rounds up to nearest 100 on substack
# 1. Import math module
# 2. Define function `round_up` that has a parameter `number` (int)
# 3. Return value resulting from: dividing `number` by 100, then passing
#    this value to `math.ceil` function,
#    (which returns an integer), then multiplying by 100. 
# 4. Define `century` function with parameter `year` (int)
# 5. Invoke `round_up` passing `year` as argument, convert return
#    value to string by passing as an argument to `str` constructor function, 
#    assign return string value to `century_yr`
# 6. Using slicing notation, create a substring of century_yr by 
#    taking a slice from the beginning of string up to but not including
#    the last 2 characters, assign result to `century_desc`
# 7. Using slicing notation, create a substring of `century_desc` by 
#    taking slice starting with 2nd character from end through the last 
#    character if len(century_desc) >= 2, else century_desc
# 8. Use if/elif statements to match ending digit or digits with 
#    'st', 'nd', 'rd', 'th' as appropriate


# import math

# def round_up(number):
#     return math.ceil(number / 100) * 100

# def century(year):
#     century_yr = str(round_up(year))
#     century_desc = century_yr[:-2]
#     last2 = century_desc[-2:] if len(century_desc) >= 2 else century_desc
   
#     if last2 in ('01', '1', '21', '31', '41', '51', '61', '71', '81', '91'):
#             return century_desc + 'st'
#     elif last2 in ('02', '2', '22', '32', '42', '52', '62', '72', '82', '92'):
#             return century_desc + 'nd'
#     elif last2 in ('03', '3', '23', '33', '43', '53', '63', '73', '83', '93'):
#             return century_desc + 'rd'
#     return century_desc + 'th'

# print(century(2000) == "20th")          # True
# print(century(2001) == "21st")          # True
# print(century(1965) == "20th")          # True
# print(century(256) == "3rd")            # True
# print(century(5) == "1st")              # True
# print(century(10103) == "102nd")        # True
# print(century(1052) == "11th")          # True
# print(century(1127) == "12th")          # True
# print(century(11201) == "113th")        # True  

# Simplified after reviewing Launch School and other solutions
# algorithm mods
# Don't need to multiply century_yr by 100, then slice the last two '00' off
#    though it helped conceptualize the century year
# Also save steps by using % 10 and % 100 operations instead of convert int
#    to strings, then slicing

import math

def round_up(number):
    return math.ceil(number / 100)

def century(year):
    century_yr = round_up(year)
    last2 = century_yr % 100
    last1 = century_yr % 10

    match last2:
        case 11 | 12 | 13:
            return f'{century_yr}th'
    match last1:
        case 1:
            return f'{century_yr}st'
        case 2:
            return f'{century_yr}nd'
        case 3:
            return f'{century_yr}rd'
        case _:
            return f'{century_yr}th'

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True  

