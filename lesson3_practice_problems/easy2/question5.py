### Problem statement:

# How would you verify whether the data structures assigned 
# to the variables numbers and table are of type list?

numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

### Solution

# one way
# print(type(numbers) is list)
# print(type(table) is list)

# preferred solution

print(isinstance(numbers, list))
print(isinstance(table, list))