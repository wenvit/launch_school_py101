# What will the following code print and why? 

def my_func():
    x = 15

    def inner_func1():
        x = 25
        print("Inner 1:", x)

    def inner_func2():
        print("Inner 2:", x)

    inner_func1()
    inner_func2()

my_func()

# This will print:
#     Inner 1: 25
#     Inner 2: 15

# line 4, within body of `my_func`, variable `x` is initialized to 15
#    This `x` is accessible within function scope and any nested functions.
# line 7, within body of `inner_func1`, local variable `x` is initialized
#    to 25. This `x` variable is separate from `x` in the next outer scope
# line 8, `print` invoked passing arguments 'Inner 1:' and `x`. This `x`
#    references local `x` value of 25
# line 11, within body of `inner_func2`, `print` invoked passing arguments
#    of 'Inner 2: ' and `x`. Because a local `x` variable is not defined in
#    `inner_func2`, python searches the outer scope and accesses the `x` value
#    of 15. `inner_func2` does not have access to `x` in its peer scope of `inner_func1`