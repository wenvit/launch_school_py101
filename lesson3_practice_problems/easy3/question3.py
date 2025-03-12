### Problem statement:

# What will the following code output?

str1 = "hello there"
str2 = str1  
str2 = "goodbye!"
print(str1)

### Solution:

# This will print:  hello there
# line 5, str1 is initialized to string object 'hello there'
# line 6, str2 is initialized to str1. Both str2 and str1 reference same
#     string object in memory 
# line 7, str2 is reassigned to 'goodbye!' 
# line 7 is a reassignment that points the 
#    str2 variable to a different string object in memory and 
#    str1 isn't affected


