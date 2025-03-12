##### Problem statement

# In the previous exercise, we assumed that the Gregorian calendar 
# has been in continuous use since the year 1. However, the Gregorian 
# calendar wasn't adopted until much later; prior to that, much of 
# the world used the Julian calendar, which observed leap year every 4 years.

# in 1752, England, Ireland, and the British colonies all switched to the 
# Gregorian calendar. Update the function from the previous exercise 
# so it uses the Julian calendar prior to 1752, and the Gregorian calendar 
# starting in 1752.

############ PEDAC #################

# inputs: any year > 0
# outputs: `True` if leap year, `False` if not

# rules
# for years < 1752, apply Julian calendar rules -
# years divisible by 4 are leap years
# for years >= 1752, apply Gregorian calendar rules 

# test cases 
# These examples should all print True
# print(is_leap_year(1) == False)
# print(is_leap_year(2) == False)
# print(is_leap_year(3) == False)
# print(is_leap_year(4) == True)
# print(is_leap_year(1000) == True)
# print(is_leap_year(1100) == True)
# print(is_leap_year(1200) == True)
# print(is_leap_year(1300) == True)
# print(is_leap_year(1751) == False)
# print(is_leap_year(1752) == True)
# print(is_leap_year(1753) == False)
# print(is_leap_year(1800) == False)
# print(is_leap_year(1900) == False)
# print(is_leap_year(2000) == True)
# print(is_leap_year(2023) == False)
# print(is_leap_year(2024) == True)
# print(is_leap_year(2025) == False)

# algorithm
# 1. Define function `is_leap_year` with a parameter `year`
# 2. Write a series of if/elif/else statements to check for a leap year
#    if year <= 0 --> return `Enter valid year > 0`
#    elif year < 1752 --> return year % 4 == 0
#    elif year % 400 == 0 --> `True`
#    elif year % 100 == 0 --> `False`
#    else return year % 4 == 0 --> `True` (`False` for non-leap years)

# code

def is_leap_year(year):
    
    if year <= 0:
        return 'Year must be greater than 0.'
    elif year < 1752:
        return year % 4 == 0
    elif year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return year % 4 == 0

print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == True)
print(is_leap_year(1100) == True)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == True)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)
print(is_leap_year(-2000))