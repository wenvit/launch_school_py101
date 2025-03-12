# What will the following code do? 

def my_func():
    num = 10

my_func()
print(num)

# This will print: NameError num is not defined
# line 4, within body of functin `my_func`, a local
#    variable `num` is initialized to integer 10
# line 6, `my_func` is invoked passing no arguments
#    but there is no return value
# line 7, `print` is invoked passing `num` as argument
#    which results in an error because local `num` not
#    accessible in global scope