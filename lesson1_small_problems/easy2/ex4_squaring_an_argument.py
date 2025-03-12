##### Problem statement

# Using the multiply function from the "Multiplying Two Numbers" exercise, 
# write a function that computes the square of its argument 
# (the square is the result of multiplying a number by itself).

# Example
# print(square(5) == 25)   # True
# print(square(-8) == 64)  # True

######### PEDAC ##################

# input: number
# output: square of number

# rules
# assume valid numeric input
# rely on `multiply` function

# algorithm
# 1. Define function `square` with a single parameter `num`
# 2. Within body of function, pass `num` as an argument twice to
#    the `multiply` function and return result

# def multiply(num1, num2):
#     return num1 * num2

# def square(num):
#     return multiply(num, num)

# print(square(5) == 25)   # True
# print(square(-8) == 64)  # True

# Further Exploration
# Suppose we want to generalize this function to a "power to the n" 
# type function: cubed, to the 4th power, to the 5th, etc. 
# How would we go about doing so while still using the multiply function?

# 1. Define function `power` with parameters `number` and `n`
# 2. Handle power of 0 with conditional: `if n == 0: return 1`
# 3. else, initialize `result` by setting to `number`
# 4. `for` loop to iterate over range from 1 to `n`
#    with each iteration, invoke `multiply` passing arguments
#    `result` and `number` and reassign `result` to returned value
# 5. return `result`

def multiply(num1, num2):
    return num1 * num2

def power(number, n):

    if n == 0:
        return 1
    else:
        result = number
        for _ in range(1, n):    
            result = multiply(result, number)
        return result

print(power(3, 4))
print(power(2, 3))
print(power(2, 0))
print(power(4, 1))
print(power(5, 5))
print(power(-5, 5))
print(power(2, 8))