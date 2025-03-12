### Problem statement:

# Programmatically determine whether 42 lies between 10 and 100, 
# inclusive. Do the same for the values 100 and 101.

# Solution:

# print(42 >= 10 and 42 <= 100) # one way before looking at hint to use `range`

print(42 in range(10, 101))
print(100 in range(10, 101))
print(101 in range(10, 101))


