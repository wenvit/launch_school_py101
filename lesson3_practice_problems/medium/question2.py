### Problem statement

# Alan wrote the following function, which was intended to 
# return all of the factors of number:

# def factors(number):
#     divisor = number
#     result = []
#     while divisor != 0:
#         if number % divisor == 0:
#             result.append(number // divisor)
#         divisor -= 1
#     return result

# Alyssa noticed that this code would fail when the input is 
# a negative number, and asked Alan to change the loop. How can he 
# make this work? Note that we're not looking to find the factors 
# for negative numbers, but we want to handle it gracefully instead 
# of going into an infinite loop.

# Bonus Question: What is the purpose of number % divisor == 0 in that code?

### Solution:

def factors(number):
    divisor = number
    result = []
    while divisor > 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result


# something like the following would give the user info on how
#    to fix the issue

# def factors(number):
#     if number < 0:
#         raise Exception('Number must be a positive integer.')
#     else:
#         divisor = number
#         result = []

#         while divisor != 0:
#             if number % divisor == 0:
#                 result.append(number // divisor)
#             divisor -= 1
#         return result

print(factors(-20))

# Bonus question:  
# `number % divisor == 0` identifies the factors because
#    factors are divisors with zero remainder
# `number % divisor == 0` evaluates as truthy if 
#    divisor is a factor