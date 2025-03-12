### Problem statement:

# What does the last line in the following code output?

# dictionary = {'first': [1]}
# num_list = dictionary['first']  # [1]
# num_list.append(2)  # [1, 2]

# print(num_list)
# print(dictionary)

### Solution:

# This will print:  {'first': [1, 2]}

# line 5, `dictionary` variable assigned to dictionary object with nested list value
# line 6, the `num_list` variable is assigned to nested list value of `dictionary`:
#     num_list = [1]. `num_list` references the same nested list associated with 
#     `dictionary['first']` key (both point to same object)
# line 7, `append` method is called on `num_list` with argument of 2
#     This mutates num_list:  num_list = [1, 2]
# Because `num_list` and `dictionary['first']` reference same object, mutating
#    `num_list` also shows up in the dictionary

# How would we update num_list without modifying the dictionary:

# one approach

# dictionary = {'first': [1]}
# num_list = dictionary['first'].copy()
# num_list.append(2)  

# print(num_list)
# print(dictionary)

# another approach

# dictionary = {'first': [1]}
# num_list = dictionary['first'] + [2]

# print(num_list)
# print(dictionary)

# also

dictionary = {'first': [1]}
num_list = dictionary['first'][:]
num_list.append(2)

print(num_list)
print(dictionary)