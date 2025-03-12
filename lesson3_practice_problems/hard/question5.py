### Problem statement:

# What do you expect to happen when the greeting variable 
# is referenced in the last line of the code below?

if False:
    greeting = "hello world"

print(greeting)

### Solution:

# This code will raise a NameError
# Because the if condition evaluations to falsy, the `greeting`
#   variable doesn't get initialized before the `print` function
#   is called 