##### Problem statement 

# Create a function that takes 2 arguments, a list and a dictionary.
# The list will contain 2 or more elements that, when joined with 
# spaces, will produce a person's name. The dictionary will contain 
# two keys, "title" and "occupation", and the appropriate values. 
# Your function should return a greeting that uses the person's full name, 
# and mentions the person's title.

# Example
# greeting = greetings(
#     ["John", "Q", "Doe"],
#     {"title": "Master", "occupation": "Plumber"},
# )
# print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.

########## PEDAC ##############

# inputs: list of names, dictionary with title & occupation
# outputs: function returns a greeting combining person's full name and title

# rules
# list elements are joined with spaces to produce person's name
# dictionary has two keys: 'title' and 'occupation'
# function should return greeting combining person's full name with title

# test cases
# greeting = greetings(
#     ["John", "Q", "Doe"],
#     {"title": "Master", "occupation": "Plumber"},
# )
# print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.

# data structure
# list to contain name elements
# dictionary to contain title + occupation key/value pairs

# algorithm
# 1. Define function `greetings` with two parameters: `name_lst`, `title_dict`
# 2. Invoke `join` method on `name_lst` to join name elements separated by
#    spaces; assign to variable `name`
# 3. Concatenate values associated with 'title' and 'occupation' dict keys
#    using `+` operator; assign to variable `title`.
# 4. `return` f-string that combines greeting with interpolation of `name` 
#    and `title` variables

# code

def greetings(name_lst, title_dict):
    name = ' '.join(name_lst)
    title = title_dict['title'] + ' ' + title_dict['occupation']
    
    return f'Hello, {name}! Nice to have a {title} around.'

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)