### Problem statement:

# What is the output of the following code?

answer = 42

def mess_with_it(some_number):
    return some_number + 8

new_answer = mess_with_it(answer)

print(answer - 8)

### Solution:

# This will print: 34

# `mess_with_it` function is defined with local variable
#    `some_number` that is separate from global `answer`. 
#    Function doesn't mutate global `answer` variable
# line 5, global `answer` variable initialized to 42. 
# line 7, `mess_with_it` function defined with parameter 
#       `some_number` (local variable)
# line 8, `mess_with_it` returns `some_number` + 8
# line 10, `mess_with_it` is called, passing `answer` (42) 
#       as argument, return value assigned to `new_answer`
# line 12, `print` invoked passing global `answer` variable - 8
#       as argument