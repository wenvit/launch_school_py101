##### Problem statement

# Create a simple tip calculator. The program should prompt 
# for a bill amount and a tip rate. The program must compute 
# the tip, then print both the tip and the total amount of the bill. 
# You can ignore input validation and assume that the user 
# will enter valid numbers.

# Example
# What is the bill? 200
# What is the tip percentage? 20

# The tip is $40.00
# The total is $240.00

############ PEDAC #################

# inputs (from user): bill, tip percentage
# outputs: calculated tip, total amount of bill

# rules
# Ignore input validation and assume valid numbers
# are input (bill and tip >0)
# Prompt for bill, tip percentage
# Multiply bill by tip percentage / 100 to determine tip amount
# Add bill to tip amount to determine total

# test cases
# bill: 200
# tip percentage: 20
# tip: 40
# total: 240

# data structure
# float

# algorithm
# 1. Ask user to input amount of bill; convert to float data type;
#    assign to variable `bill`
# 2. Ask user to input tip percentage; convert to float data type;
#    assign to variable `tip_percent`
# 3. Multiply `bill * tip_percent / 100` and assign to variable `tip`
# 4. Add `bill` and `tip` and assign to variable `total`
# 5. Invoke `print` function with f-string argument that interpolates `tip`
# 6. Invoke `print` function with f-string argument that interpolates `total`
# 7. `tip` and `total` should be printed with 2 decimal places.

# code

bill = float(input('What is the bill? '))
tip_percent = float(input('What is the tip percentage? '))

tip = bill * (tip_percent / 100)
total = bill + tip

print(f'The tip is ${tip:.2f}.')
print(f'The total is ${total:.2f}.')