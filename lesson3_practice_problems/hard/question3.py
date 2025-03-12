### Problem statement:

# Given the following similar sets of code, what will each code snippet print?

# A

# def mess_with_vars(one, two, three):
#     one = two 
#     two = three 
#     three = one 

# one = ["one"]
# two = ["two"]
# three = ["three"]

# mess_with_vars(one, two, three)

# print(f"one is: {one}")
# print(f"two is: {two}")
# print(f"three is: {three}")

### Solution A:

# This will print:
# one is: ['one']
# two is: ['two']
# three is: ['three']

# line 7, `mess_with_vars` defined with parameters `one`, `two`, `three` 
#    which are local to the function. These local variables shadow the 
#    global variables `one`, `two`, `three`
# line 16, `mess_with_vars` invoked, passing ['one'], ['two'], ['three']
#    list objects by reference to `mess_with_vars`. 
#    Within function, `one`, `two`, `three` local variables point to same 
#    list objects as the global `one`, `two`, `three` variables
#  lines 8-10, local variable references to the lists are changed, however
#    the list objects themselves aren't mutated. Since these are local variable
#    references, the global variable `one`, `two`, and `three` aren't affected
#    and continue to point to ['one'], ['two'], ['three'] respectively

# B

# def mess_with_vars(one, two, three):
#     one = ["two"]
#     two = ["three"]
#     three = ["one"]

# one = ["one"]
# two = ["two"]
# three = ["three"]

# mess_with_vars(one, two, three)

# print(f"one is: {one}")
# print(f"two is: {two}")
# print(f"three is: {three}")

### Solution B:

# This will print:
# one is: ['one']
# two is: ['two']
# three is: ['three']

# line 43, `mess_with_vars` defined with parameters `one`, `two`, `three` 
#    which are local to the function. These local variables shadow the 
#    global variables `one`, `two`, `three`
# line 52, `mess_with_vars` invoked, passing ['one'], ['two'], ['three']
#    list objects by reference to `mess_with_vars`. 
#  lines 44-46, local variable references are reassigned to new list objects. This
#    doesn't mutate the original list objects, and because these are 
#    local variables, the global variables `one`, `two`, and `three` aren't affected
#    and continue to point to ['one'], ['two'], ['three'] respectively


# C

def mess_with_vars(one, two, three):
    one[0] = "two" #['two']
    two[0] = "three" #['three']
    three[0] = "one" #['one']

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

### Solution C:

# This will print:
# one is: ['two']
# two is: ['three']
# three is: ['one']

# line 80, `mess_with_vars` defined with parameters `one`, `two`, `three` 
#    which are local to the function. These local variables shadow the 
#    global variables `one`, `two`, `three`
# line 89, `mess_with_vars` invoked, passing ['one'], ['two'], ['three']
#    list objects by reference to `mess_with_vars`. 
#    Within function, `one`, `two`, `three` local variables point to same 
#    list objects as the global `one`, `two`, `three` variables
#  lines 81-83, list objects are mutated by reassigning elements at index 0
#    of all three lists. Because the global variables point to the same list
#    objects, the changes are seen in the global variables `one`, `two`, 
#    and `three` aren't affected
