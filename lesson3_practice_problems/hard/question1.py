### Problem statement:

# Will the following functions return the same results?

def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first())
print(second())

### Solution:

# The `first` function returns the dictionary object {'prop1': 'hi there'}
# The `second` function returns `None`. When Python encounters `return` it
#    terminates the function and returns to the line in the code where the function
#    was called. The code following the return statement is not executed.

