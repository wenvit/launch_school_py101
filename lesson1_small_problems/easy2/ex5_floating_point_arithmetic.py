##### Problem statement

# Write a program that prompts the user for two positive numbers 
# (floating-point), then prints the results of the following 
# operations on those two numbers: addition, subtraction, 
# product, quotient, floor quotient, remainder, and power. 
# Do not worry about validating the input.

############## PEDAC #############

# inputs: 2 postive numbers (floats)
# outputs: results of the following 
# operations on those two numbers: addition, subtraction, 
# product, quotient, floor quotient, remainder, and power

# rules
# do not worry about validating input
# user inputs positive floating point numbers
# mathematical operations use numbers in order they're input

# test cases
# ==> Enter the first number:
# 3.141529
# ==> Enter the second number:
# 2.718282
# ==> 3.141529 + 2.718282 = 5.859811
# ==> 3.141529 - 2.718282 = 0.42324699999999993
# ==> 3.141529 * 2.718282 = 8.539561733178
# ==> 3.141529 / 2.718282 = 1.1557038600115808
# ==> 3.141529 // 2.718282 = 1.0
# ==> 3.141529 % 2.718282 = 0.42324699999999993
# ==> 3.141529 ** 2.718282 = 22.45792517468373

# data structure
# float

# algorithm
# 1. Use `input` function to prompt user to input first number;
#    convert value to float data type.
# 2. Similarly, prompt for second number; convert to float.
# 3. Use a series of `print` function calls with f-strings to 
#    interpolate results of following mathematical operations: 
#    addition, subtraction, product, quotient, 
#    floor quotient, remainder, and power

# code

# float1 = float(input('==> Enter the first number:\n'))
# float2 = float(input('==> Enter the second number:\n'))

# print(f'==> {float1} + {float2} == {float1 + float2}')
# print(f'==> {float1} - {float2} == {float1 - float2}')
# print(f'==> {float1} * {float2} == {float1 * float2}')
# print(f'==> {float1} / {float2} == {float1 / float2}')
# print(f'==> {float1} // {float2} == {float1 // float2}')
# print(f'==> {float1} % {float2} == {float1 % float2}')
# print(f'==> {float1}**{float2} == {float1**float2}')

# another approach based on Launch School solution
# 1. Define function `calculator` with parameters
#    `float1`, `float2`, `operator`
# 2. Within function body, use a match/case statement 
#    to find operator, then return the result of that
#    particular mathematical operation
# 3. Use `for` loop to iterate over the list of operators,
#    and call `calculator` function passing each operator
#    as an argument, assign returned value to `result`. 
#    Print f-string and interpolate `result`

def calculator(float1, float2, operator):
    match operator:
        case '+': 
            return float1 + float2
        case '-':
            return float1 - float2
        case '*':
            return float1 * float2
        case '/':
            return float1 / float2
        case '//':
            return float1 // float2
        case '%':
            return float1 % float2
        case '**':
            return float1**float2
        
float1 = float(input('==> Enter the first number:\n'))
float2 = float(input('==> Enter the second number:\n'))

math_operators = ['+', '-', '*', '/', '//', '%', '**']

for operator in math_operators:

    result = calculator(float1, float2, operator)
    print(f'==> {float1} {operator} {float2} = {result}')



