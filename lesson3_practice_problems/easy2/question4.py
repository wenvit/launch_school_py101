### Problem statement:

# Given a list of numbers [1, 2, 3, 4, 5], mutate the list by removing the 
# number at index 2, so that the list becomes [1, 2, 4, 5].

numbers = [1, 2, 3, 4, 5]

# Solution:

#numbers.pop(2) # one way
del numbers[2] # another way
print(numbers)