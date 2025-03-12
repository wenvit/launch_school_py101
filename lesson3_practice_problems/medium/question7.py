### Problem statement:

# One day, Spot was playing with the Munster family's home 
# computer, and he wrote a small program to mess with their 
# demographic data:

munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"

# After writing this function, he typed the following code:

mess_with_demographics(munsters)
print(munsters)

# Before Grandpa could stop him, Spot hit the Enter 
# key with his tail. Did the family's data get ransacked? 
# Why or why not?

### Solution:

# Yes, invoking `mess_with_demographics` and passing the 
# `munsters` dictionary object as argument will mutate the dictionary.
# Dictionaries are mutable objects. When `munsters` is passed as 
# an argument, a reference to the dictionary is passed, not a copy of the 
# object. Within the function, the local variable `demo_dict` points
# to the same dictionary object as `munsters`. When the key/value pairs
# are updated in the function, the dictionary is mutated. 

# Here's one way to retain original data

# import copy

# def mess_with_demographics():
#     updated_dict = copy.deepcopy(munsters)

#     for key, value in updated_dict.items():
#         value["age"] += 42
#         value["gender"] = "other"

# # After writing this function, he typed the following code:

# mess_with_demographics()
# print(munsters)