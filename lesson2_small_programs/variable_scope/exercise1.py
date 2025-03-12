# What will the following code print and why? 

num = 5

def my_func():
    print(num)

my_func()

# This will print: 5
# line 3, global variable `num` is initialized to integer 5
# line 5, function `my_func` defined with no parameters
# line 6, within body of function, `print` function invoked passing
#      `num` as argument. `num` not defined locally so python
#      looks to global scope for definition and prints 5
# line 8, `my_func` invoked passing no arguments, 5 is printed