### Problem statement:

# Consider these two simple functions:

def foo(param="no"):
    return "yes"

def bar(param="no"):
    return (param == "no") and (foo() or "no")

# What will the following function invocation return?

print(bar(foo()))

### Solution:

# This will return: False

# line 5, `foo` function defined with parameter `param` that
#     has a default value of `no`. 
# line 6, `foo` returns 'yes' regardless of what `param` is
# line 8, `bar` defined with parameter `param` that has a 
#     default value of `no`
# line 9, returns result of expression:
#     (`param` == 'no') and (value returned by calling `foo` or 'no')

# line 13, `foo` is called with no argument, returns 'yes'
#    `bar` is invoked, passing return value of 'yes'
# expression with `bar` becomes:
# ('yes' == 'no') and ('yes' or 'no') which evalutes to False. Note
# Note that the right side of `and` operator is not evaluated because
# of short circuiting after the left side is False

