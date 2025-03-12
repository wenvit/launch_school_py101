### Problem statement:

# What will the following code output?

my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy() # duplicate of my_list1
my_list2[0]['first'] = 42 # mutate my_list2
print(my_list1) # unchanged

### Solution:

# This will print:  [{"first": 42}, {"second": "value2"}, 3, 4, 5]
# line 5, my_list1 assigned to list object consisting of nested dictionaries
#     plus integers
# line 6, my_list2 assigned to a shallow copy of my_list1
# line 7, my_list2 is mutated by making a reassignment of the value 
#         associated with 'first' key in dictionary object at index 0.
#         Because my_list2 is a shallow copy of my_list1, mutations of any
#         nested objects will be seen in the nested object of 
#         my_list1 as well