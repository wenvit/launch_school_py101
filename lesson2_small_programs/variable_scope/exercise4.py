# What will the following code print and why? 

def outer():
    outer_var = 'Hello'

    def inner():
        inner_var = 'World'
        print(outer_var, inner_var)

    inner()

outer()

# This will print: Hello World
# starting on line 3, definition of `outer` function begins
# line 4, variable `outer_var` initialized to string 'Hello'
#    `outer_var` is local to `outer` function and can be accessed
#    by any nested functions as well
# line 6, definition of nested `inner` function begins
# line 7, local variable `inner_var` initialized to string 'World'
# line 8, `print` invoked passing `outer_var` and `inner_var` as 
#    arguments. python can access `outer_var` from outer scope 
# line 10, `inner` function invoked
# line 12, `outer` function invoked 