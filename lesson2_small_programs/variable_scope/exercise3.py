# What will the following code print and why?

num = 5

def my_func():
    global num
    num = 10

my_func()
print(num)

# This will print: 10
# line 3, global variable `num` initialized to integer 10
# line 6, within body of function `my_func`, `global` keyword
#     specifies that `num` within function is the global `num`
# line 7, global `num` reassigned to integer 10
# line 9, `my_func` invoked, which results in reassigning global
#     `num` to 10
# line 10, `print` invoked passing global `num` as argument, which
#     prints 10