##### Problem statement

# Build a program that displays when the user 
# will retire and how many years she has to work till retirement.

############# PEDAC ##############

# input: current age, retirement age 
# output: retirement year, number of years until retirement 

# rules
# assume valid inputs
# calculate number of years until retirement by subtracting 
#   current age from retirement age
# calculate retirement year by adding number of years until 
#   retirement to current year

# test case

# What is your age? 30
#At what age would you like to retire? 70

#It's 2024. You will retire in 2064.
#You have only 40 years of work to go!

# data structure
# integers

# algorithm
# 1. Import date from datetime module: `from datetime import date`
# 2. Obtain current year by invoking `date.today()` function, then
#    getting year attribute from the returned date object; assign to variable
#    `current_year`
# 3. Use `input` function to ask user to input current age and
#    desired retirement age; convert values to integers; assign
#    to variables `current_age` and `retire_age`
# 4. Calculate difference between `retire_age` and `current_age` and assign
#    to variable `yrs_until_retire`
# 4. Invoke `print` function with f-string argument that interpolates
#    `current_year`, as well as retirement year by adding `yrs_until_retire`
#    to `current_year`
# 5. Invoke `print` function with f-string argument that interpolates
#    `yrs_until_retire`

# code

from datetime import date

current_year = date.today().year

current_age = int(input('What is your age? '))
retire_age = int(input('At what age would you like to retire? '))
yrs_until_retire = retire_age - current_age

print(f"It's {current_year}. You will retire in {current_year + yrs_until_retire}.")
print(f'You only have {yrs_until_retire} years of work to go!')

