# What will the following code print and why? 

num = 5

def my_func():
    num = 10

my_func()
print(num)

# This will print: 5
# line 3, global variable `num` initialized to integer 5
# line 6, within body of function `my_func`, `num` is initialized
#     to integer 10. Because `num` is defined within function, it's a 
#     local variable separate from global `num`. Example of variable
#     shadowing. Can't reassign global variable from within function without
#     use of `global` keyword
# line 8, `my_func` is invoked passing no arguments, no value is returned
# line 9, `print` function invoked passing global `num` as argument because
#     local `num` not accessible in global scope