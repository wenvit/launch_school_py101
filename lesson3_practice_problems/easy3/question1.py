### Problem statement:

# Write two different ways to remove all of the elements 
# from the following list:

numbers = [1, 2, 3, 4]

### Solution

# one way using `clear` method

# numbers.clear()
# print(numbers)

# another way using `del`

# del numbers[:]
# print(numbers)

# another approach from launch school solution

while numbers:
    numbers.pop()

print(numbers)