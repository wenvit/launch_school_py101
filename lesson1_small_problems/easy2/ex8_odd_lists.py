##### Problem statement

# Write a function that returns a list that contains every other element
# of a list that is passed in as an argument. The values in the returned 
# list should be those values that are in the 1st, 3rd, 5th, and so on 
# elements of the argument list.

# Bonus question: Try to solve the problem using list slicing.

############# PEDAC ###############

# input: list
# output: list containing only every other element

# rules
# assume valid list passed in as argument
# function returns list containing every other element, which are
#    elements at even numbered indices of list

# test cases
# print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
# print(oddities([1, 2, 3, 4]) == [1, 3])        # True
# print(oddities(["abc", "def"]) == ['abc'])     # True
# print(oddities([123]) == [123])                # True
# print(oddities([]) == [])                      # True

# data structure
# list for function input & output
# range to iterate over list indices

# algorithm
# 1. Define function `oddities` with a parameter `input_list` (list)
# 2. Use list comprehension to create a new list by iterating over
#    indices `idx` in `input_list` using `range(len(input_list))` 
#    and selecting even numbered indices using if conditional
#    based on `idx % 2 == 0`

# code

# def oddities(input_list):
#     odd_list = [
#         input_list[idx] 
#         for idx in range(len(input_list))
#         if idx % 2 == 0
#     ]
#     return odd_list


# bonus question: using slicing

# def oddities(input_list):
#     return input_list[::2]


# print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
# print(oddities([1, 2, 3, 4]) == [1, 3])        # True
# print(oddities(["abc", "def"]) == ['abc'])     # True
# print(oddities([123]) == [123])                # True
# print(oddities([]) == [])                      # True

# further exploration 
# Write a companion function that returns the 2nd, 4th, 6th, 
# and so on elements of a list. These are the odd-numbered indices

def even_elements(input_list):
    even_list = [
        input_list[idx] 
        for idx in range(len(input_list))
        if idx % 2 == 1
    ]
    return even_list

print(even_elements([2, 3, 4, 5, 6]) == [3, 5])  # True
print(even_elements([1, 2, 3, 4]) == [2, 4])        # True
print(even_elements(["abc", "def"]) == ['def'])     # True
print(even_elements([123]) == [])                # True
print(even_elements([]) == [])                      # True