### Problem statement:

# Write two distinct ways of reversing the list 
# without mutating the original list.

numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

### Solution:

# `reverse` method mutates list so need other methods

# one way using slicing notation

# numbers_reversed = numbers[::-1]

# print(numbers_reversed)
# print(numbers)  # check that original list is not mutated

# another way using list comprehension using `reversed` function

# numbers_reversed = [
#     number
#     for number 
#     in reversed(numbers)
# ]

# more straightford using `list` constructor function
numbers_reversed = list(reversed(numbers))

print(numbers_reversed)
print(numbers)

# another way using range

# numbers_reversed = []

# for idx in range(len(numbers) - 1, -1, -1):
#     numbers_reversed.append(numbers[idx])

# print(numbers_reversed)
# print(numbers)